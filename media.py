import webbrowser


class Movie:
    """ This class creates a movie instance with four
    argument and it has a function to play youtube trailer for that movie
    title = title of the movie
    storyline = storyline of the movie
    poster_image = poster of the movie
    trailer_youtube = youtube url for the trailer of the movie"""

    def __init__(self, title,storyline,poster_image,trailer_youtube):
        self.title = title
        self.storyline = storyline
        self .poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Function to Play trailer from youtube
    def play_trailer(self):
        webbrowser.open(self.trailer_youtube)
