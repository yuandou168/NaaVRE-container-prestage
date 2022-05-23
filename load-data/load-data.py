from torch.utils.data import DataLoader
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--CustomDataset', action='store' , required='True', dest='CustomDataset')


args = arg_parser.parse_args()

id = args.id

CustomDataset = args.CustomDataset



def load_data(data_path, input_shape=(224,224)):
    """Load data (training, validation and test sets).
    Required outputs: loaders of each set and dictionary containing the length of each corresponding set
    """
    ### START CODE HERE ###
    trainset = CustomDataset(partition_file="train_client_3b", folder=data_path, input_shape=input_shape)
    valset = CustomDataset(partition_file="val_client_3", folder=data_path, input_shape=input_shape)
    testset = CustomDataset(partition_file="test_v2", folder=data_path, input_shape=input_shape)
    

    trainloader = DataLoader(trainset, batch_size=64, shuffle=True)
    valloader = DataLoader(valset, batch_size=64, shuffle=True)
    testloader = DataLoader(testset, batch_size=64, shuffle=True)
    ### END CODE HERE ###
    
    num_examples = {"trainset" : len(trainset), "valset": len(valset), "testset" : len(testset)}
    
    return trainloader, valloader, testloader, num_examples

