import fresh_tomatoes
import media

the_boss_baby = media.Movie("The Boss Baby",
                            "A story about how a new baby's arrival impacts a family,"
                            "told from the point of view of a delightfully unreliable narrator,"
                            " a wildly imaginative 7 year old named Tim.",
                            "https://image.tmdb.org/t/p/w640/unPB1iyEeTBcKiLg8W083rlViFH.jpg",
                            "https://www.youtube.com/watch?v=RBfCQuQqgNs")
wonder_women = media.Movie("Wonder Women",
                           "An Amazon princess comes to the world of Man to become "
                           "the greatest of the female superheroes.",
                           "https://image.tmdb.org/t/p/w640/gfJGlDaHuWimErCr5Ql0I8x9QSy.jpg",
                           "https://www.youtube.com/watch?v=5lGoQhFb4NM")
pirates_of_caribbean = media.Movie("Pirates of the Caribbean: Dead Men Tell No Tales",
                                   "Captain Jack Sparrow is pursued by an old rival,"
                                   "Captain Salazar, who along with his crew of ghost "
                                   "pirates has escaped from the Devil's Triangle,"
                                   " and is determined to kill every pirate at sea."
                                   " Jack seeks the Trident of Poseidon, a powerful artifact "
                                   "that grants its possessor total control over the seas, in order to defeat Salazar.",
                                   "https://image.tmdb.org/t/p/w640/xbpSDU3p7YUGlu9Mr6Egg2Vweto.jpg",
                                   "https://www.youtube.com/watch?v=RBfCQuQqgNs")
gurdians_galaxy = media.Movie("Guardians of the Galaxy Vol. 2",
                              "The Guardians must fight to keep their new found family together"
                              " as they unravel the mysteries of Peter Quill's true parentage.",
                              "https://image.tmdb.org/t/p/w640/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg",
                              "https://www.youtube.com/watch?time_continue=1&v=wUn05hdkhjM")
logan = media.Movie("logan",
                    "In the near future, a weary Logan cares for an ailing Professor"
                    " X in a hideout on the Mexican border. But Logan's attempts to"
                    " hide from the world and his legacy are upended when a young mutant"
                    " arrives, pursued by dark forces.",
                    "https://image.tmdb.org/t/p/w640/9EXnebqbb7dOhONLPV9Tg2oh2KD.jpg",
                    "https://www.youtube.com/watch?v=XaE_9pfybL4")
baahubali = media.Movie("Baahubali 2: The Conclusion",
                        "When Mahendra, the son of Bahubali, learns about his heritage,"
                        " he begins to look for answers. His story is juxtaposed with "
                        "past events that unfolded in the Mahishmati Kingdom.",
                        "https://image.tmdb.org/t/p/w640/sXf30F2HFpsFPXlNz7jpOySSV9I.jpg",
                        "https://www.youtube.com/watch?v=qD-6d8Wo3do")

movies = [the_boss_baby,wonder_women,pirates_of_caribbean,gurdians_galaxy,logan,baahubali]
fresh_tomatoes.open_movies_page(movies)