---
type: daily
date: <% tp.file.title %>
---

#<% tp.file.title %>

**Prev::** [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title,"YYYY-MM-DD") %>]]
**Next::** [[<% tp.date.now("YYYY-MM-DD", +1, tp.file.title,"YYYY-MM-DD") %>]]
**Parent::** [[<% tp.date.now("YYYY-MM", 0, tp.file.title,"YYYY-MM-DD") %>]], [[<% tp.date.now("YYYY-[W]ww", 0, tp.file.title,"YYYY-MM-DD") %>]]

## TO DO LIST:
```dataviewjs
dv.taskList(dv.pages().file.tasks
.where(t=>t.text.includes("{{date:YYYY-MM-DD}}")))
```

## MORNING REVIEW:


## LOG:


## EXPENSES:


## EVEN REVIEW:
