```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, director as Director, scoreImdb + "/10⭐" as "IMDB",  myrating as "My Rating", genre as Genre, watched as "Date Watched" from "LIFE/Movies" where contains(status, "complete") and watched >= date("2023-01-01")
and watched <= date("2023-12-31") sort myrating desc, watched asc
```