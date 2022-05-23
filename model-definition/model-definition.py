import torchvision.models as models
import torch.nn as nn
import torch


class Model(nn.Module):
    """Model architecture. Inputs in the init function can be added if needed."""
    def __init__(self, input_shape=(224,224), n_classes=2) -> None:
        super(Model, self).__init__()
        
        ### START CODE HERE ###
        self.input_shape = input_shape
        self.n_classes = n_classes
        
        # self.model = models.mobilenet_v2(pretrained=False)
        # self.model.classifier[-1] = torch.nn.Linear(in_features=1280, out_features=self.n_classes)
        # self.model = models.mobilenet_v2(pretrained=False)
        # self.model.classifier[-1] = torch.nn.Linear(in_features=1280, out_features=self.n_classes)
        self.model = models.vgg16(pretrained=False)
        self.model.classifier[-1] = torch.nn.Linear(in_features=4096, out_features=self.n_classes)

        # self.model = models.vgg16(pretrained=False)
        # self.model.classifier[-1] = torch.nn.Linear(in_features=4096, out_features=self.n_classes)
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

import json
filename = "/tmp/Model_" + id + ".json"
file_Model = open(filename, "w")
file_Model.write(json.dumps(Model))
file_Model.close()
