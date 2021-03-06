import fresh_tomatoes
import media

# Movie data (instances)

napoleon_dynamite = media.Movie("Napoleon Dynamite",
                                "In small-town Preston, Idaho,awkward teen Napoleon Dynamite (Jon Heder) "
                                "has trouble fitting in. After his grandmother "
                                "is injured in an accident, his life is made "
                                "even worse when his strangely nostalgic uncle, "
                                "Rico (Jon Gries), shows up to keep an eye on "
                                "him. With no safe haven at home or at school, "
                                "Napoleon befriends the new kid, Pedro (Efren "
                                "Ramirez), a morose Hispanic boy who speaks "
                                "little English. Together the two launch a "
                                "campaign to run for class president.",
                                "http://www.gstatic.com/tv/thumb/movieposters/34617/p34617_p_v8_ab.jpg",
                                "https://www.youtube.com/watch?v=ZHDi_AnqwN4")

oldboy = media.Movie("Oldboy",
                     "Dae-Su is an obnoxious drunk bailed from the police station "
                    "yet again by a friend. However, he's abducted from the street and wakes up in a cell, "
                    "where he remains for the next 15 years, drugged unconscious when human contact is unavoidable, "
                    "otherwise with only the television as company. And then, suddenly released, he is invited to track "
                    "down his jailor with a denouement that is simply stunning.",
                     "http://www.gstatic.com/tv/thumb/movieposters/35948/p35948_p_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=D89OHw0VsYM")

shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "Andy Dufresne (Tim Robbins) is sentenced to two consecutive life terms in "
                                   "prison for the murders of his wife and her lover and is sentenced to a tough "
                                   "prison. However, only Andy knows he didn't commit the crimes. While there, "
                                   "he forms a friendship with Red (Morgan Freeman), experiences brutality "
                                   "of prison life, adapts, helps the warden, etc., all in 19 years.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Vincent Vega (John Travolta) and Jules Winnfield (Samuel L. Jackson) are hitmen "
                            "with a penchant for philosophical discussions. In this ultra-hip, "
                            "multi-strand crime movie, their storyline "
                            "is interwoven with those of their boss, gangster Marsellus Wallace (Ving Rhames) ; "
                            "his actress wife, Mia "
                            "(Uma Thurman) ; struggling boxer Butch Coolidge (Bruce Willis) ; "
                            " master fixer Winston Wolfe (Harvey Keitel) "
                            "and a nervous pair of armed robbers, 'Pumpkin' (Tim Roth) and 'Honey Bunny' (Amanda Plummer).",
                           "http://www.gstatic.com/tv/thumb/movieposters/15684/p15684_p_v8_ac.jpg",
                           "https://www.youtube.com/watch?v=5ZAhzsi1ybM")

forrest_gump = media.Movie("Forrest Gump",
                           "Slow-witted Forrest Gump (Tom Hanks) has never thought of himself as disadvantaged, "
                            "and thanks to his supportive mother (Sally Field), he leads anything but a restricted life. "
                            "Whether dominating on the gridiron as a college football star, fighting in Vietnam or captaining "
                            "a shrimp boat, Forrest inspires people with his childlike optimism. But one person Forrest cares "
                            "about most may be the most difficult to save -- his childhood love, the sweet but "
                            "troubled Jenny (Robin Wright).",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg" )

toy_story_3 = media.Movie("Toy Story 3",
                          "With their beloved Andy preparing to leave for college, Woody (Tom Hanks), Buzz "
                          "Lightyear (Tim Allen), Jessie (Joan Cusack), and the rest of the toys find themselves "
                          "headed for the attic but mistakenly wind up on the curb with the trash. Woody's quick "
                          "thinking saves the gang, but all but Woody end up being donated to a day-care center. "
                          "Unfortunately, the uncontrollable kids do not play nice, so Woody and the gang make "
                          "plans for a great escape.",
                          "https://pics.filmaffinity.com/toy_story_3-691147043-large.jpg",
                          "https://www.youtube.com/watch?v=ZZv1vki4ou4")

# List of movies

movies = [napoleon_dynamite,oldboy, shawshank_redemption, pulp_fiction, forrest_gump, toy_story_3]

# Script to convert movie data into html

fresh_tomatoes.open_movies_page(movies)
