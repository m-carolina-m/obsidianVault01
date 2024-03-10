- **Monday** [[<% tp.date.weekday("YYYY-MM-DD", 1) %>]]

- **Tuesday** [[ <% tp.date.weekday("YYYY-MM-DD", 2) %>]]

- **Wednesday** [[<% tp.date.weekday("YYYY-MM-DD", 3) %>]]

- **Thursday** [[<% tp.date.weekday("YYYY-MM-DD", 4) %>]]

- **Friday** [[<% tp.date.weekday("YYYY-MM-DD", 5) %>]]

- **Saturday** [[<% tp.date.weekday("YYYY-MM-DD", 6) %>]]

- **Sunday** [[<% tp.date.weekday("YYYY-MM-DD", 7) %>]]


## From file title

- **Monday** [[<% tp.date.weekday("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]

- **Tuesday** [[<% tp.date.weekday("YYYY-MM-DD", 2, tp.file.title, "YYYY-MM-DD") %>]]

- **Wednesday** [[<% tp.date.weekday("YYYY-MM-DD", 3, tp.file.title, "YYYY-MM-DD") %>]]

- **Thursday** [[<% tp.date.weekday("YYYY-MM-DD", 4, tp.file.title, "YYYY-MM-DD") %>]]

- **Friday** [[<% tp.date.weekday("YYYY-MM-DD", 5, tp.file.title, "YYYY-MM-DD") %>]]

- **Saturday** [[<% tp.date.weekday("YYYY-MM-DD", 6, tp.file.title, "YYYY-MM-DD") %>]]

- **Sunday** [[<% tp.date.weekday("YYYY-MM-DD", 7, tp.file.title, "YYYY-MM-DD") %>]]

## Week year

```dataview 
TABLE Do_Time AS "Time", Do_Date AS "Do", Due_Date AS "Due" 
FROM "01-Journal/01-Daily"
WHERE date(Due_Date).weekyear = date(this.file.name).weekyear OR date(Do_Date).weekyear = date(this.file.link).weekyear 
SORT Do_Time ASC 
```


## 

```dataview
TABLE fileWeek 
FROM "01-Journal/01-Daily" 
FLATTEN dateformat( date( regexreplace( file.name, "^(\d{2})(\d{2})(\d{2}).*", "20$1-$2-$3" ) ), "WW" ) as fileWeek 
WHERE fileWeek = dateformat( date(now), "WW" )
```

```dataview 
TABLE WITHOUT ID title, textDate, dateformat(date(textDate), "WW") 
FLATTEN list( "230301 - Daily Note", "230302 - Daily Note", "230321 - Daily Note", "230322 - Daily Note" ) as title 
FLATTEN regexreplace(title, "^(\d{2})(\d{2})(\d{2}).*", "20$1-$2-$3") as textDate WHERE file.folder = this.file.folder AND 
file.name = this.file.name 
```


```dataview 
table without id duration, date(2023-01-02) + dur(duration) as "Date after start" where file.name = this.file.name 
```

weeknumber:: {{date:w}}

weeknumber:: {{date:W}}

<% tp.date.weekday("DD.MM ddd", 0, tp.file.title, "YYYY-[W]ww") %>

year
<% tp.file.title.slice(0,4) %> 

month
<% tp.file.title.slice(6,8) %>