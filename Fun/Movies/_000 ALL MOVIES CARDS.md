---
cssclasses:
  - cards
  - wide-page
---

```dataview
table without id ("![](" + poster + ")") as Poster, file.link as Nombre, released as Estreno, "by " + director as Director, "⭐" + scoreImdb as "IMDB", rated as Clasificación from "Diversion/Peliculas" where  type != movie and poster != "N/A" and poster != empty

```

