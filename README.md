# Animelist-Generator
Last generated at: July 21, 2023 12:01 AM CDT

## What is it?
This is a list for mapping anime from various anime websites to their ID on the TVDB. I made it for my personal use with [Plex-Meta-Manager](https://github.com/meisnate12/Plex-Meta-Manager) as the list included in the project updates once a month and I needed something more frequent. This list should update once a day using a small python script and GitHub actions.


## Lists
The two lists used to make anime_list_full.json are below. If something is incorrect it likely needs to be fixed in one of those locations.
- [Anime-Lists/anime-lists (AniDB and TVDB)](https://github.com/Anime-Lists/anime-lists/)
- [manami-project/anime-offline-database (Pretty much every anime site but not TVDB)](https://github.com/manami-project/anime-offline-database/)

## API
On the first of each month, the script will also check [TMDB](https://www.themoviedb.org/?language=en-US) for any new TMDB ids. These are looked up using the IMDB ids.