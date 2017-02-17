movie_titles = ['Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'The Dark Knight', '12 Angry Men']
parental_guidance_ratings = ['R', 'R', 'R', 'PG-13', 'Approved']
bechdel_score = [0, 2, 2, 3, 0]
imdb_genre = ['Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama', 'Crime/Drama']
imdb_rating = [9.2, 9.2, 9.0, 8.9, 8.9]

# Movie titles: top 5 rated on IMDB
# Parental Guidance Ratings source: http://imdb.com/
# Bechdel score source: http://shannonvturner.com/bechdel
# IMDB genre source: http://imdb.com/
# IMDB rating source: http://imdb.com/

# Prints results in a comma separated format to copy and paste into a csv
for movie_titles, parental_guidance_ratings, bechdel_score, imdb_genre, imdb_rating in zip(movie_titles, parental_guidance_ratings, bechdel_score, imdb_genre, imdb_rating):
	print "{0},{1},{2},{3},{4}".format(movie_titles, parental_guidance_ratings, bechdel_score, imdb_genre, imdb_rating)