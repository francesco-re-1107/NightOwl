import torch.nn as nn
import torchvision.models as models
from torchvision.transforms import Normalize

class Model(nn.Module):

    def __init__(self, means, stds):
        super(Model, self).__init__()
        self.normalize = Normalize(means, stds)

        """self.resnet18 = models.resnet18()
        self.resnet18.fc = nn.Sequential(
            nn.Linear(self.resnet18.fc.in_features, 256),
            nn.ReLU(),
            nn.Dropout(0.6),
            nn.Linear(256, 3), 
            nn.LogSoftmax(dim=1)
        )"""
        self.mobilenet_v3 = models.mobilenet_v3_small()
        self.mobilenet_v3.classifier = nn.Sequential(
            nn.Dropout(0.2, inplace=True),
            nn.Linear(576, 3),
            nn.LogSoftmax(dim=1)
        )

    def forward(self, x):
        return self.mobilenet_v3(self.normalize(x))
