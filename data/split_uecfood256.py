from datasets import load_from_disk, DatasetDict

# 1. 從剛才 save_to_disk 的路徑讀回來
ds_dict = load_from_disk("/data/uecfood256")
# ds_dict 可能長這樣：DatasetDict({'train': Dataset(num_rows=...)})

# 2. 取出唯一的 split
full_ds = ds_dict["train"]

# 3. 隨機切分：80% train、20% test，設定 seed 讓結果可重現
splits = full_ds.train_test_split(test_size=0.2, seed=42)
train_ds = splits["train"]
test_ds  = splits["test"]

# 4. （可選）把切好的 split 存回硬碟：
train_ds.save_to_disk("/data/uecfood256/train")
test_ds .save_to_disk("/data/uecfood256/test")
