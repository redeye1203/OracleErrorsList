# Oracle 錯誤代碼查詢工具

這是一個基於 Kivy 的 GUI 應用程式，用於查詢 Oracle 資料庫錯誤代碼及其對應的錯誤說明。

## 功能特色

- 🔍 快速搜尋 Oracle 錯誤代碼
- 🌐 支援錯誤訊息翻譯（使用 Google Translate）
- 📱 簡潔直觀的用戶介面
- 📋 包含大量 Oracle 錯誤代碼資料庫

## 安裝需求

### 系統需求
- Python 3.7 或更高版本
- Windows/Linux/macOS

### 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方法

1. 執行程式：
```bash
python main.py
```

2. 在搜尋框中輸入 Oracle 錯誤代碼（如：ORA-00001）
3. 點擊「搜尋」按鈕查看錯誤說明
4. 如需翻譯，可使用翻譯功能

## 專案結構

```
OracleErrorsList/
├── main.py           # 主程式檔案
├── requirements.txt  # 依賴套件清單
└── README.md        # 專案說明文件
```

## 主要依賴

- **Kivy** - GUI 框架，用於建立跨平台的桌面應用程式
- **deep-translator** - 翻譯功能，支援 Google Translate

## 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 文件

## 免責聲明

此工具僅供教育和參考用途。使用者應自行驗證錯誤代碼的準確性，作者不對使用此工具產生的任何後果負責。