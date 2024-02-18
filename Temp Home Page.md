---
cssClass: wide-page
---
`$=moment(dv.current().updated).format("YYYY-MM-DD")`
>[!multi-column]  
>  
>> ## 🗓️Agenda  
>> `$= '[['+moment().format("YYYY-MM-DD")+'|Today]]'`  
>> `$= '[['+moment().format("YYYY-[W]ww")+'|Week]]'`  
>> `$= '[['+moment().format("YYYY - MM-MMM")+'|Month]]'`  
>  
>> ## 🎚️Work  
>> [[01 PKM|PKM]]  
>> [[02 Projects|Projects]]  
>> [[02-servers|Servers]]  
>> [[People|People]]  
>  
>> ## 😎 Life OS  
>> [[01 Nuno|Nuno]]  
>> [[02 xxx|xxx]]  
>> [[03 xxx|xxx]]  
>> [[Monthly Payments Map]]  
>  
>> ## 🍃 Evergreen  
>> [[Obsidian Hotkeys]]  
>> [[Obsidian Callouts]]  
>> [[Windows Terminal Shortcuts]]  
>> [[Vim mode shortcuts]]  


```dataviewjs  
let nofold = '!"04 Templates'  
let allFile = dv.pages().file  
let totalTask = allFile.tasks.length  
let completedTask = allFile.tasks.where(t => !t.completed).length  
let tasks = "You have completed " + completedTask + " tasks of " + totalTask + " !"  
let tasksp = Math.round((completedTask / totalTask) * 100)  
let pb = "![progress]([https://progress-bar.dev/](https://progress-bar.dev/)" + tasksp + "/)"  
dv.paragraph(  
tasks + "<br>" + pb  
)  
```

```dataview  
table WITHOUT ID (link(file.path, alias)) as Project,  
"![progress]([https://progress-bar.dev/](https://progress-bar.dev/)" + round((tasksCompleted / projectTasks) * 100) + "/)" AS Progress, status AS Status   
from #project/active  
SORT file.path ASCENDING  
```
