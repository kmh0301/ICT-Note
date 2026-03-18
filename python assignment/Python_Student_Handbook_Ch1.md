# Python 程式設計基礎 (第一章) - 學生教學手冊

## Lesson 1: 基礎輸出與轉換 (print & int)

### 📚 教學重點 (Summary)
在 Python 中，指令是電腦執行的最小單位。
*   **print() 函數 (Function)**：這是最常用的指令，用於將訊息顯示在用家的螢幕上。
    *   **用法**：`print("Halo")`
    *   **運行結果**：螢幕上會出現 `Halo` 這幾個字。注意：文字必須用引號 `"` 括起來。
*   **變數 (Variable)**：想像變數是一個「盒子」，可以用來存放數據，並給這個盒子起一個名稱。
    - 例如：`age = 15`，這表示把數字 15 存進名為 `age` 的盒子裡。
*   **int() 函數**：電腦很死板，它認為 `"100"`（有引號）是文字，而 `100`（無引號）才是數字。`int()` 會把文字字串轉換成可以計算的 **整數 (Integer)**。
    - 例如：`int("100")` 會變成純數字 `100`。

> [!TIP]
> 如果你寫 `print("100" + "50")`，結果會是 `10050`；但如果你轉換成整數再計算，結果才是正確的 `150`。

### 🎯 任務描述 (Task)
1. 定義一個字串變數 `num_str = "100"`。
2. 使用 `int()` 將其轉換為整數並存入變數 `num`。
3. 計算 `num + 50` 的結果。
4. 使用 `print()` 顯示結果。

### 💻 程式碼模版 (Template)
```python
# 1. 定義字串
num_str = "100"

# 2. 將字串轉換為整數 (使用 int)


# 3. 計算 num + 50


# 4. 顯示結果 (使用 print)
```

### ✅ 參考答案 (Solution)
```python
num_str = "100"
num = int(num_str)
result = num + 50
print(result)
```

### ✍️ 額外挑戰 (Exercise)
**題目**: 定義一個字串變數 `price_str = "250"`，將其轉換為整數後，計算並顯示打折後的價格（即 `price_str` 減去 `50`）。

**挑戰答案**:
```python
price_str = "250"
price = int(price_str)
print(price - 50)
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 2: 獲取用戶輸入 (input)

### 📚 教學重點 (Summary)
為了讓程式有互動性，我們需要獲取用家的回饋。
*   **input() 函數**：當電腦執行到 `input()` 時會停下來，等待用家在鍵盤輸入內容並按下 Enter。
*   **輸入特性**：非常重要的一點——`input()` 接收到的內容永遠被視為 **字串 (String)**，即使你輸入的是數字。
    - 例如：用家輸入 `15`，Python 拿到的其實是 `"15"`。
*   **組合用法**：如果你想讓用家輸入一個數字拿來做加減乘除，你必須套用轉換函數。
    - **正確寫法**：`age = int(input())`

> [!WARNING]
> 常見錯誤：`age = input()` 之後接著寫 `print(age + 10)` 會導致程式崩潰，因為 Python 無法讓「文字」和「數字」相加。

### 🎯 任務描述 (Task)
編寫一個程式：
1. 讀取用家輸入的數字（代表目前的年齡）。
2. 計算並顯示 10 年後的年齡（即輸入加 10）。

### 💻 程式碼模版 (Template)
```python
# 1. 使用 input() 讀取用戶輸入，並使用 int() 轉換
age = 

# 2. 計算並顯示 10 年後的年齡
```

### ✅ 參考答案 (Solution)
```python
age = int(input())
print(age + 10)
```

### ✍️ 額外挑戰 (Exercise)
**題目**: 請用戶輸入兩個數字，程式會計算並顯示這兩個數字相加的結果。

**挑戰答案**:
```python
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 3: 數據類型 (Data Types)

