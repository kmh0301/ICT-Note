---
marp: true
theme: Dictation
paginate: true
---

<div class="header-info">
  <div class="school-info">佛教黃鳳翎中學</div>
  <div class="exam-info">資訊及通訊科技科——教學筆記</div>
</div>

# 電腦系統的組成部份 (Computer System Components)

## 1. 電腦硬件 (Computer Hardware)

- **（a）** 是構成電腦的實體裝置 (physical devices)。
- **（b）** 包括組成電腦的各種部件及周邊設備 (components and peripherals)。

## 2. 電腦硬件的四個基本組成部件 (Four Basic Components)

中央處理器 (CPU)、儲存部件 (storage)、輸入部件 (input) 及輸出部件 (output)。

## 3. 中央處理器 (Central Processing Unit - CPU)

- **（a）** 用來控制和協調 (control and coordinate) 電腦各部件的操作。
- **（b）** 是進行資料運算 (data processing) 的地方。
- **（c）** 主要部分：
  - **控制部件 (Control Unit)**：將各部件連繫及協調起來。
  - **算術及邏輯運算部件 (ALU - Arithmetic Logic Unit)**：負責算術運算及邏輯比較。

---
## 3. 中央處理器 (Central Processing Unit - CPU)
- **（d）** 機器週期 (Machine Cycle) 的四個步驟：
  讀取指令 (fetch) → 解譯指令 (decode) → 執行指令 (execute) → 儲存結果 (store)。
- **（e）** 時鐘比率 (clock speed) 是指電腦每秒能進行基本操作的比率，例如把兩個數值相加或把數值由一個記數器轉到別另一個記數器。當時鐘比率越高，電腦的運算速度亦越快。
- **（f）** 電腦以二進制 (binary) 形式進行儲存及運算資料。
- **（g）** 美國信息交換標準碼 (ASCII) 可以用來表示所有數字、大小寫英文字母和基本符號。
  

## 4. 主記憶體 (Primary Memory)

**（a）** 分為唯讀記憶體 (ROM) 和隨機存取記憶體 (RAM) 兩種：

| 特性 | ROM (Read-Only Memory) | RAM (Random Access Memory) |
|------|-----|-----|
| 主要用途 (Purpose) | 主要儲存了用來啟動電腦的指令 (boot instructions) | 儲存臨時的數據及指令 (temporary data) |
| 持久性 (Persistence) | 儲存的數據及資料是永久的 (permanent) | 儲存的數據及資料是暫時的 (temporary) |
| 可修改性 (Modifiable) | 儲存的資料不能隨便修改 (non-modifiable) | 儲存的資料可以讀取及修改 (readable & writable) |

**（b）** 儲存容量 (storage capacity) 可以字節 (Byte) 為基本單位，較大的容量可使用KB、MB、GB、TB等單位。

---

## 5. 輔助儲存器 (Secondary Storage)

- **（a）** 用來儲存一些長期性數據 (long-term data)。
- **（b）** 數據和程序可永久保存 (permanent storage)。
- **（c）** 例子包括硬碟 (hard disk)、光碟 (optical disk)、隨身儲存設備 (portable storage) 及雲端儲存 (cloud storage)。

## 6. 輸入部件 (Input Devices)

- **（a）** 用來把指令和數據輸入電腦 (input commands and data)。
- **（b）** 例子包括：鍵盤 (keyboard)、滑鼠 (mouse)、操縱桿 (joystick)、掃描器 (scanner) 等。

## 7. 輸出部件 (Output Devices)

- **（a）** 用來顯示電腦的運算結果或反饋的信息 (display results or feedback)。
- **（b）** 例子包括：顯示器 (monitor)、揚聲器 (speaker)、打印機 (printer) 等。

---
### 輸出類型比較 (Output Types Comparison)

| 特性 | 屏幕輸出 (Screen Output) | 列印輸出 (Print Output) |
|------|----------|----------|
| 輸出資料 (Output Data) | 文字、圖像及視像 (text, images, video) | 文字及圖像 (text & images) |
| 保存時間 (Duration) | 暫時性顯示影像 (temporary display) | 列印後可永久保存 (permanent after printing) |

## 8. 各部件之間的聯繫及數據流動 (Component Connections & Data Flow)

```
輸入部件 (Input) ←→ 中央處理器 (CPU) ←→ 輸出部件 (Output)
                    ↑      ↓
                  儲存部件 (Storage)
```

各部件之間透過數據匯流排 (data bus) 進行相互聯繫和數據傳輸，形成一個完整的電腦系統 (complete computer system)。