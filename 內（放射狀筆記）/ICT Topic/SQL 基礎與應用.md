---
相關概念:
  - "[[SQL 數據聚合與分組]]"
  - "[[SQL 進階範例]]"
---
## 筆記內容

### 1. SQL 的定義與用途
SQL（結構化查詢語言）是一種用於管理關係型數據庫的標準語言。它允許用戶執行數據查詢、插入、更新和刪除等操作。

### 2. 數據庫的基本概念
數據庫是以結構化方式存儲和管理數據的系統。關係型數據庫使用表格來表示數據，表格由行和列組成。

### 3. 基本查詢

#### 示例場景

假設我們有一個名為 `products` 的表，結構如下：

| id | name        | category | price |
|----|-------------|----------|-------|
| 1  | Laptop      | Electronics | 1200  |
| 2  | Smartphone   | Electronics | 800   |
| 3  | T-shirt     | Clothing  | 20    |
| 4  | Jeans       | Clothing  | 40    |
| 5  | Headphones  | Electronics | 150   |

#### 基本查詢目標

我們想要查詢所有產品的名稱和價格。

#### SQL 查詢

```sql
SELECT name, price FROM products;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| name        | price |
|-------------|-------|
| Laptop      | 1200  |
| Smartphone   | 800   |
| T-shirt     | 20    |
| Jeans       | 40    |
| Headphones  | 150   |

### 4. 使用 WHERE 子句的範例

#### 示例場景

如果我們只想查詢價格高於 $100 的產品。

#### SQL 查詢

```sql
SELECT name, price FROM products WHERE price > 100;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| name        | price |
|-------------|-------|
| Laptop      | 1200  |
| Smartphone   | 800   |
| Headphones  | 150   |

### 5. 數據排序：使用 ORDER BY 子句

#### 示例場景

如果我們希望按照價格對產品進行排序。

#### SQL 查詢

```sql
SELECT name, price FROM products ORDER BY price DESC;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| name        | price |
|-------------|-------|
| Laptop      | 1200  |
| Smartphone   | 800   |
| Headphones  | 150   |
| Jeans       | 40    |
| T-shirt     | 20    |

### 6. 數據分組：使用 GROUP BY 子句的具體例子

#### 示例場景

假設我們有一個名為 `sales` 的表，結構如下：

| id | product_id | quantity |
|----|------------|----------|
| 1  | 1          | 10       |
| 2  | 2          | 20       |
| 3  | 1          | 5        |
| 4  | 3          | 15       |

#### 計算每個產品的總銷售量目標

我們想要計算每個產品的總銷售量。

#### SQL 查詢

```sql
SELECT product_id, SUM(quantity) AS total_quantity 
FROM sales 
GROUP BY product_id;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| product_id | total_quantity |
|------------|----------------|
| 1          | 15             |
| 2          | 20             |
| 3          | 15             |

### 解釋

- **`SELECT product_id, SUM(quantity) AS total_quantity`**：選擇產品 ID 和該產品的總銷售量。
- **`FROM sales`**：數據來源於 `sales` 表。
- **`GROUP BY product_id`**：按產品 ID 分組，使得每個產品的銷售量可以被單獨計算。

### 數據更新與刪除

#### 使用 UPDATE 語句範例

如果我們需要更新某個產品的價格，例如將 `T-shirt` 的價格改為 $25：

```sql
UPDATE products SET price = 25 WHERE name = 'T-shirt';
```

#### 使用 DELETE 語句範例

如果我們需要刪除某個產品，例如刪除 `Jeans`：

```sql
DELETE FROM products WHERE name = 'Jeans';
```

## 總結
本課程涵蓋了 SQL 的基本知識，包括數據庫結構、基本查詢、數據排序與分組、以及數據更新和刪除操作。學生應能運用所學進行基本的數據操作，並理解 SQL 在數據管理中的重要性。透過實作練習，學生將能夠熟悉 SQL 的語法及其在實際應用中的重要性。

Citations:
[1] https://www.w3school.com.cn/sql/sql_groupby.asp
[2] https://liaoxuefeng.com/books/sql/manipulation/delete/index.html
[3] https://www.runoob.com/mysql/mysql-group-by-statement.html
[4] https://www.w3school.com.cn/sql/sql_delete.asp
[5] https://www.fooish.com/sql/group-by.html
[6] https://www.runoob.com/sql/sql-groupby.html