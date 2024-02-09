```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, seasons + " x " + episodes + "ep" as "Seasons", scoreImdb + "/10⭐" as "IMDB", genre as Genre, mycurrentepisode as "Watched Episode", location as "Where"  from "LIFE/Series" where contains(status, "in progress") sort scoreImdb desc
```