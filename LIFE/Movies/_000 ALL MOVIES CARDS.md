---
cssclasses:
  - cards
  - wide-page
---

```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Title, released as Released, "by " + director as Director, "⭐" + scoreImdb as "IMDB", rated from "LIFE/Movies" where  type != movie and poster != "N/A" and poster != empty

```

