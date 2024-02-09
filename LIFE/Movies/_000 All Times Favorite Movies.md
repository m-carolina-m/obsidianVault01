```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, director as Director, scoreImdb + "/10⭐"  as "IMDB",  myrating as "My Rating", genre as Genre, watched as "Date Watched" from "LIFE/Movies" sort myrating desc, scoreImdb desc where contains(status, "complete") 
```

