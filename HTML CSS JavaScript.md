---
相關概念:
  - "[[PHP]]"
---

# 網頁基本構件
	1. HTML 網頁結構
	2. CSS 網頁美觀
	3. JavaScript 網頁動態程式

## HTML 基礎

### 1. HTML 的定義與用途
HTML（超文本標記語言）是用於創建網頁的標準標記語言。它使用標籤來結構化網頁內容。

### 2. 基本結構
每個 HTML 文件都應包含以下基本結構：

```html
<!DOCTYPE html>
<html>
<head>
    <title>我的第一個網頁</title>
</head>
<body>
    <h1>歡迎來到我的網站</h1>
    <p>這是一段簡單的介紹文字。</p>
</body>
</html>
```

### 3. 常用標籤
- `<h1>` 到 `<h6>`：標題標籤，表示不同層級的標題。
- `<p>`：段落標籤，用於文本內容。
- `<a>`：超鏈接標籤，用於創建鏈接。
- `<img>`：圖像標籤，用於插入圖片。                                                                                                         

### 示例
```html
<h1>歡迎來到我的網站</h1>
<p>這是一段簡單的介紹文字。</p>
<a href="https://www.example.com">訪問範例網站</a>
<img src="image.jpg" alt="描述圖片">
```


### 4. 列表

#### 無序列表
無序列表用於列出不需要特定順序的項目。

```html
<ul>
    <li>項目一</li>
    <li>項目二</li>
    <li>項目三</li>
</ul>
```

#### 有序列表
有序列表用於列出需要特定順序的項目。

```html
<ol>
    <li>第一項</li>
    <li>第二項</li>
    <li>第三項</li>
</ol>
```

### 5. 表格

#### 示例場景
假設我們有一個學生信息表，結構如下：

```html
<table>
    <tr>
        <th>姓名</th>
        <th>年齡</th>
        <th>城市</th>
    </tr>
    <tr>
        <td>小明</td>
        <td>25</td>
        <td>台北</td>
    </tr>
    <tr>
        <td>小華</td>
        <td>30</td>
        <td>高雄</td>
    </tr>
    <tr>
        <td>小美</td>
        <td>28</td>
        <td>台中</td>
    </tr>
</table>
```

### 6. 文本格式化

#### 粗體、斜體和下劃線
使用以下標籤來格式化文本：

```html
<p><b>這是一段粗體文字。</b></p>
<p><i>這是一段斜體文字。</i></p>
<p><u>這是一段下劃線文字。</u></p>

<p>這是普通文本，其中包含上標<sup>上標文字</sup>和下標<sub>下標文字</sub>.</p>
```
<p><b>這是一段粗體文字。</b></p>
<p><i>這是一段斜體文字。</i></p>
<p><u>這是一段下劃線文字。</u></p>

<p>這是普通文本，其中包含上標<sup>上標文字</sup>和下標<sub>下標文字</sub>.</p>
### 7. 超鏈接

#### 示例場景
您可以使用 `<a>` 標籤創建超鏈接：

```html
<p>訪問<a href="https://www.example.com" target="_blank">範例網站</a></p>
```
<p>訪問<a href="https://www.youtube.com" target="_blank">範例網站</a></p>
### 8. 內嵌框架

#### 示例場景
使用 `<iframe>` 標籤嵌入其他內容，例如 YouTube 視頻：

```html
<iframe width="560" height="315" src="https://youtu.be/CLUPkcLQm64?feature=shared" frameborder="0" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/CLUPkcLQm64?si=bnlfCdqGjOfgB9SF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> From youtube 
```
<iframe width="560" height="315" src="https://www.youtube.com/embed/CLUPkcLQm64?si=bnlfCdqGjOfgB9SF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="900" height="900" src=
"https://codepen.io/Sau-Yung-Pang/pen/ogvzrJw" ></iframe>


## 筆記 2: CSS 基礎

### 1. CSS 的定義與用途
CSS（層疊樣式表）用於控制網頁的外觀和佈局。它可以改變顏色、字體、間距等樣式。

### 2. CSS 的基本語法
CSS 使用選擇器和聲明塊來應用樣式：

```css
selector {
    property: value;
}
```

### 3. 常用屬性
- `color`：文本顏色。
- `background-color`：背景顏色。
- `font-size`：字體大小。
- `margin` 和 `p---adding`：外邊距和內邊距。

### 示例
```css
body {
    background-color: #f4f4f4;
}

h1 {
    color: blue;
    font-size: 24px;
}

p {
    margin: 20px;
}
```

### 在 HTML 中使用 CSS
可以在 `<head>` 中使用 `<style>` 標籤或鏈接外部 CSS 文件：

```html
<link rel="stylesheet" href="styles.css">
```

---

## 筆記 3: JavaScript 基礎

### 1. JavaScript 的定義與用途
JavaScript 是一種高級編程語言，主要用於為網頁添加互動性和動態效果。

### 2. 基本語法
JavaScript 使用變量、函數和事件來執行操作：

```javascript
// 定義變量
let message = "Hello, World!";

// 定義函數
function greet() {
    alert(message);
}

// 調用函數
greet();
```

### 3. 常用功能
- **DOM 操作**：可以通過 JavaScript 操作 HTML 元素。
- **事件處理**：可以為元素添加事件監聽器。

### 示例：改變文本內容
```html
<p id="demo">這是一段文字。</p>
<button onclick="changeText()">點擊我</button>

<script>
function changeText() {
    document.getElementById("demo").innerHTML = "文本已更改！";
}
</script>                      
```

---

這三個筆記涵蓋了 HTML、CSS 和 JavaScript 的基本概念及示例，幫助您快. 入門前端開發。希望這些內容對您有幫助！如果您需要更詳細的解釋或其他主題，請隨時告訴我！