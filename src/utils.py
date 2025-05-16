import os
from PIL import Image

def load_image(img_path):
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"{img_path} not found.")
    return Image.open(img_path)

def print_result(food, cal):
    print(f"Food: {food}, Estimated Calories: {cal} kcal")
