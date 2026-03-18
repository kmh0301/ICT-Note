---
name: python-assignment-generator
description: 用於生成 Python 程式設計作業的 JSON 檔案，遵循特定的語言和編碼慣例（說明用中文、代碼用英文）。
---

# Python 作業生成規則 (Python Assignment Generator)

本 Skill 用於協助教師生成符合學生學習進度與操作便利性的 Python 程式設計作業。

## 核心準則

1. **語言分配 (Language Convention)**:
    - **指引與注釋**: 使用 **繁體中文**。包括 JSON 中的 `title`、`content` 以及程式碼中的 `# 注釋`。
    - **程式碼操作**: 使用 **英文**。包括 `input()` 的提示語、`print()` 輸出的字串、變數名稱及狀態標籤（例如 FAT/THIN/FIT）。這是為了避免學生在編寫程式時需要頻繁切換輸入法。

2. **技術偏好 (Technical Preferences)**:
    - **開方運算**: 優先使用 `** 0.5` 代替 `math.sqrt()`，除非明確要求練習 Math module。
    - **數值格式化**: 使用 `:.3g` 處理「3 位有效數字」的要求（通常作為獎分任務）。
    - **輸入處理**: 優先使用 `float(input())` 處理數據以增加程式的適應性。

3. **自動評分與測試 (Testing & Marking)**:
    - **匹配類型**: 在 JSON 的 `testcases` 中，將 `match_type` 設為 `"C"` (Contains)。
    - **預期輸出**: 測試案例的 `output` 應只包含核心關鍵字（如 `FAT`、`Two real roots`），這樣即使學生的輸出包含額外的空格或數值格式不同，系統也能判定正確。

## JSON 檔案結構範例

```json
{
    "version": 1,
    "assignment": {
        "title": "繁體中文標題",
        "content": "<h3>HTML 格式的中文任務說明</h3>",
        "language": "python",
        "code_template": "print(\"English prompt:\")\nvariable = float(input())\n",
        "modal_solution": "...",
        "testcases": [
            {
                "input": "...",
                "output": "English Keywords",
                "match_type": "C"
            }
        ]
    }
}
```

## 使用情境

- 當用戶要求「建立一個關於 [主題] 的作業」時。
- 當用戶要求「準備測試案例和參考答案」時。
- 始終確保作業內容符合「中文說明、英文代碼」的平衡。
