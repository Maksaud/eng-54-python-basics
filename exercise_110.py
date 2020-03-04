
# Movie Ratings!

#  As a user I should be able to ask the user for the a rating, and receive back the appropriate response:
user_input = input("What movie rating are you looking for? ")

movie_rating = {
    "Universal": "Everyone can watch",
    "pg": "general viewing ",
    "12": "films are classified 12",
    "15": "no one younger than 15 may see a 15 film in a cinema",
    "18": "no one younger than 18 film in a cinema"
}

if user_input == "universal":
    print(movie_rating["Universal"])
elif user_input == "pg":
    print(movie_rating["pg"])
elif user_input == "12":
    print(movie_rating["12"])
elif user_input == "15":
    print(movie_rating["15"])
elif user_input == "18":
    print(movie_rating["18"])
else:
    print("That is not a rating")

# check for rating for this movie:
  ## universal -> everyone can watch
  ## pg --> General viewing, but some scenes may be unsuitable for young children
  ## 12 -->  Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.
  ## 15 --> No one younger than 15 may see a 15 film in a cinema.
  ## 18 --> No one younger than 18 may see an 18 film in a cinema.