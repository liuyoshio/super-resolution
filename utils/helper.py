import os
import numpy as np
import torch
import matplotlib.pyplot as plt 
from .config import DEVICE

# Visualize the dataset
# example: datasets[0] -> (HR image, LR image)
def visualize_dataset(dataset):
    image_hr = dataset[0].permute(1, 2, 0).numpy()
    image_lr = dataset[1].permute(1, 2, 0).numpy()

    _, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image_hr)
    ax[0].set_title('HR image')

    ax[1].imshow(image_lr)
    ax[1].set_title('LR image')

    plt.show()

# Random crop the image by crop_sizexcrop_size
def random_crop(img, crop_size):
    h, w = img.shape[:2]
    top = np.random.randint(0, h - crop_size)
    left = np.random.randint(0, w - crop_size)
    img = img[top:top+crop_size, left:left+crop_size]
    return img

# laod model dict
def load_model_dict(model, model_path):
    if not os.path.isfile(model_path):
        print ('Model path is not exist!')
        return
    model.load_state_dict(torch.load('model_path', map_location=DEVICE))