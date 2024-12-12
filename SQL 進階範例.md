
以下是一些 SQL 查詢的進階範例，涵蓋了不同的情境和用法，包括 `ORDER BY` 和 `GROUP BY` 的多種應用。

### 1. 使用 ORDER BY 排序

#### 示例場景

假設我們有一個名為 `students` 的表，結構如下：

| id | name    | age | score |
|----|---------|-----|-------|
| 1  | Alice   | 22  | 85    |
| 2  | Bob     | 21  | 90    |
| 3  | Charlie  | 23  | 78    |
| 4  | David   | 20  | 92    |
| 5  | Eva     | 22  | 88    |

#### 按分數排序

我們希望按照學生的分數從高到低排序。

#### SQL 查詢

```sql
SELECT name, score FROM students ORDER BY score DESC;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| name    | score |
|---------|-------|
| David   | 92    |
| Bob     | 90    |
| Eva     | 88    |
| Alice   | 85    |
| Charlie | 78    |

#### 按年齡和分數排序

如果我們希望首先按年齡排序，然後按分數排序（年齡相同的情況下）。

#### SQL 查詢

```sql
SELECT name, age, score FROM students ORDER BY age ASC, score DESC;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| name    | age | score |
|---------|-----|-------|
| David   | 20  | 92    |
| Bob     | 21  | 90    |
| Alice   | 22  | 85    |
| Eva     | 22  | 88    |
| Charlie | 23  | 78    |

### 2. 使用 GROUP BY 和 HAVING 子句

#### 示例場景

假設我們有一個名為 `orders` 的表，結構如下：

| id | customer_id | amount |
|----|-------------|--------|
| 1  | A           | 100    |
| 2  | B           | 200    |
| 3  | A           | 150    |
| 4  | C           | 300    |
| 5  | B           | 250    |

#### 計算每位客戶的總訂單金額

我們想要計算每位客戶的總訂單金額。

#### SQL 查詢

```sql
SELECT customer_id, SUM(amount) AS total_amount 
FROM orders 
GROUP BY customer_id;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| customer_id | total_amount |
|-------------|--------------|
| A           | 250          |
| B           | 450          |
| C           | 300          |

#### 過濾總訂單金額超過 $300 的客戶

如果我們只想顯示總訂單金額超過 $300 的客戶。

#### SQL 查詢

```sql
SELECT customer_id, SUM(amount) AS total_amount 
FROM orders 
GROUP BY customer_id 
HAVING SUM(amount) > 300;
```

#### 查詢結果

執行上述查詢後，結果將如下所示：

| customer_id | total_amount |
|-------------|--------------|
| B           | 450          |
| C           | 300          |

### 總結
這些範例展示了如何使用 SQL 中的 `ORDER BY` 和 `GROUP BY` 子句來對數據進行排序和分組。透過這些查詢，學生可以更好地理解如何在實際應用中運用 SQL 語言進行數據分析和管理。學生應能夠運用這些技巧來解決各種數據查詢問題。