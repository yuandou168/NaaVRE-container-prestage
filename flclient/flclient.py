import torch
import time
import flwr as fl
from collections import OrderedDict
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--DEVICE', action='store' , type=str , required='True', dest='DEVICE')
arg_parser.add_argument('--load_data', action='store' , type=str , required='True', dest='load_data')
arg_parser.add_argument('--Model', action='store' , required='True', dest='Model')
arg_parser.add_argument('--test', action='store' , type=str , required='True', dest='test')
arg_parser.add_argument('--train', action='store' , type=str , required='True', dest='train')


args = arg_parser.parse_args()

id = args.id

DEVICE = args.DEVICE
load_data = args.load_data
Model = args.Model
test = args.test
train = args.train



net = Model().to(DEVICE)
s1 = time.time()
trainloader, valloader, testloader, num_examples = load_data("./data_laeti")
print("time to load the data for this client: ", time.time()-s1)

class HistologyClient(fl.client.NumPyClient):
    def __init__(self, model, trainloader, valloader, testloader, num_examples) -> None:
        self.model = model
        self.trainloader = trainloader
        self.valloader = valloader
        self.testloader = testloader
        self.num_examples = num_examples
    def get_parameters(self):
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]
    def set_parameters(self, parameters):
        params_dict = zip(self.model.state_dict().keys(), parameters)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        self.model.load_state_dict(state_dict, strict=True)
    def fit(self, parameters, config):
        self.set_parameters(parameters)
        train(self.model, self.trainloader, self.valloader, epochs=10)
        return self.get_parameters(), self.num_examples["trainset"], {}
    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        loss, accuracy = test(self.model, self.testloader)
        print("==== loss, accuracy", loss, accuracy)
        return float(loss), self.num_examples["testset"], {"accuracy": float(accuracy)}
    
    # client = HistologyClient()

start_time = time.time()
client = HistologyClient(net, trainloader, valloader, testloader, num_examples)
fl.client.start_numpy_client("152.228.166.247:8080", client=client, grpc_max_message_length=895_870_912)
finish_time = time.time()

print("==== TOTAL TIME TO TRAIN THE FEDERATION: ", finish_time-start_time)
print("FINISHED")
loss, acc = test(client.model, client.testloader)
print("FINAL MODEEEEL: ")
print(loss, acc)
torch.save(client.model.state_dict(), "final_model_v1.pt")

