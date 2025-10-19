# GEMINI CLI 設定說明

本文件說明用於與 Gemini CLI 互動的各種 Prompt 設定。

## 1. System Prompt (系統提示)

System Prompt 是預先設定好的指令，它定義了 Gemini CLI 的核心行為、能力和限制。它包含了以下幾個要點：

- **角色定位**: Gemini 是一個由 Google 開發的大型語言模型，作為互動式 CLI 代理，專門處理軟體工程任務。
- **核心指令**:
    - 嚴格遵守現有的專案慣例。
    - 在使用函式庫或框架前，先確認其已在專案中被使用。
    - 模仿現有程式碼的風格、結構和架構。
    - 謹慎地新增註解，只在必要時解釋「為什麼」而不是「做什麼」。
    - 在超出請求範圍時，會先與使用者確認。
- **安全規則**:
    - 在執行可能修改檔案系統或系統狀態的關鍵指令前，必須先解釋其目的和潛在影響。
    - 絕不引入會洩漏敏感資訊（如 API 金鑰）的程式碼。
- **工具使用**:
    - 所有檔案路徑都必須使用絕對路徑。
    - 鼓勵並行執行獨立的工具呼叫。
    - 使用 `run_shell_command` 來執行 shell 指令。

這確保了 Gemini 在提供協助時，能夠保持一致、安全且高效。

## 2. User Prompt (使用者提示)

User Prompt 是指您（使用者）在命令列介面中輸入的指令或問題。它是您與 Gemini 互動的主要方式。

例如：
```
請幫我建立一個名為 "utils.py" 的檔案。
```
```
在 `main.py` 中，尋找所有名為 "calculate_total" 的函數。
```

Gemini 會根據您的 User Prompt 來理解您的需求，並利用其 System Prompt 中定義的能力和工具來完成任務。

## 3. Project Prompt (專案提示)

Project Prompt 是針對特定專案的客製化指令，通常儲存在專案根目錄的 `.gemini/GEMINI.md` 或類似的設定檔中。它允許開發者為特定專案覆寫或擴充 Gemini 的行為。

根據我收到的上下文，這個專案的 Project Prompt 設定如下：

```markdown
## AI遵守規則
 1.所有回覆使用繁體中文版
 2.你是一個有耐心的python老師
```

這表示在這個專案中，我被要求：
1.  所有回覆都必須使用**繁體中文**。
2.  我的角色是一位**有耐心的 Python 老師**。

此外，專案中也可能有名為 `GEMINI.md` 的檔案，用於記錄專案相關的筆記，例如 `/home/pi/Documents/github/Lesson_Raspberry/GEMINI.md` 的內容為：

```markdown
## 虛擬環境
- 使用uv建立的虛擬環境
- 所有python套件安裝請使用'uv add 套件名稱'

## 工作目錄描述
    Lesson_Raspberry是上課用的主目錄

## 目前次專案的工作目錄
    Lesson_Raspberry/俄羅斯方塊
```

這提供了關於專案環境和結構的附加上下文。

## 4. GEMINI CLI 的安裝與操作

本節說明如何安裝、啟動和使用 Gemini 命令列介面 (CLI)。

### 4.1 安裝與更新

為了獲得最新的功能和錯誤修復，請定期更新您的 Gemini CLI。更新方法會根據您的安裝方式而有所不同。

#### 透過套件管理器 (範例：npm, pip)
如果 CLI 是透過套件管理器安裝的：
```bash
# 如果是 Node.js 應用
npm update -g gemini-cli 
# 如果是 Python 應用
pip install --upgrade gemini-cli 
```

#### 透過下載最新版本
如果 CLI 是直接下載的可執行檔，您可能需要從官方來源下載最新版本並替換舊版本。

### 4.2 基本啟動

通常，Gemini CLI 會作為一個可執行檔提供。您可以在終端機中直接執行它。

#### 執行 Gemini CLI
```bash
gemini
```

#### 獲取幫助資訊
要查看可用的命令和選項，可以使用 `--help` 參數：
```bash
gemini --help
```
或者針對特定命令獲取幫助：
```bash
gemini [command] --help
```
例如：
```bash
gemini chat --help
```

### 4.3 帶有參數啟動

您可以透過在啟動時傳遞參數來配置 Gemini CLI 的行為。

#### 設定 API 金鑰 (範例)
如果您的 Gemini CLI 需要 API 金鑰，通常會透過環境變數或啟動參數來設定：

**透過環境變數 (推薦)**
```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
gemini chat "Hello, Gemini!"
```
**透過命令列參數 (如果支援)**
```bash
gemini chat --api-key "YOUR_API_KEY_HERE" "Hello, Gemini!"
```
> **請注意**：請查閱您的 Gemini CLI 文件以了解確切的 API 金鑰設定方式。

### 4.4 執行特定命令
Gemini CLI 通常包含多個子命令，用於執行不同的任務。

**範例：進行聊天**
```bash
gemini chat "請幫我寫一首關於秋天的詩。"
```

**範例：生成程式碼**
```bash
gemini code "用 Python 寫一個計算斐波那契數列的函數。"
```

### 4.5 配置檔案
某些 Gemini CLI 工具可能支援透過配置檔案來管理設定，例如 `~/.gemini/config.yaml` 或專案根目錄下的 `.geminirc`。請查閱相關文件以了解配置檔案的使用方法。

> **免責聲明**：上述指令是通用範例。請務必參考您所使用的 Gemini CLI 的官方文件，以獲取最準確和最新的啟動與使用說明。