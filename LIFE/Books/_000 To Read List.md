```dataview 
Table without id  ("![|100](" + cover + ")") as Cover, author as Author, title as Title, pages as "Pages", category as Genre From "LIFE/Books" Where contains(status, "to read") sort author asc, title asc
```