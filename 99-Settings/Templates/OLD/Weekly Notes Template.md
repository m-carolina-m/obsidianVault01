## TO DO LIST
```dataview
task FROM "SENIAT" WHERE due <= date({{date:YYYY-MM-DD}}) AND due >= date({{date:YYYY-MM-DD}}) - dur(7days) SORT file.day ASC
```
LIST FROM #daily_journal WHERE file.day <= date({{date:YYYY-MM-DD}}) AND file.day >= date({{date:YYYY-MM-DD}}) - dur(7days) SORT file.day ASC

dataview 
task
from "SENIAT"
where due >= date(today) and due < date(today) + dur(7 days)

dataview 
task
from "SENIAT"
where due >= ("2024-01-08") and due < ("2024-01-08") + dur(7 days)

dataview
task FROM "SENIAT" WHERE !completed and due <= date({{date:YYYY-MM-DD}}) AND due >= date({{date:YYYY-MM-DD}}) - dur(7days) SORT file.day ASC
## OTHER