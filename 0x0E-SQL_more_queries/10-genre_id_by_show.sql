-- List all shows contained in DB that have at least one genre linked
SELECT tv.title, g.genre_id FROM tv_shows as tv INNER JOIN tv_show_genres as g ON tv.id = g.show_id ORDER BY tv.title, g.genre_id asc;
