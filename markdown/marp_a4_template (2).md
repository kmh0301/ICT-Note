---
marp: false
theme: a4-template
paginate: true
size: A4
---

<style>
/* A4 Template Theme */
section {
  width: 210mm;
  height: 297mm;
  padding: 20mm;
  font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', system-ui, sans-serif;
  font-size: 16pt;
  line-height: 1.5;
  color: #1a1a1a;
  background: white;
  box-sizing: border-box;
}

/* Page Header */
section::before {
  content: 'heading';
  position: absolute;
  top: 10mm;
  right: 20mm;
  font-size: 14pt;
  color: #999;
  font-weight: normal;
}

/* Name and Date Fields */
.name-date-fields {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px 0 30px 0;
  font-size: 14pt;
  color: #1a1a1a;
}

.name-field, .date-field {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #1a1a1a;
}

.field-line {
  border-bottom: 1px solid #1a1a1a;
  min-width: 150px;
  height: 20px;
  display: inline-block;
}

.checkbox {
  width: 15px;
  height: 15px;
  border: 1px solid #1a1a1a;
  display: inline-block;
  margin-left: 5px;
}

/* Page Footer */
section::after {
  content: 'footer';
  position: absolute;
  bottom: 15mm;
  left: 20mm;
  right: 20mm;
  padding: 8px 15px;
  background: #f5e6a3;
  border-left: 4px solid #d4af37;
  font-size: 14pt;
  color: #1a1a1a;
}

/* Main Heading H1 */
h1 {
  background: #8b5a9f;
  color: white;
  padding: 12px 20px;
  margin: 0 -20px 20px -20px;
  font-size: 12pt;
  font-weight: bold;
  border: none;
}

/* Secondary Heading H2 */
h2 {
  color: #8b5a9f;
  font-size: 12pt;
  font-weight: normal;
  margin: 20px 0 15px 0;
  padding: 0;
}

/* Tertiary Heading H3 */
h3 {
  background: #a67bb0;
  color: white;
  padding: 10px 20px;
  margin: 15px -20px 15px -20px;
  font-size: 12pt;
  font-weight: bold;
}

/* Quaternary Heading H4 */
h4 {
  color: #999;
  font-size: 12pt;
  font-weight: normal;
  margin: 15px 0 10px 0;
  padding: 8px 0;
  border-top: 1px dotted #ccc;
  border-bottom: 1px dotted #ccc;
}

/* Unordered Lists */
ul {
  margin: 15px 0;
  padding-left: 20px;
}

ul li {
  margin: 8px 0;
  list-style-type: disc;
  color: #1a1a1a;
}

ul li::marker {
  color: #8b5a9f;
  font-size: 18pt;
}

/* Ordered Lists */
ol {
  margin: 15px 0;
  padding-left: 25px;
}

ol li {
  margin: 8px 0;
  color: #1a1a1a;
}

ol li::marker {
  color: #8b5a9f;
  font-weight: bold;
}

/* Remarks/Special Content */
.remark {
  border: 2px dashed #a67bb0;
  padding: 15px;
  margin: 20px 0;
  color: #a67bb0;
  font-style: italic;
  text-align: center;
  background: #f8f5ff;
}

/* Paragraph styling */
p {
  margin: 10px 0;
  text-align: justify;
}

/* Code blocks */
pre {
  background: #f5f5f5;
  border-left: 4px solid #8b5a9f;
  padding: 15px;
  margin: 15px 0;
  font-family: 'Courier New', monospace;
  overflow-x: auto;
}

/* Inline code */
code {
  background: #f0f0f0;
  padding: 2px 4px;
  font-family: 'Courier New', monospace;
  font-size: 14pt;
}

/* Tables */
table {
  border-collapse: collapse;
  width: 100%;
  margin: 15px 0;
}

th {
  background: #8b5a9f;
  color: white;
  padding: 10px;
  text-align: left;
  border-bottom: 2px solid #333;
}

td {
  padding: 8px 10px;
  border-bottom: 1px solid #ddd;
}

tr:nth-child(even) {
  background: #f9f9f9;
}

/* Blockquotes */
blockquote {
  border-left: 4px solid #8b5a9f;
  padding-left: 20px;
  margin: 15px 0;
  font-style: italic;
  color: #666;
}

/* Strong and emphasis */
strong {
  color: #8b5a9f;
  font-weight: bold;
}

em {
  color: #8b5a9f;
  font-style: italic;
}
</style>

<!-- Slide 1 -->
# H1

<div class="name-date-fields">
  <div class="name-field">
    Name: <span class="field-line"></span><span class="checkbox"></span>
  </div>
  <div class="date-field">
    Date: <span class="field-line"></span>
  </div>
</div>

## H2

### H3

#### H4

- ul
1. ol

<div class="remark">remark</div>

---

<!-- Slide 2 -->
# Sample Content

## Introduction

This is a sample paragraph to demonstrate the A4 template styling. The text is justified and uses a clean, professional font.

### Key Features

- Professional A4 layout
- Purple color scheme for headings
- Clean typography and spacing
- Footer with yellow background

#### Additional Details

1. Numbered lists are also styled
2. With purple markers
3. And proper spacing

<div class="remark">This is a special remark box for important notes</div>

---

<!-- Slide 3 -->
# Advanced Elements

## Code Examples

Here's some inline `code` and a code block:

```javascript
function hello() {
    console.log("Hello World!");
}
```

### Tables

| Feature | Status | Priority |
|---------|--------|----------|
| Headers | ✓ Done | High |
| Footer | ✓ Done | High |
| Lists | ✓ Done | Medium |

> This is a blockquote for important information or citations.

**Bold text** and *italic text* are styled with the theme colors.
