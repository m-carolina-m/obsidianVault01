---
cssClass: wide-page, obsidian-banner

---

![[Pasted image 20240123155443.png|banner|lower]]

# HOME

moment().

>[!multi-column]  
>  
>> ## 🗓️Agenda 
>> [[moment().format('YYYY-MM-DD')]]  
>> [[<% tp.date.now(/JOUNAL/Daily/YYYY/MM-MMMM/YYYY-MM-DD-dddd) %>|Today]]
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
dv.paragraph(  
tasks + "<br>" + "<progress max=100 value=" + tasksp + "> </progress> " + tasksp + "% </p>"
)  
```

```dataview  
table WITHOUT ID (link(file.path, alias)) as Project,  
"<progress max=100 value=" + round((tasksCompleted / projectTasks) * 100) +"> </progress> " + round((tasksCompleted / projectTasks) * 100) + "% </p>" AS Progress, status AS Status   
from #project/active  
SORT file.path ASCENDING  
```

```dataviewjs  
const Title = dv.current().file.name  
const kbfile = Title + "-Kanban"  
const Tasks = dv.page(kbfile).file.tasks  
let NumberOfTasks = Tasks.length || 1  
let CompletedTasks = Tasks.where(t => t.completed)  
dv.span("<progress max=100 value=" + parseInt((CompletedTasks.length / NumberOfTasks) * 100) +"> </progress> " + parseInt((CompletedTasks.length / NumberOfTasks) * 100) + "% </p>")  
```

```dataview  
table file.ctime as Created, file.mtime as "Last modified"  
where file.name != this.file.name  
sort file.mtime DESC  
limit 10  
```