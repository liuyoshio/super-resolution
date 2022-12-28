from torchvision import transforms

HR_SIZE = 256
LR_SIZE = 128
HEIGHT = 500
WIDTH = 500

# Path to the WorldStrat dataset (High Resolution)
WorldStrat_path = '/Users/terry/Desktop/WorldStrat_hr'


transform_hr = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((HR_SIZE, HR_SIZE)),
])

transform_lr = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((LR_SIZE, LR_SIZE)),
])