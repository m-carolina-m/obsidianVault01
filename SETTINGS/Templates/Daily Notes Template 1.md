---
type: daily
date: # <% moment(tp.file.title,'YYYY-MM-DD').format("MM, DD, YYYY") %>
---

# <% moment(tp.file.title,'YYYY-MM-DD').format("dddd, MMMM DD, YYYY") %>

<< [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').subtract(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Yesterday]] \| [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').add(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Tomorrow]] >>

## TO DO LIST:
```dataviewjs
dv.taskList(dv.pages().file.tasks
.where(t=>t.text.includes("{{date:YYYY-MM-DD}}")))
```

## FIRST LIGHT


## EXPENSES:


## LAST LIGHT:

### 📅 Daily Questions

##### 🌜 Last night, after work, I...


##### 🙌 One thing I'm excited about right now is...


##### 🚀 One+ thing I plan to accomplish today is...

##### 👎 One thing I'm struggling with today is...

# 📝 Notes
<% tp.file.cursor() %>

### Notes created today
```dataview
List FROM "" WHERE file.cday = date("<%tp.date.now("YYYY-MM-DD")%>") SORT file.ctime asc
```

### Notes last touched today

```dataview
List FROM "" WHERE file.mday = date("<%tp.date.now("YYYY-MM-DD")%>") SORT file.mtime asc
```

