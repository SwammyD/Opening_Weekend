from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True) # to proxy requests

print(imdb.search_for_title("The Dark Knight"))