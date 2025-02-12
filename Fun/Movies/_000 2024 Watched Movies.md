[[00_HOME]]


```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, director as Director, scoreImdb + "/10⭐" as "IMDB",  myrating as "Rating", genre as Genre, watched as "Vista" from "Fun/Movies" where contains(status, "complete") and watched >= date("2024-01-01")
and watched <= date("2024-12-31") sort myrating desc, watched asc
```