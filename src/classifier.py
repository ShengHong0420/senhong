import torch
import torchvision.transforms as transforms
from torchvision import models

class FoodClassifier:
    def __init__(self, model_path=None, num_classes=101):
        self.model = models.mobilenet_v2(pretrained=True)
        self.model.classifier[1] = torch.nn.Linear(self.model.last_channel, num_classes)
        if model_path:
            self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
    
    def predict(self, image):
        # Assume image is a PIL image
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor()
        ])
        input_tensor = transform(image).unsqueeze(0)
        with torch.no_grad():
            output = self.model(input_tensor)
        return torch.argmax(output, dim=1).item()
