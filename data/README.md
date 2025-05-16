## Dataset
- Food 101 Kaggle : https://www.kaggle.com/datasets/dansbecker/food-101?utm_source=chatgpt.com
- uecfood 256 kaggle : https://www.kaggle.com/datasets/rkuo2000/uecfood256/code?utm_source=chatgpt.com

### 現在有點複雜@@
- 下載food101, uec256解壓縮
- Food101 : 
    - 把meta、images資料夾拉到data下
    - 執行split_data.py
- uecfood256 :
    - 執行split_uecfood256.py
[warning] 兩個py檔產生都是test / train資料夾，用第二個之前可能要改名