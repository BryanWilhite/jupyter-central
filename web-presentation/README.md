# Songhay Web Presentations

Here are my notes around modernizing the Web Presentation stack used mostly on kintespace.com. For over a decade, the Presentation was static HTML, generated from an offline SQL Server database. This modernization effort respects the small scale of Songhay Publications and replaces SQL Server as a primary data source with Markdown and JSON static files supplemented by a tiny document database, LiteDB.

The new Presentation stack includes:

- The [Songhay Publications C# project](https://github.com/BryanWilhite/Songhay.Publications) (`Songhay.Publications`) is the core of this modernization effort, centralizing routines for conventional Markdown and JSON-rendered Publication index formats.
- [11ty.dev](https://www.11ty.dev/) is the static-site generator technology, replacing the SQL-Server-based custom solution built by this Studio.
- [Azure Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/) is the conventional store for Publications static file formats.
- [Azure App Service](https://docs.microsoft.com/en-us/azure/app-service/overview) is the Presentation destination of choice for Songhay Publications.
- The Songhay Publications Kinté Space project is the first customer of `Songhay.Publications`.

@[BryanWilhite](https://twitter.com/BryanWilhite)
