import os
import shutil
import random

# 1. 找到腳本所在目錄，並設定 UECFOOD256 路徑
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR    = os.path.join(BASE_DIR, "UECFOOD256")
CATEGORY_F  = os.path.join(ROOT_DIR, "category.txt")

# 2. 切分比例與隨機種子
SPLIT_RATIO = 0.8  # 80% train, 20% test
SEED        = 42
random.seed(SEED)

# 3. 解析 category.txt 得到 id → class_name 映射
mapping = {}
with open(CATEGORY_F, encoding="utf-8") as f:
    header = next(f)  # 跳過表頭
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) != 2:
            continue
        id_str, name = parts
        safe_name = (
            name
            .replace(" ", "_")
            .replace("'", "")
            .replace("/", "_")
        )
        mapping[id_str] = safe_name

# 4. 將數字資料夾改名為文字資料夾
for id_str, cls_name in mapping.items():
    src = os.path.join(ROOT_DIR, id_str)
    dst = os.path.join(ROOT_DIR, cls_name)
    if os.path.isdir(src) and not os.path.exists(dst):
        os.rename(src, dst)

# 5. 建立 train/ test 兩個資料夾
train_root = os.path.join(BASE_DIR, "train")
test_root  = os.path.join(BASE_DIR, "test")
for d in (train_root, test_root):
    os.makedirs(d, exist_ok=True)

# 6. 依類別切分並複製
for cls_name in mapping.values():
    cls_folder = os.path.join(ROOT_DIR, cls_name)
    if not os.path.isdir(cls_folder):
        continue

    imgs = [f for f in os.listdir(cls_folder) if f.lower().endswith(".jpg")]
    random.shuffle(imgs)
    n_train = int(len(imgs) * SPLIT_RATIO)

    for phase, subset in (("train", imgs[:n_train]), ("test", imgs[n_train:])):
        out_dir = os.path.join(BASE_DIR, phase, cls_name)
        os.makedirs(out_dir, exist_ok=True)
        for fn in subset:
            src = os.path.join(cls_folder, fn)
            dst = os.path.join(out_dir, fn)
            shutil.copy(src, dst)
    print(f"[{cls_name}]  train: {n_train},  test: {len(imgs)-n_train}")

print("切分完成 → ./train/, ./test/")
