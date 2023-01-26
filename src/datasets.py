import os
import cv2
from torch.utils.data import Dataset
from utils.config import WorldStrat_path, transform_hr, transform_lr
from utils.helper import random_crop

# custom dataset class
# only takes the high resolution image directory
# pass in the downgrading method is optional
class MyDataset(Dataset):
    def __init__(self, directory_path, downgrading_method=None):
        # get all file names in the directory
        self.directory_path = directory_path
        self.file_list = os.listdir(directory_path)
        self.downgrading_method = downgrading_method

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, index):
        # Return the data and target at the given index
        img_hr = cv2.imread(os.path.join(self.directory_path, self.file_list[index]))
        img_hr = cv2.cvtColor(img_hr, cv2.COLOR_BGR2RGB)
        img_hr = cv2.resize(img_hr, (1088, 1088))
        
        if self.downgrading_method is None:
            img_lr = cv2.resize(img_hr, (img_hr.shape[1] // 8, img_hr.shape[0] // 8), interpolation=cv2.INTER_AREA)
        else:
            img_lr = self.downgrading_method(img_hr)
            
        return transform_hr(img_hr), transform_lr(img_lr)

if __name__ == '__main__':
    # create the dataset
    dataset = MyDataset(WorldStrat_path)
    print('Dataset size: ', len(dataset))