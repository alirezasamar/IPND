import media
import fresh_tomatoes

the_intouchables = media.Movie("The Intouchables", 
	"a quadriplegic aristocrat who was injured in a paragliding accident and a young man from the projects.", 
	"https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg", 
	"https://www.youtube.com/watch?v=34WIbmXkewU")

before_midnight = media.Movie("Before Midnight", 
	"We meet Jesse and Celine nine years on in Greece. "
	"Almost two decades have passed since their first meeting on that train bound for Vienna.", 
	"https://upload.wikimedia.org/wikipedia/en/a/ad/Before_Midnight_poster.jpg", 
	"https://www.youtube.com/watch?v=euOJkb0U8vE")

kung_fu_panda3 = media.Movie("Kung Fu Panda 3", 
	"In the Valley of Peace, Po the Panda finds himself chosen as the Dragon Warrior "
	"despite the fact that he is obese and a complete novice at martial arts.", 
	"https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg", 
	"https://www.youtube.com/watch?v=10r9ozshGVE")

gravity = media.Movie("Gravity", 
	"a heart-pounding thriller that pulls you into the infinite and unforgiving realm of deep space.", 
	"https://upload.wikimedia.org/wikipedia/en/f/f6/Gravity_Poster.jpg", 
	"https://www.youtube.com/watch?v=OiTiKOy59o4")

interstellar = media.Movie("Interstellar", 
	"The film features a crew of astronauts who travel through a wormhole in search of a new home for humanity.", 
	"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", 
	"https://www.youtube.com/watch?v=zSWdZVtXT7E")

spotlight = media.Movie("Spotlight", 
	"The film follows The Boston Globe's Spotlight team, the oldest continuously operating newspaper investigative journalist unit in the United States, "
	"and its investigation into cases of widespread and systemic child sex abuse in the Boston area by numerous Roman Catholic priests.", 
	"https://upload.wikimedia.org/wikipedia/en/f/f3/Spotlight_%28film%29_poster.jpg", 
	"https://www.youtube.com/watch?v=EwdCIpbTN5g")


movies = [the_intouchables, before_midnight, kung_fu_panda3, gravity, interstellar, spotlight]
fresh_tomatoes.open_movies_page(movies)
