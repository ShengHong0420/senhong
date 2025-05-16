from torchvision.datasets import Food101
from datasets import load_dataset

# 更 : 用kaggle比較快
# 下載 train split
# train_ds = Food101(root="data/food101", split="train", download=True)
# 下載 test split
# test_ds  = Food101(root="data/food101", split="test",  download=True)

# ds = load_dataset("tiennv/uecfood256", cache_dir="/data/hf_datasets")
# ds.save_to_disk("/data/uecfood256")