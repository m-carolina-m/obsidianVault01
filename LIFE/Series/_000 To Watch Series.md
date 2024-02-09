```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, seasons + " x " + episodes + "ep" as "Seasons", scoreImdb + "/10⭐" as "IMDB", genre as Genre, location as "Where"  from "LIFE/Series" where contains(status, "to watch") sort scoreImdb desc
```