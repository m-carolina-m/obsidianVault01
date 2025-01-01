```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Nombre, director as Director, scoreImdb + "/10⭐" as "IMDB", genre as Género, location as "Donde" from "Diversion/Peliculas" where contains(status, "to watch") sort scoreImdb desc
```