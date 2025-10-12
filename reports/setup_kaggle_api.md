
# Kaggle API Setup Guide (Optional) / Kaggle API 配置指南（可选）

If in the future you want to automate dataset download from Kaggle, follow these steps:

1. Install Kaggle CLI:
   pip install kaggle

2. Get your API token:
   - Go to https://www.kaggle.com
   - Settings -> API -> Create New API Token
   - This will download a kaggle.json file

3. Configure locally:
   mkdir ~/.kaggle
   mv /path/to/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json

4. Test:
   kaggle datasets list -s hyperspectral

Notes:
- Keep kaggle.json private. / 请保管好 kaggle.json 文件，不要泄露。
