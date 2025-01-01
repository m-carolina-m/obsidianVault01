```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Nombre, director as Director, scoreImdb + "/10⭐" as "IMDB",  myrating as "Puntuación", genre as Género, watched as "Vista" from "Diversion/Peliculas" where contains(status, "complete") and watched >= date("2025-01-01")
and watched <= date("2025-12-31") sort myrating desc, watched asc
```