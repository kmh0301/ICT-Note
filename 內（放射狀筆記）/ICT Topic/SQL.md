# SQL 學習筆記

## 什麼是 SQL？
SQL（結構化查詢語言）是一種用於管理關聯數據庫的語言，能夠用來查詢、插入、更新和刪除數據。

## 基本概念

### 數據庫（Database）
數據庫是一個有組織的數據集合，通常由多個表（Table）組成。

### 表（Table）
表是數據庫中存儲數據的基本單位，每個表由行（Row）和列（Column）構成。

### 行（Row）
每一行代表一條記錄（Record）。

### 列（Column）
每一列代表一個字段（Field），定義了數據的屬性。

## 基本 SQL 命令

### 1. 查詢數據：`SELECT`
```sql
SELECT column1, column2 FROM table_name;
```
例如：
```sql
SELECT name, age FROM users;
```

### 2. 插入數據：`INSERT`
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```
例如：
```sql
INSERT INTO users (name, age) VALUES ('小明', 30);
```

### 3. 更新數據：`UPDATE`
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```
例如：
```sql
UPDATE users SET age = 31 WHERE name = '小明';
```

### 4. 刪除數據：`DELETE`
```sql
DELETE FROM table_name WHERE condition;
```
例如：
```sql
DELETE FROM users WHERE name = '小明';
```

## 進階查詢

### 1. 條件查詢：`WHERE`
用來過濾查詢結果。
```sql
SELECT * FROM users WHERE age > 25;
```

### 2. 排序：`ORDER BY`
用來對查詢結果進行排序。
```sql
SELECT * FROM users ORDER BY age DESC;
```

### 3. 分組：`GROUP BY`
用來對結果進行分組。
```sql
SELECT age, COUNT(*) FROM users GROUP BY age;
```

### 4. 連接多個表：`JOIN`
用來從多個表中查詢數據。
```sql
SELECT users.name, orders.amount 
FROM users 
JOIN orders ON users.id = orders.user_id;
```

