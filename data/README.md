Kaggle CLI

bash
複製
編輯
# 安裝 kaggle 之後，下載到 /data
kaggle datasets download -d dansbecker/food-101 -p /data
# 解壓到 /data/food-101
unzip /data/food-101.zip -d /data/food-101
完成後，你會看到：

bash
複製
編輯
/data/food-101/images/train/…  
/data/food-101/images/test/…  
PyTorch torchvision

python
複製
編輯
from torchvision.datasets import Food101

# 下載並存到 /data/food101
train_ds = Food101(root="/data/food101", split="train", download=True)
test_ds  = Food101(root="/data/food101", split="test",  download=True)
下載完後會自動在 /data/food101/food-101/images/... 建好 train/test 兩個資料夾。

TensorFlow Datasets

python
複製
編輯
import tensorflow_datasets as tfds

# 指定 data_dir 為 /data/tfds
ds_train = tfds.load("food101",
                     split="train",
                     data_dir="/data/tfds",
                     as_supervised=True,
                     shuffle_files=True)
ds_val   = tfds.load("food101",
                     split="validation",
                     data_dir="/data/tfds",
                     as_supervised=True)
這樣所有 tfds 的原始檔、cache 也都會存在 /data/tfds/food101/...。

直接從官方網站 wget

bash
複製
編輯
# 下載到 /data
wget -P /data https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/food-101.tar.gz
# 解壓到 /data
tar -xzf /data/food-101.tar.gz -C /data
解完後，你會在 /data/food-101/images、/data/food-101/meta 看到原始圖片和標註檔。
