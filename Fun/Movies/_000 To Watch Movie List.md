```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, director as Director, scoreImdb + "/10⭐" as "IMDB", genre as Genre, location as "Where" from "Fun/Movies" where contains(status, "to watch") sort scoreImdb desc
```