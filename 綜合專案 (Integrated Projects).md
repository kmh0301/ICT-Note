<div style="page-break-after: always; visibility: hidden">

\pagebreak

</div>
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