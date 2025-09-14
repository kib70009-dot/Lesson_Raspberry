# Gemini 啟動說明

本文件說明如何以不同方式啟動 Gemini。

## 透過指令列介面 (CLI)

最直接的方式是透過終端機或命令提示字元來啟動 Gemini CLI。

```bash
gemini [您的指令]
```

您可以直接輸入您的問題或指令。如果需要查看所有可用的選項和參數，可以使用 `--help` 旗標。

```bash
gemini --help
```

## 透過 API (使用 Google AI SDK)

如果您是開發者，希望在您的應用程式中整合 Gemini，您可以使用 Google AI SDK。這需要您先取得 API 金鑰，並安裝對應的程式庫。

### Python 範例

以下是一個基本的 Python 範例，展示如何初始化模型並開始對話：

```python
import google.generativeai as genai
import os

# 建議從環境變數或安全的地方讀取您的 API 金鑰
# os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# 選擇您要使用的模型
model = genai.GenerativeModel('gemini-pro')

# 開始一個對話
chat = model.start_chat(history=[])

# 傳送訊息
response = chat.send_message("你好！")

print(response.text)
```

在執行此程式碼之前，請確保您已經安裝了 SDK：

```bash
pip install -q -U google-generativeai
```