### 📚 教學重點 (Summary)
電腦處理不同的數據時，會給予它們不同的標籤，這就是 **數據類型 (Data Types)**：
1.  **int (整數)**：任何沒有小數點的正數或負數。例如：`10`, `-500`。
2.  **float (浮點數)**：帶有小數點的數字。例如：`3.14`, `12.0`。
3.  **str (字串)**：任何用引號括起來的內容，無論是文字、數字還是空格。例如：`"Apple"`, `"123"`。
4.  **bool (布爾值)**：邏輯開關，只有兩個值：`True` (真) 和 `False` (假)。通常用於開關狀態或判斷題。
*   **type() 函數**：如果你不確定一個變數目前是什麼類型，你可以用 `print(type(變數))` 來查看。

### 🎯 任務描述 (Task)
依序檢查並顯示以下數值的類型：
1. `100`
2. `3.14`
3. `"Python"`
4. `True`

### 💻 程式碼模版 (Template)
```python
# 使用 print(type(數值)) 來顯示其數據類型
# 範例：print(type(50))
```

### ✅ 參考答案 (Solution)
```python
print(type(100))
print(type(3.14))
print(type("Python"))
print(type(True))
```

### ✍️ 額外挑戰 (Exercise)
**題目**: 定義一個變數 `x = "50.5"`。請問 `type(x)` 是什麼？如何將它轉換為可以運算的類型？

**挑戰答案**:
`type(x)` 是 `<class 'str'>`。應使用 `float(x)` 轉換為浮點數。

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 4: 算術運算符 (Arithmetic Operators)

### 📚 教學重點 (Summary)
Python 就像一個強大的計算機，可以使用 **運算符 (Operators)** 進行複雜運算：
*   `+` (加)、`-` (減)、`*` (乘)、`/` (除)
*   `%` (**取模 / 取餘數**)：這是很有用的符號。`7 % 3` 的結果是 `1`（因為 7 除以 3 餘 1）。常用來判斷單雙數。
*   `//` (**整除**)：只保留除法後的整數商。`7 // 3` 的結果是 `2`。
*   `**` (**指數 / 冪運算**)：計算幾次方。例如 `2 ** 3` 就是 $2^3 = 8$。平方根可以用 `** 0.5` 來表示。

### 🎯 任務描述 (Task)
輸入兩個整數 `a` 和 `b`，按順序計算並輸出：加、減、乘、除、餘數、整除、指數。

### ✅ 參考答案 (Solution)
```python
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)
```

---

## Lesson 5: 比較運算符 (Comparison Operators)

### 📚 教學重點 (Summary)
**比較運算符 (Comparison Operators)** 用於判斷兩個東西的關係，結果永遠是布爾值 (`True` 或 `False`)。
*   `>` (大於)、`<` (小於)
*   `>=` (大於或等於)、`<=` (小於或等於)
*   `==` (**等於**)：注意！在 Python 中，一個等於 `=` 是「賦值」（把東西存進盒子），兩個等於 `==` 才是「比較」兩邊是否一樣。
*   `!=` (**不等於**)：判斷兩邊是否不同。

### 🎯 任務描述 (Task)
輸入兩個整數 `a` 和 `b`，輸出所有比較運算的結果。

### ✅ 參考答案 (Solution)
```python
a = int(input())
b = int(input())

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 6: if 語句 (單一條件)

### 📚 教學重點 (Summary)
**if 語句 (Conditional Statement)** 讓程式具備思考能力，只有當滿足某個條件時，電腦才會執行特定的動作。
*   **結構**：
    ```python
    if 條件式:
        # 滿足條件後要執行的內容 (必須縮進)
    ```
*   **冒號 (:)**：條件式的最後必須加上冒號，表示「如果...的話，就做下面的事」。
*   **縮進 (Indentation)**：當你按下冒號並 Enter，程式碼會自動往右移動（縮進）。縮進的程式碼就像是屬於 `if` 指令的「合約內容」，沒縮進的則不歸 `if` 管。

> [!IMPORTANT]
> 如果沒有正確對齊（縮進），Python 會報錯，這是新手最常遇到的問題！

### 🎯 任務描述 (Task)
設定 `mark = 50`。如果 `mark` 大於或等於 50，顯示 "Pass"。

### ✅ 參考答案 (Solution)
```python
mark = 50
if mark >= 50:
    print("Pass")
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 7: if...else 語句 (二選一)

