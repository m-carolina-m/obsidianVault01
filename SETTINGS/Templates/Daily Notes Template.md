---
type: daily
date: # <% moment(tp.file.title,'YYYY-MM-DD').format("MM, DD, YYYY") %>
---

<%tp.date.now%>
<< [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').subtract(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Yesterday]] \| [[<% fileDate = moment(tp.file.title, 'YYYY-MM-DD-dddd').add(1, 'd').format('[JOURNAL]/[Daily]/YYYY/MM-MMMM/YYYY-MM-DD-dddd') %>\|Tomorrow]] >>

## TO DO LIST:
```dataviewjs
dv.taskList(dv.pages().file.tasks
.where(t=>t.text.includes("{{date:YYYY-MM-DD}}")))
```

## FIRST LIGHT

<% tp.file.cursor() %>
## EXPENSES:


## LAST LIGHT:
