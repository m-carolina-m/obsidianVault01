---
type: daily
date: # <% moment(tp.file.title,'YYYY-MM-DD').format("MM, DD, YYYY") %>
---

# <% moment(tp.file.title,'YYYY-MM-DD').format('dddd, MMMM DD, YYYY') %>

<< [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').subtract(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Yesterday]] \| [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').add(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Tomorrow]] >>


 ## [!danger]+ Overdue 
```tasks
 not done
 (due before {{date:YYYY-MM-DD}}) OR ((happens before {{date:YYYY-MM-DD}}) sort by due date
```

## Due today:
```dataviewjs
dv.taskList(dv.pages().file.tasks
.where(t=>t.text.includes("{{date:YYYY-MM-DD}}")))
```

```
TASK FROM "" WHERE !completed AND due GROUP BY choice(due < date(today), "🚩 overdue", "🟢 in time") AS abc
```

## [!tip]- Coming Soon (next 3 days)
```tasks
not done
happens after {{date:YYYY-MM-DD}}
happens before {{date+3d:YYYY-MM-DD}}
hide recurrence rule
hide due date
hide scheduled date
group by happens
```

## Someday  
```tasks  
not done  
no due date  
((path includes Task List) OR (path includes Entry)) AND (path does not include Travel)  
filter by function task.status.symbol === ' '  
```


## Completed today



## EXPENSES:


## 

### 📅 Daily Questions

##### 🌜 Last night, after work, I...


##### 🙌 One thing I'm excited about right now is...


##### 🚀 One+ thing I plan to accomplish today is...

##### 👎 One thing I'm struggling with today is...

# 📝 Notes
<% tp.file.cursor() %>



## 5 Minute Journal

### FIRST LIGHT
3 things I am grateful for...
1.

What will i do to make today great?

Daily affirmations

### LAST LIGHT:
What were the highlights from today?
1.

How could I have made today even better?

#### Today's Notes
```dataview
List FROM "" WHERE file.cday = date("<% tp.file.title("YYYY-MM-DD") %>") SORT file.ctime asc
```

<% tp.file.title("YYYY-MM-DD") %>
#### Modified today
```dataview
List FROM "" WHERE file.mday = date("<% tp.file.title("YYYY-MM-DD") %>") SORT file.mtime asc
```
table file.ctime from "Folder" where file.ctime >= date(2021-08-21)-dur(7 day) where file.ctime < date(2021-08-22) sort file.ctime desc