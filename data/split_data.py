import os
import shutil

# 根目錄設定
BASE_DIR = "data"
IMG_DIR  = os.path.join(BASE_DIR, "images")
META_DIR = os.path.join(BASE_DIR, "meta")

for split in ("train", "test"):
    txt_path = os.path.join(META_DIR, f"{split}.txt")
    out_dir  = os.path.join(BASE_DIR, split, "images")

    # 建資料夾
    os.makedirs(out_dir, exist_ok=True)

    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            rel = line.strip().lstrip("/\\")       # e.g. "apple_pie/1011328"
            if not rel:
                continue

            # 拆出 class name 與 image id
            cls, img_id = rel.split("/")
            src = os.path.join(IMG_DIR, cls, img_id + ".jpg")
            dst_dir = os.path.join(out_dir, cls)
            dst = os.path.join(dst_dir, img_id + ".jpg")

            # 確保來源存在，並建立目的資料夾
            if not os.path.exists(src):
                print(f"[WARN] 找不到檔案：{src}")
                continue
            os.makedirs(dst_dir, exist_ok=True)

            # 複製圖片
            shutil.copy(src, dst)

    print(f"→ 完成 split={split}，輸出至 `{split}/images/`")
