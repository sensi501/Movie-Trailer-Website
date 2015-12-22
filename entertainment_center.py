# These import statements include the media python module for detailing the Movie class code 
# while the fresh_tomatoes python module contain the final movies webpage setup code
import media
import fresh_tomatoes

# These are the three movies to be instantiated in to movie objects
full_metal_jacket = media.Movie(
    "Full Metal Jacket",
    "An outlandishly funny story about marines from training to the Vietnam War",
    "http://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
    "https://www.youtube.com/watch?v=x9f6JaaX7Wg",
    "R",
    "1987")

a_space_odyssey = media.Movie(
    "2001: A Space Odyssey",
    "A quest to uncover an artifact on the moon",
    "http://ia.media-imdb.com/images/M/MV5BNDYyMDgxNDQ5Nl5BMl5BanBnXkFtZTcwMjc1ODg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",
    "https://youtu.be/Z2UWOeBcsJI",
    "G",
    "1968")

the_matrix = media.Movie(
    "The Matrix",
    "A computer hacker joins rebels to uncover the truth about his reality",
    "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX214_AL_.jpg",
    "https://youtu.be/m8e-FF8MsqU",
    "R",
    "1999")

# A list type array containing the Movie class instances
movies = [full_metal_jacket, a_space_odyssey, the_matrix]

# A method/function of the fresh_tomatoes python module to utilize the Movie
# class instances contained in the movies list to create the final movie page
fresh_tomatoes.open_movies_page(movies)
