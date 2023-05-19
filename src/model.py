import torch.nn as nn
import torchvision.models as models
from normalize import Normalize

class Model(nn.Module):

    def __init__(self, means, stds):
        self.normalize = Normalize(means, stds)

        self.resnet18 = models.resnet18()
        self.resnet18.fc = nn.Sequential(
            nn.Linear(self.resnet18.fc.in_features, 256),
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(256, 3), 
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        return self.resnet18(self.normalize(x))
