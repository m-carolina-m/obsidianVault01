[[00_HOME]]

```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, director as Director, scoreImdb + "/10⭐"  as "IMDB",  myrating as Score, genre as Genre, watched as Watched from "Fun/Movies" sort myrating desc, scoreImdb desc where contains(status, "complete") 
```

