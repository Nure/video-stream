import webbrowser

class Movie():
    """This class consists movie information """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.story_line = movie_storyline
        self.image_url = poster_image
        self.youtube_trailer_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.youtube_trailer_url)

