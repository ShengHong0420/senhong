from torchvision.datasets import Food101

# 下載 train split
train_ds = Food101(root="data/food101", split="train", download=True)
# 下載 test split
test_ds  = Food101(root="data/food101", split="test",  download=True)
