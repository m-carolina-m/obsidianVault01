---
cssclasses:
  - wide-page
alliasses: 
sleep-time: 10:30pm
wake-up-time: 06:00am
times-i-woke-up: 0
rested: 0-10
exercise: 0
arms: 0
core: 0
legs: 0 
glutes: 0
weights: 0
cardio: 0
weight: 95
water: 0-8
mood: 0-5
---

<%*
  let today     = tp.date.now("YYYY-MM-DD",  0, tp.file.title, "YYYY-MM-DD")
  let tomorrow  = tp.date.now("YYYY-MM-DD",  1, tp.file.title, "YYYY-MM-DD")
  let soon      = tp.date.now("YYYY-MM-DD",  4, tp.file.title, "YYYY-MM-DD")
%>


```calendar-nav
```

## First Light 🌞


**3 things I am grateful for...**
1.


**What will I do to make today great?**
- 

**Daily affirmations**
affirmations:: 

**Taks for the Day**
- [ ]


## [[Tasks Dashboard | Tasks]]
>[!multi-column]
> >[!Over Due]+ Due before <% today %>
>> ```tasks
>> not done
>> due before <% today %>
>> hide tags
>> hide task count 
>> group by function task.tags
>> ```
> 
>>[!Due Today|purple]+ Due <% today %>
>> ```tasks
>> not done
>> due on <% today %>
>> hide tags
>> hide task count 
>> group by function task.tags
>> ```
> 
>> [!coming-soon]+ Due soon after <% today %>
>>```tasks
>> not done
>> due after <% today %>
>> due before <% soon %>
>> hide tags
>> hide task count
>> group by function task.tags
>> ```

> [!success]+ Completed <% today %>
> ```tasks
> done <% today %>
> hide task count
> hide tags
> short mode
> group by function task.tags
> ```


## Last Light 🌚
**What were the highlights from your day?**
1. 

**How could I have made today even better?**
-

**TASKS for Tomorrow**
- [ ]

Highlights::

## Today's Notes
> [!note]+ On This Day
>  ```dataview
> List 
>  From "01-Journal/01-Daily"
> Where file.ctime >= date(<% today %>) AND file.ctime <= date(<% tomorrow %>)
>  ```

Prueba
```dataview
LIST
FROM "01-Journal/Daily"
WHERE dateformat(file.day, "MM-dd") = dateformat(this.file.day, "MM-dd")
```

> [!warning]+ Files Created (<% today %>)
>  ```dataview
>  table without id
>  file.link as Note,
>  file.folder as Folder,
>  file.ctime as "Created"
>  FROM ""
>  where file.ctime >= date(<% today %>) AND file.ctime <= date(<% tomorrow %>) AND file.path != this.file.path
>  sort file.ctime desc
>   ```

> [!summary]+  Files Modified (<% today %>)
>  ```dataview
> table without id
> file.link as Note,
> file.folder as Folder,
> file.mtime as "Last Modified"
> FROM ""
> where file.mtime >= date(<% today %>) AND file.mtime <= date(<% tomorrow %>) AND file.path != this.file.path
> sort file.mtime desc
>  ```