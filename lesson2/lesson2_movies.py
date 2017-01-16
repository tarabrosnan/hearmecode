movie_title = ['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight', '12 Angry Men']
movie_rating = ['R', 'R', 'R', 'PG-13', 'Approved']
bechdel_rating = [0, 2, 2, 3, 0]
imdb_rating = [9.3, 9.2, 9.0, 9.0, 8.9]
imdb_genre = ['Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama']

for movie_title, movie_rating, bechdel_rating, imdb_rating, imdb_genre in zip(movie_title, movie_rating, bechdel_rating, imdb_rating, imdb_genre):
	print "{0},{1},{2},{3},{4}".format(movie_title, movie_rating, bechdel_rating, imdb_rating, imdb_genre)