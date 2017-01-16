movie_titles = ['Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight', '12 Angry Men']
movie_ratings = ['R', 'R', 'R', 'PG-13', 'Approved']
bechdel_score = [0, 2, 2, 3, 0]
imdb_genre = ['Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama']
imdb_rating = [9.2, 9.2, 9.0, 8.9, 8.9]

for movie_titles, movie_ratings, bechdel_score, imdb_genre, imdb_rating in zip(movie_titles, movie_ratings, bechdel_score, imdb_genre, imdb_rating):
	print "{0},{1},{2},{3},{4}".format(movie_titles, movie_ratings, bechdel_score, imdb_genre, imdb_rating)