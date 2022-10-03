from tkinter import W
import torch
import torch.nn as nn
import torchvision
from PIL import Image
from torchvision.models.resnet import resnet50
import os

os.environ["CUDA_VISIBLE_DEVICES"]=""

checkpoint_path = '_ckpt_epoch_63.ckpt' 

transform = torchvision.transforms.Compose([
                            torchvision.transforms.Resize((224,224)),
                            torchvision.transforms.ToTensor(),
                            torchvision.transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])])

class Net(nn.Module):
    def __init__(self):
        super().__init__() 


        self.network = resnet50(pretrained = False)
        self.network = torch.nn.Sequential(*list(self.network.children())[:-1])
        
        self.fc1 = nn.Linear(2048,1)

    def forward(self,x ):
        x = self.network(x)
        x = x.view(-1,2048)
        x = self.fc1(x)
        x = torch.nn.Sigmoid()(x)
        return x


net = Net()
state_dict = torch.load(checkpoint_path, map_location=torch.device('cpu'))['state_dict']
net.load_state_dict(state_dict)
net.eval()

def classify(image_path):
    image_path = image_path 
    image = Image.open(image_path)
    image = transform(image)

    image = image[None,...]
    result = net(image)
    result = result.item()
    return result



