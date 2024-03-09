---
cssclasses:
  - wide-page
aliases: the one where/when ....
enjoyment: /10
why: 
---

```calendar-nav
```


## What is worth remembering about this week?

## What did I accomplish this week?

## What could I have done better this week?

## What am I grateful for this week, and what am I thinking of?

## What did I set to achieves this week?

## What do I want to achieve next week?

## Sweat Tracker
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

startDate: 2024-02-26
endDate: 2024-03-03

## Weight

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


## Combined:

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

## Sleep tracker 
Bar graph y axis de time vs x axis day 

-------
Dates | Day |  higlight |  3 habits (Sleep hours, exercise, water)

Books Read

Movies Watched

Series Watched