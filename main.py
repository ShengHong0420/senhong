import os
from PIL import Image

from src.classifier import FoodClassifier
from src.detector import FoodDetector
from src.calorie_estimator import estimate_calorie
from src.recommender import recommend_by_culture
from src.ingredient_helper import ask_user_ingredients, refine_calorie
from src.utils import load_image, print_result

# ==== 初始化模型 ====
classifier = FoodClassifier(model_path='models/food_classifier.pt')
detector = FoodDetector(model_path='models/yolov5_food.pt')

# ==== 使用者參數（模擬）====
user_culture = 'taiwanese'
user_history = ['braised_pork_rice', 'fried_chicken']

# ==== 主流程 ====
def process_image(image_path):
    print(f"\n Processing: {image_path}")
    image = load_image(image_path)

    # === 偵測圖片中食物位置 ===
    detections = detector.detect(image_path)
    if detections.empty:
        print("No food detected.")
        return

    for i, row in detections.iterrows():
        # Crop 食物區塊
        x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
        cropped = image.crop((x1, y1, x2, y2))

        # === 分類食物類型 ===
        food_type = classifier.predict(cropped)
        print(f" Detected food: {food_type}")

        # === 模擬詢問烹調方式 ===
        cook_method = input(f" What is the cooking method for '{food_type}'? (fried/boiled/raw): ")

        # === 預估初步卡路里 ===
        base_cal = estimate_calorie(food_type, cook_method)
        print(f" Base calorie: {base_cal} kcal")

        # === 成分調整 ===
        ing = ask_user_ingredients(food_type)
        final_cal = refine_calorie(base_cal, ing)

        # === 輸出結果 ===
        print_result(food_type, final_cal)

# ==== 餐點推薦 ====
def recommend_food():
    print("\n Personalized Menu Recommendation")
    suggestions = recommend_by_culture(user_culture, history=user_history)
    if suggestions:
        print(" You haven't tried:")
        for food in suggestions:
            print(f"   {food}")
    else:
        print("You’ve tried everything in this cuisine!")

# ==== 主程式入口 ====
if __name__ == "__main__":
    # 跑一張測試圖（之後可以改成資料夾 batch）
    test_image_path = 'test_images/lunch.jpg'
    process_image(test_image_path)

    # 推薦還沒吃過的餐點
    recommend_food()
