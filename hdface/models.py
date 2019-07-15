import torch
import torch.nn as nn
import torch.nn.functional as F

class PNet(nn.Module):
    ''' PNet '''

    def __init__(self, is_train=False, use_cuda=True):
        super(PNet, self).__init__()
        self.is_train = is_train
        self.use_cuda = use_cuda

        # backend
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3, 10, kernel_size=3, stride=1),  # conv1
            nn.BatchNorm2d(10),
            nn.PReLU(),  # PReLU1
            nn.MaxPool2d(kernel_size=2, stride=2),  # pool1
            nn.Conv2d(10, 16, kernel_size=3, stride=1),  # conv2
            nn.BatchNorm2d(16),
            nn.PReLU(),  # PReLU2
            nn.Conv2d(16, 32, kernel_size=3, stride=1),  # conv3
            nn.BatchNorm2d(32),
            nn.PReLU()  # PReLU3
        )
        # detection
        self.conv4_1 = nn.Conv2d(32, 1, kernel_size=1, stride=1)
        # bounding box regresion
        self.conv4_2 = nn.Conv2d(32, 4, kernel_size=1, stride=1)
        # landmark localization
        self.conv4_3 = nn.Conv2d(32, 10, kernel_size=1, stride=1)

        # weight initiation with xavier

    def forward(self, x):
        x = self.pre_layer(x)
        label = F.sigmoid(self.conv4_1(x))
        offset = self.conv4_2(x)
        # landmark = self.conv4_3(x)

        if self.is_train is True:
            # label_loss = LossUtil.label_loss(self.gt_label,torch.squeeze(label))
            # bbox_loss = LossUtil.bbox_loss(self.gt_bbox,torch.squeeze(offset))
            return label,offset
        #landmark = self.conv4_3(x)
        return label, offset





class RNet(nn.Module):
    ''' RNet '''

    def __init__(self,is_train=False, use_cuda=True):
        super(RNet, self).__init__()
        self.is_train = is_train
        self.use_cuda = use_cuda
        # backend
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3, 28, kernel_size=3, stride=1),  # conv1
            nn.BatchNorm2d(28),
            nn.PReLU(),  # prelu1
            nn.MaxPool2d(kernel_size=3, stride=2),  # pool1
            nn.Conv2d(28, 48, kernel_size=3, stride=1),  # conv2
            nn.BatchNorm2d(48),
            nn.PReLU(),  # prelu2
            nn.MaxPool2d(kernel_size=3, stride=2),  # pool2
            nn.Conv2d(48, 64, kernel_size=2, stride=1),  # conv3
            nn.BatchNorm2d(64),
            nn.PReLU()  # prelu3

        )
        self.conv4 = nn.Linear(64*2*2, 128)  # conv4
        self.prelu4 = nn.PReLU()  # prelu4
        # detection
        self.conv5_1 = nn.Linear(128, 1)
        # bounding box regression
        self.conv5_2 = nn.Linear(128, 4)
        # lanbmark localization
        self.conv5_3 = nn.Linear(128, 10)
        # weight initiation weih xavier

    def forward(self, x):
        # backend
        x = self.pre_layer(x)
        x = x.view(x.size(0), -1)
        x = self.conv4(x)
        x = self.prelu4(x)
        # detection
        det = torch.sigmoid(self.conv5_1(x))
        box = self.conv5_2(x)
        # landmark = self.conv5_3(x)

        if self.is_train is True:
            return det, box
        #landmard = self.conv5_3(x)
        return det, box




class ONet(nn.Module):
    ''' RNet '''

    def __init__(self,is_train=False, use_cuda=True):
        super(ONet, self).__init__()
        self.is_train = is_train
        self.use_cuda = use_cuda
        # backend
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1),  # conv1
            nn.BatchNorm2d(32),
            nn.PReLU(),  # prelu1
            nn.MaxPool2d(kernel_size=3, stride=2),  # pool1
            nn.Conv2d(32, 64, kernel_size=3, stride=1),  # conv2
            nn.BatchNorm2d(64),
            nn.PReLU(),  # prelu2
            nn.MaxPool2d(kernel_size=3, stride=2),  # pool2
            nn.Conv2d(64, 64, kernel_size=3, stride=1),  # conv3
            nn.BatchNorm2d(64),
            nn.PReLU(), # prelu3
            nn.MaxPool2d(kernel_size=2,stride=2), # pool3
            nn.Conv2d(64,128,kernel_size=2,stride=1), # conv4
            nn.BatchNorm2d(128),
            nn.PReLU() # prelu4
        )
        self.conv5 = nn.Linear(128*2*2, 256)  # conv5
        self.prelu5 = nn.PReLU()  # prelu5
        # detection
        self.conv6_1 = nn.Linear(256, 1)
        # bounding box regression
        self.conv6_2 = nn.Linear(256, 4)
        # lanbmark localization
        self.conv6_3 = nn.Linear(256, 10)
        # weight initiation weih xavier

    def forward(self, x):
        # backend
        x = self.pre_layer(x)
        x = x.view(x.size(0), -1)
        x = self.conv5(x)
        x = self.prelu5(x)
        # detection
        det = torch.sigmoid(self.conv6_1(x))
        box = self.conv6_2(x)
        landmark = self.conv6_3(x)
        if self.is_train is True:
            return det, box, landmark
        #landmard = self.conv5_3(x)
        return det, box, landmark
