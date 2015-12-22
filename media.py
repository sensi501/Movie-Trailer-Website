# This import statement links the webbrowser python module to allow for the
# utilization of the webbrowser.open method required for the show_trailer method
import webbrowser

class Movie():
    # This init constructor method details the required information for the
    # creation of the Movie object to acquire information such as:
    # title, storyline, poster image, trailer, rating, and release year
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_rating, movie_release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
        self.release_year = movie_release_year

    # The show_trailer method allows movie objects to be linked to their
    # respective movie trailers
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