### 📚 教學重點 (Summary)
生活中有許多情況是二選一的。當 `if` 的條件不成立時，我們需要一個「後備方案」，這就是 **else 指令**。
*   **邏輯**：如果 (if) 天氣好，就出去玩；否則 (else)，就留在家。
*   **用法**：`else` 永遠跟在 `if` 區塊的最後，它不需要再寫任何條件，因為它是負責處理「所有剩餘的情況」。

### 🎯 任務描述 (Task)
輸入一個分數 `mark`：
- 如果 `mark >= 50`，顯示 "Pass."。
- 否則，顯示 "Fail."。

### ✅ 參考答案 (Solution)
```python
mark = int(input())
if mark >= 50:
    print("Pass.")
else:
    print("Fail.")
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Lesson 8: if...elif...else 語句 (多重條件)

### 📚 教學重點 (Summary)
當你有三個或更多選項時，就要用到 **elif (Else If 的縮寫)**。
*   **執行流程**：電腦會從第一行 `if` 開始看，如果符合就執行並直接離開整組 `if`；如果不符，就看下一個 `elif`。如果全部 `if` 和 `elif` 都不符合，最後才會輪到 `else`。
*   **好處**：比起寫很多個獨立的 `if`，使用 `elif` 的效能更高，且能確保多個選項中只有「其中一個」會被執行。

### 🎯 任務描述 (Task)
輸入分數 `mark`：
1. `mark >= 80`: 顯示 "Credit."
2. `mark >= 50`: 顯示 "Pass."
3. 否則: 顯示 "Fail."

### ✅ 參考答案 (Solution)
```python
mark = float(input())
if mark >= 80:
    print("Credit.")
elif mark >= 50:
    print("Pass.")
else:
    print("Fail.")
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
# 綜合專案 (Integrated Projects)

## Project 1: BMI 判斷器

**任務要求**:
1. 請用戶輸入體重 (kg) 和身高 (m)。
2. 計算 BMI = `weight / (height**2)`。
3. 輸出 BMI 值（保留 3 位有效數字，例如使用 `f"{BMI:.3g}"`）。
4. 判斷身體狀況：
   - BMI >= 24: "FAT"
   - BMI <= 20: "THIN"
   - 否則: "FIT"

**參考答案**:
```python
print("Please input your weight(kg):")
weight = float(input())
print("Please input your height(m):")
height = float(input())

BMI = weight / (height ** 2)

print(f"Your BMI is: {BMI:.3g}")

if BMI >= 24:
    print("FAT")
elif BMI <= 20:
    print("THIN")
else:
    print("FIT")
```

---
<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>
## Project 2: 一元二次方程求根計算器

**任務要求**:
1. 輸入方程 ax^2 + bx + c = 0 的係數 `a`, `b`, `c`。
2. 計算判別式 Delta = b^2 - 4ac。
3. 使用 `** 0.5` 計算平方根。
4. 根據 Delta 的值，輸出方程的根。

**參考答案**:
```python
#print("Please input a:")
a = float(input())
print("Please input b:")
b = float(input())
print("Please input c:")
c = float(input())

# 在下方編寫判別式計算與 if 判斷邏輯
Delta = b**2-4*a*c
# 提示：使用 ** 0.5 來計算平方根
x1 = (-b+(Delta)**0.5)/2*a
x2 = (-b-(Delta)**0.5)/2*a

if (Delta > 0):
    print('Two real roots: ' +str(x1)+' and '+str(x2))
elif (Delta == 0 ):
    print('One real root: ' +str(x1))
else : 
    print("No real roots")
```
