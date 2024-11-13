---
up: 
- "[[2.1 數據分級]]"
相關試題:
- "[[2019P1Q3]]"
- "[[2020P1Q10]]"
- "[[2021P1Q13]]"
- "[[2022P1Q10]]"
tags: 
課本: 
課題重要性: 
DSE出現頻率:
---
<!-- theme: uncover -->
<style>
  :root {
    --color-background: #fffbf0; /* Soft cream background */
    --color-background-code: #ffe4b5; /* Light peach for code blocks */
    --color-background-paginate: rgba(255, 228, 196, 0.1); /* Light peach pagination */
    --color-foreground: #345; /* Dark slate for text */
    --color-highlight: #6184D8; 
    --color-highlight-heading: #315DC4; 
    --color-header: #ffb6c1; /* Light pink for headers */
    --color-header-shadow: rgba(0, 0, 0, 0.1); /* Subtle shadow */
  }

  h2 {
    text-align: left; /* Align H2 to the left */
    color: var(--color-highlight-heading);
    font-size: 2em;
    margin-top: 1em;
    margin-bottom: 0.5em;
    padding-bottom: 0.2em;
  }
  
  h3 {
    text-align: left; /* Align H2 to the left */
    color: var(--color-highlight-heading);
    font-size: 2em;
    padding-bottom: 0.2em;
  }
  p {
    margin-bottom: 1em;
  }
  ul, ol 
	{ text-align: left; /* Ensure lists are left-aligned */ 
	  margin-left: 20px; /* Indent lists for visual clarity */ 
	}
</style>


# 內容
---
## 1. 公式
---
### 1. 常數
![[Pasted image 20241111111834.png]]

---
### 2. 運算符
--- 
1. 算術運算符
 ![[Pasted image 20241111112003.png]]
---
2. 比較運算符
比較運算符可以比較數字，字串（但不可以比較字串的大小階）和布爾值
![[Pasted image 20241111112657.png]]

---
3. 文字串連運算符
![[Pasted image 20241111120904.png]]

---
4. 儲存格參照
儲存格參照可以根據儲存格位址以識別單一或一組儲存格
- 外部參照
![[Pasted image 20241111121751.png]]
---
- 參照運算符
![[Pasted image 20241111121736.png]]
---

## 2. 函數

---
### 數學函數
重點函數(Dse 試卷中附件有印)
- sum()
- sumif()
- ABS()
- INT()
- RAND()
- SQRT()
---

![[Pasted image 20241111122442.png]]

---
### 數學函數
函數(Dse 試卷中附件沒有印)
- Round()
- Rounddown()
- Roundup()
- Randbetween()
- Power()

---
![[Pasted image 20241111134513.png]]

---
### 邏輯函數
重點函數(Dse 試卷中附件有印)
- AND（ ）
- NOT（ ）
- OR ( )
- IF ( )
---
![[Pasted image 20241111134722.png]]

---
### 文字函數
重點函數(Dse 試卷中附件有印)
- CHAR( ) 
- TEXT( )
---
![[Pasted image 20241111143831.png]]


---
重點函數(Dse 試卷中附件有印)
- VALUE( ) 
- CONCATENATE( )
- LEN( )
- LEFT( )
- MID( )
- RIGHT( )

---
![[Pasted image 20241111145145.png]]

---
重點函數(Dse 試卷中附件有印)
- LOWER( )
- UPPER( )
- PROPER( )
- TRIM( )
- FIND( ) 
--- 
![[Pasted image 20241111145414.png]]
![[Pasted image 20241111144723.png]]

--- 
函數(Dse 試卷中附件沒有印)
- EXACT ( )
- CODE ( )
- REPLACE ( )
- SEARCH ( )
- SUBSTITUTE ( )

---

![[Pasted image 20241111145845.png]]

--- 
### 資訊函數
重點函數(Dse 試卷中附件有印)
- ISBLANK()
![[Pasted image 20241111150117.png]]

--- 
函數(Dse 試卷中附件沒有印)
![[Pasted image 20241111150145.png]]

--- 

### 統計函數
重點函數(Dse 試卷中附件有印)
- AVERAGE( )
- COUNT( )
- COUNTA( )
- COUNTBLANK( )
- COUNTIF( )
- MAX( )
- MIN( )
- RANK.EQ( )/ RANK( )

--- 
![[Pasted image 20241111150637.png]]

---
![[Pasted image 20241111151039.png]]

--- 
函數(Dse 試卷中附件沒有印)
- MEDIAN ( )
- MODE ( )/ MODE.SNGL( )
- LARGE( )
- SMALL( )
- RANK.AVG( )

--- 
![[Pasted image 20241111151156.png]]

---
### 查閱函數
重點函數(Dse 試卷中附件有印)
- VLOOKUP( )
 ![[Pasted image 20241111151547.png]]

--- 
函數(Dse 試卷中附件沒有印)
- HLOOKUP( )
![[Pasted image 20241111151604.png]]

---
