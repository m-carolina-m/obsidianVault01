Calendar View
```tracker
searchType: frontmatter
searchTarget: exercise
folder: 01-Journal/01-Daily
datasetName: Exercise
month:
	startWeekOn: 'Mon'
	color: steelblue
```

searchType can be dvField for a tag inside de text of the note 

Calendar View with zoom and annotation 
```tracker
searchType: frontmatter
searchTarget: exercise
folder: 01-Journal/01-Daily
datasetName: Exercise
fixedScale: 1.5
month:
	mode: annotation
	annotation: 🏋️‍♀️
	startWeekOn: 'Mon'
	color: steelblue
```

```tracker
searchType: frontmatter
searchTarget: exercise
folder: 01-Journal/01-Daily
datasetName: Exercise
summary:
	template: "Longest Streak: {{maxStreak()}} day(s)\\nLongest Break: {{maxBreaks()}} day(s) \\nLast Streak: {{currentStreak()}} day(s)"
```

threshold: 7 
circleColorByValue: true
todayRingColor: white
selectedRingColor: steelblue

## Water
```tracker
searchType: frontmatter
searchTarget: water
folder: 01-Journal/01-Daily
datasetName: Water
bar:
```

```tracker
searchType: frontmatter
searchTarget: water
folder: 01-Journal/01-Daily
datasetName: water
summary:
	template: "Minimum: {{min()}} Glasses\nMaximum: {{max()}} Glasses\nMedian: {{median()}} Glasses\nAverage: {{average()}} Glasses"
```

## Mood Tracker
```tracker
searchType: frontmatter
searchTarget: mood
folder: 01-Journal/01-Daily
line:
	title: "Mood (0 Bad-5 Great)"
	yAxisLabel: Mood
	lineColor: "#d65d0e"
```

Combined:

```tracker
searchType: frontmatter
searchTarget: weight, mood
folder: 01-Journal/01-Daily
datasetName: weight, mood
line:
	title: "Weight & Mood"
	lineColor: yellow, "#d65d0e"
	yAxisLocation: left, right
	yAxisLabel: Weight, "Mood (0 Bad-5 Great)"
	showLegend: True
	
```


```tracker
searchType: frontmatter
searchTarget: exercise
folder: 01-Journal/01-Daily
datasetName: Exercise
month:
	startWeekOn: 'Mon'
	color: steelblue
```

```tracker
searchType: frontmatter
searchTarget: exercise
folder: 01-Journal/01-Daily
datasetName: Exercise
summary:
	template: "Longest Streak: {{maxStreak()}} day(s)\\nLongest Break: {{maxBreaks()}} day(s) \\nLast Streak: {{currentStreak()}} day(s)"
```


## My Weeks in Color
```dataview
table aliases, enjoyment, why
from "01-Journal/02-Weekly"
```


TOTAL
```tracker
searchType: task.done, task.all
searchTarget: work, work
summary:
	template: "tasks - {{sum(dataset(0))/sum(dataset(1))*100}}% - {{sum(dataset(0))}}/{{sum(dataset(1))}} Days Completed"
```
