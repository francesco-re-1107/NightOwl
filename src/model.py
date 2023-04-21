import torch.nn as nn
import torchvision.models as models

class Model(nn.Module):

    def __init__(self):
        self.resnet50 = models.resnet50(weights='ResNet50_Weights.DEFAULT')

        for param in self.resnet50.parameters():
            param.requires_grad = False
        
        self.resnet50.fc = nn.Sequential(
            nn.Linear(2048, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, 3),
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        return self.resnet50(x)
