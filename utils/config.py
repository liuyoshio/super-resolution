import torch
from torchvision import transforms

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
HR_SIZE = 256
LR_SIZE = 128

# Path to the WorldStrat dataset (High Resolution)
WorldStrat_path = "/Users/terry/Desktop/WorldStrat_hr/"

transform_hr = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((HR_SIZE, HR_SIZE)),
])

transform_lr = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((LR_SIZE, LR_SIZE)),
])