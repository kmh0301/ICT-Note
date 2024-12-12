## 課程目標
本課程旨在使學生深入理解 SQL 中的 `GROUP BY` 語句及其在數據聚合中的應用，能夠熟練使用聚合函數進行數據分析。

## 課程大綱
1. SQL 聚合函數介紹
   - COUNT、SUM、AVG、MAX、MIN
2. `GROUP BY` 的基本用法
3. 結合 `HAVING` 子句進行過濾
4. 實作練習與案例分析

## 筆記內容

### 1. SQL 聚合函數介紹
聚合函數用於從多行數據中計算單一值，例如：
- **COUNT**：計算行數
- **SUM**：計算總和
- **AVG**：計算平均值
- **MAX**：找出最大值
- **MIN**：找出最小值

### 2. 使用 `GROUP BY` 的具體例子

#### 示例場景

假設我們有一個名為 `sales` 的表，結構如下：

| id | product   | category | amount |
|----|-----------|----------|--------|
| 1  | Laptop    | Electronics | 1200   |
| 2  | Smartphone | Electronics | 800    |
| 3  | Shirt     | Clothing  | 50     |
| 4  | Shoes     | Clothing  | 100    |
| 5  | TV        | Electronics | 600    |

#### 目標

我們想要計算每個類別的總銷售額。

#### SQL 查詢

```sql
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| category     | total_sales |
|--------------|-------------|
| Electronics   | 2600        |
| Clothing      | 150         |

#### 解釋

- **`SELECT category, SUM(amount) AS total_sales`**：選擇類別列和該類別的總銷售額。
- **`FROM sales`**：數據來源於 `sales` 表。
- **`GROUP BY category`**：按類別分組，使得每個類別的銷售額可以被單獨計算。

這個例子展示了如何使用 `GROUP BY` 對數據進行分組並進行聚合計算。

### 3. 結合 `HAVING` 子句進行過濾

假設我們希望只顯示銷售額超過 1000 的類別，我們可以使用 `HAVING` 子句：

#### SQL 查詢

```sql
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category
HAVING SUM(amount) > 1000;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| category     | total_sales |
|--------------|-------------|
| Electronics   | 2600        |

### 實作練習
1. 使用不同的聚合函數（如 COUNT 和 AVG）來分析其他數據表。
2. 嘗試使用 `HAVING` 子句過濾不同的聚合結果。

## 總結
本課程涵蓋了 SQL 中的聚合函數和 `GROUP BY` 的使用，學生應能運用所學進行基本的數據分組和聚合計算，並能夠利用 `HAVING` 子句進一步過濾結果。透過實作練習，學生將能夠熟悉 SQL 在數據分析中的應用。