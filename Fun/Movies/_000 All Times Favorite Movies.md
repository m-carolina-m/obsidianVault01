```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Nombre, director as Director, scoreImdb + "/10⭐"  as "IMDB",  myrating as Puntuación, genre as Género, watched as Vista from "Diversion/Peliculas" sort myrating desc, scoreImdb desc where contains(status, "complete") 
```

