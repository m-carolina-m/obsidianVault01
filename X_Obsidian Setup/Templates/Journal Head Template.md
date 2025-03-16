---
tags:
  - journal
---
[[<% moment(tp.file.title,'DDMM').add(-1,'days').format("DDMM") %>]]  <<  [[<% moment(tp.file.title,'DDMM').format("MMM") %>]]  >> [[<% moment(tp.file.title,'DDMM').add(1,'days').format("DDMM") %>]]  

# Tareas Pendientes

```todoist
name: "SENIAT"
filter: "/SENIAT"
sorting: [ date, priority ]
```

<br/>

```todoist
name: "Droguerias"
filter: "/Droguerias"
sorting: ["date", "priority"]
```

<br/>

```todoist
name: "Por hacer"
filter: " today | overdue "
sorting: [ date, priority ]
groupBy: project
```

<br/>
