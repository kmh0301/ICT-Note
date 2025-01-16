---
up: []
aliases:
  - Export to Anki (plugin)
---
- 參考資料：[官方documentation](https://github.com/ObsidianToAnki/Obsidian_to_Anki/wiki)
	- [regex](https://github.com/ObsidianToAnki/Obsidian_to_Anki/wiki/Regex)

# 安裝與設定
## 第一次安裝-Anki端設定（基本上只要做一次）

1. 打開Anki，開啟到想要使用的個人檔案。
2. 安裝「Anki Connect」這個Add-on：
	1. 選擇`Tool > Add-ons > Get Add-ons`
	2. 輸入代碼 `2055492159`，按OK
4. 修改「Anki Connect」的設定：點選，Tools > Add-ons > Anki Connect > Config，然後在如下所示的位置加上 `"app://obsidian.md"` 這行程式碼

```
{
    "apiKey": null,
    "apiLogPath": null,
    "ignoreOriginList": [],
    "webBindAddress": "127.0.0.1",
    "webBindPort": 8765,
    "webCorsOriginList": [
        "http://localhost",
        "app://obsidian.md"
    ]
}
```

4. 重新啟動Anki
5. 幫要用的Anki的note type新增「Obsidian Link」和「Obsidian Context」欄位，
6. 設定這兩個欄位在卡面上出現：Cards > Back template > 貼上下列程式碼：

```
<br><br><br>

<div style='font-size: 12px;'>{{Obsidian Link}} {{Obsidian Context}}</div>
```

7. 在Anki中新增需要的牌組

## Obsidian端設定（若重啟plugin要再做一次的設定）
 
- 設定note type table
	- 設定在用的note type的 link field & context field
		- Basic, Cloze
	- 貼上regex
		- Basic: `((?:[^\n][\n]?)+) #flashcard ?\n*((?:\n(?:^.{1,3}$|^.{4}(?<!<!--).*))+)`
		- Cloze: `((?:[^\n][\n]?)+) #clozecard ?\n*((?:\n(?:^.{1,3}$|^.{4}(?<!<!--).*))+)`
- 設定Folder table
	- 外：`國考考古題`
	- 內：`國考醫學知識`
- Defaults:
	- 打開： Add File link, Add Context, CurlyCloze, ID Comments

# 日常使用

## Flashcard
- 用 `#flashcard` 對應到基本型卡片

## ClozeCard格式

- 注意：`#clozecard`標籤後方一定要換行，下一行要有任何文字或符號，之後再空行分開段落
- 單純{}產生cloze，有幾個就幾張卡片
- 加上編號{1: } {2: }的話，同一編號的出現在同一張卡片
- 提示文字：加在雙冒號之後 {答案::提示}

### 範例

```
- 他住在{1:倫敦::城市名稱}的{1:貝克街::街道名稱}，興趣是{2:拉小提琴::樂器} #clozecard 
- Sherlock Holmes
```