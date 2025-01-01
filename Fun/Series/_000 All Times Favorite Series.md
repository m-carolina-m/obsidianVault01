```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, seasons + " x " + episodes + "ep" as "Seasons", scoreImdb + "/10⭐"  as "IMDB",  myrating as "My Rating", genre as Genre, lastwatched as "Date Completed" from "Fun/Series" sort myrating desc, scoreImdb desc where contains(status, "complete") 
```

