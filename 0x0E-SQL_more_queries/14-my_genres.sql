-- Uses the DB to lists all genres of the show specific
SELECT tv_genres.name
	FROM tv_show_genres
	LEFT JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_shows.title = 'Dexter'
	ORDER BY tv_genres.name;
