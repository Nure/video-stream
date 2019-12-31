import open_trailer
import media

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump is a simple man with a low I.Q.",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=uPIEn0M8su0")


rockey = media.Movie("Rockey",
                     "Rocky Balboa, a small-time boxer, gets a supremely rare chance to fight",
                     "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                     "https://www.youtube.com/watch?v=h8nC-RnETd0")

the_pursuit_of_happiness = media.Movie("The Pursuit of Happiness",
                                       "",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                       "https://www.youtube.com/watch?v=gHXKitKAT1E")

hours_127 = media.Movie("127 Hours",
                        "",
                        "https://upload.wikimedia.org/wikipedia/en/b/b3/127_Hours_Poster.jpg",
                        "https://www.youtube.com/watch?v=OlhLOWTnVoQ")

moneyball = media.Movie("Moneyball",
                        "",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",
                        "https://www.youtube.com/watch?v=o9Q0kp8CMFQ")

the_blind_side = media.Movie("The Blind Side",
                            "",
                            "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",
                            "https://www.youtube.com/watch?v=76nhIfp9gr0")

movies = [forrest_gump, rockey, the_pursuit_of_happiness, hours_127, moneyball, the_blind_side]

open_trailer.open_movie_trailer(movies)