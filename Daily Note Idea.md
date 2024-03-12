```dataview
TASK FROM "01-Journal" 
WHERE !completed AND !checked 
SORT file.name asc
```
## On This Day...

```dataview
LIST 
FROM "01-Journal/01-Daily"
WHERE dateformat(file.day, "MM-dd") = dateformat(this.file.day, "MM-dd")
AND file.day != this.file.day
```

```dataview
LIST 
FROM "01-Journal/01-Daily"
WHERE dateformat(file.day, "MM-dd") = dateformat(this.file.day, "MM-dd")
and file.day != this.file.day
```

> [!note]+ On This Day
>  ```dataview
> List 
>  From "01-Journal/01-Daily"
> Where file.ctime >= date(<% today %>) AND file.ctime <= date(<% tomorrow %>)
>  ```

Prueba
```dataview
LIST
FROM "01-Journal/01-Daily"
WHERE dateformat(file.day, "MM-dd") = dateformat(this.file.day, "MM-dd")
```



---

## Notes Created Today

```dataview
TABLE created, updated as modified, tags, type, status
FROM "" AND !"01-Journal" AND !"Templates"
WHERE contains(dateformat(file.ctime, "yyyy-MM-dd"), dateformat(this.file.day, "yyyy-MM-dd"))
```

---

## Highlights For Today

```dataview
TABLE highlights
FROM "01-Journal/01-Daily"
WHERE this.file.name = file.name
AND highlights != null
```

---


## Las Updated
```dataview
TABLE dateformat(updated, "yyyy-MM-dd - HH:mm") AS "Last modified"
FROM ""
SORT updated DESC
LIMIT 25
```

## Created on this day years ago

```dataview
TABLE dateformat(journal-start-date, "yyyy-MM-dd") AS "Created"
FROM "01-Journal/01-Daily"
WHERE journal-start-date = date(today) - dur(12 months) OR
journal-start-date = date(today) - dur(24 months) OR
journal-start-date = date(today) - dur(36 months) OR
journal-start-date = date(today) - dur(48 months)
SORT journal-start-date DESC
```

WHERE journal-start-date AND journal-start-date <= date(today) - dur(6 months) AND journal-start-date >= date(today) - dur(6 months 7 days)

```dataview 
TABLE file.ctime AS "created" 
FROM "" 
WHERE file.cday.year = this.file.cday.year -1 AND 
file.cday.month = this.file.cday.month AND 
file.cday.day = this.file.cday.day
```