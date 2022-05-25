import time
import numpy as np
import pandas as pd
import torchvision.models as models
import ssl
from torch.utils.data import DataLoader
import cv2
import torch.nn as nn
import torch
from sklearn.metrics import confusion_matrix
import flwr as fl
from collections import OrderedDict
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--input_path', action='store' , type=str , required='True', dest='input_path')
arg_parser.add_argument('--server_IP_port', action='store' , type=str , required='True', dest='server_IP_port')


args = arg_parser.parse_args()

id = args.id

input_path = args.input_path
server_IP_port = args.server_IP_port




ssl._create_default_https_context = ssl._create_unverified_context

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


input_path = input_path
server_IP_port = server_IP_port

def load_images(df_data, dir_data, input_shape):
    """Function to load images to study and apply preprocessing if needed."""
    list_images = []
    
    print("dir_data: ", dir_data)
    for i in range(0, len(df_data)):
        img = cv2.imread(dir_data + df_data.images[i])
        img = cv2.resize(img, input_shape)
        list_images.append(img)

    return np.array(list_images)

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, partition_file, folder, input_shape):
        ### START CODE HERE ###
        self.input_shape = input_shape
        
        df_data = pd.read_csv(folder + "/" + partition_file + '.csv', dtype=str, delimiter=',')
        print("count values in df:\n", df_data['GT'].value_counts())
        val_counts = df_data['GT'].value_counts()
        factor = 1-(val_counts[1]/val_counts[0])
        df_data = df_data.drop(df_data.loc[df_data['GT']=='0'].sample(frac=float(factor)).index).reset_index()
        print("count values in df after balancing:\n", df_data['GT'].value_counts())
        self.X = load_images(df_data, folder, self.input_shape)
        self.Y = df_data.GT
        self.Y = [int(el) for el in self.Y]
        
        ### END CODE HERE ###
        
        self.indexes = np.arange(0, len(self.X))
        
    def __len__(self):
        """Required output: length of the dataset"""
        return self.X.shape[0]
    
    def __getitem__(self, idx):
        """Required input: index to access
        Required output: image corresponding to the input index and its label"""
        
        image = self.X[idx]
        label = self.Y[idx]
        
        return image, label
    

def load_data(data_path, input_shape=(224,224)):
    """Load data (training, validation and test sets).
    Required outputs: loaders of each set and dictionary containing the length of each corresponding set
    """
    ### START CODE HERE ###
    trainset = CustomDataset(partition_file="train_client", folder=data_path, input_shape=input_shape)
    valset = CustomDataset(partition_file="val_client", folder=data_path, input_shape=input_shape)
    testset = CustomDataset(partition_file="test", folder=data_path, input_shape=input_shape)
    
    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    valloader = DataLoader(valset, batch_size=64, shuffle=True)
    testloader = DataLoader(testset, batch_size=64, shuffle=True)
    ### END CODE HERE ###
    
    num_examples = {"trainset" : len(trainset), "valset": len(valset), "testset" : len(testset)}
    
    return trainloader, valloader, testloader, num_examples


class Model(nn.Module):
    """Model architecture. Inputs in the init function can be added if needed."""
    def __init__(self, input_shape=(224,224), n_classes=2) -> None:
        super(Model, self).__init__()
        
        ### START CODE HERE ###
        self.input_shape = input_shape
        self.n_classes = n_classes
        
        self.model = models.mobilenet_v2(pretrained=False)
        self.model.classifier[-1] = torch.nn.Linear(in_features=1280, out_features=self.n_classes)
        
        ### END CODE HERE ###
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Required input: tensor of images to predict
        Required output: output of the model given the images tensor in input"""
            
        ### START CODE HERE ###
        x = x.permute(0, 3, 1, 2)
        x = self.model(x)
        x = torch.squeeze(x)
        ### END CODE HERE ###
        
        return x


def train(net, trainloader, valloader, epochs):
    """Train the network on the training set, evaluating it on the validation set at each epoch."""
    criterion = torch.nn.CrossEntropyLoss() #TODO Define loss function
    optimizer = torch.optim.SGD(net.parameters(), lr=0.001) #TODO Define optimizer
    
    start = time.time()
    for i_epoch in range(epochs):
        ### START CODE HERE ###
        print("Epoch ", i_epoch+1)
        
        correct, total, train_loss_epoch = 0, 0, 0.0
        for images, labels in trainloader:
            images = torch.from_numpy(np.asarray(images).astype('float32'))
            images, labels = images.to(DEVICE), labels.to(DEVICE)
            optimizer.zero_grad()
            
            outputs = net(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            loss_iteration = criterion(outputs, labels)
            loss_iteration.backward()
            optimizer.step()
            
            optimizer.zero_grad()
            
            train_loss_epoch += loss_iteration.item()
        
        train_loss_epoch = train_loss_epoch / total
        train_acc_epoch = correct / total
        val_loss_epoch, val_acc_epoch = test(net, valloader)
        info = "[INFO] Epoch {}/{} - train_loss: {:.6f} - train_acc: {:.6f} - val_loss: {:.6f} - val_acc: {:.6f}".format(
                i_epoch + 1, epochs, train_loss_epoch, train_acc_epoch, val_loss_epoch, val_acc_epoch)
        print(info + "\n")
        
    end = time.time()
    print("Time to train the whole network: ", end-start, " s")
        
        ### END CODE HERE ###

def test(net, testloader):
    """Validate the network on the entire test set."""
    criterion = torch.nn.CrossEntropyLoss()
    correct, total, loss = 0, 0, 0.0
    whole_labels, whole_predicted = torch.Tensor([]), torch.Tensor([])
    with torch.no_grad():
        for data in testloader:
            images = torch.from_numpy(np.asarray(data[0]).astype('float32'))
            images, labels = images.to(DEVICE), data[1].to(DEVICE)
            outputs = net(images)
            loss += criterion(outputs, labels).item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            whole_labels = torch.cat((whole_labels.cpu(), labels.cpu()))
            whole_predicted = torch.cat((whole_predicted.cpu(), predicted.cpu()))
    print("CONFUSION MATRIX:")
    print(confusion_matrix(whole_labels.cpu(), whole_predicted.cpu()))
    accuracy = correct / total
    loss = loss / total
    return loss, accuracy
        
        
        # Load model and data

net = Model().to(DEVICE)
trainloader, valloader, testloader, num_examples = load_data(input_path)

class HistologyClient(fl.client.NumPyClient):
    def get_parameters(self):
        return [val.cpu().numpy() for _, val in net.state_dict().items()]

    def set_parameters(self, parameters):
        params_dict = zip(net.state_dict().keys(), parameters)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        net.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        train(net, trainloader, valloader, epochs=5)
        return self.get_parameters(), num_examples["trainset"], {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        loss, accuracy = test(net, testloader)
        print("==== loss, accuracy", loss, accuracy)
        return float(loss), num_examples["testset"], {"accuracy": float(accuracy)}

fl.client.start_numpy_client(server_IP_port, client=HistologyClient())

print("FINISHED")

