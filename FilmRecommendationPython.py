import pandas as pd

films_df = pd.read_csv(r"Z:\A_University Stuff\A_Waterloo\Hackathons\Films.csv")

class Films:
    def __init__(self, genre, rating):
        self.genre = genre
        self.rating = rating

user_genre = str(input("Entre a movie genre (Action, Comedy, Drama, Horror, Romance or Sci-fi): "))
user_rating = str(input("Entre a movie rating (from 0.0 to 10.0): "))
userInput = Films(user_genre, user_rating)
print("Here are your Film Recommendations:")
rec_df = films_df[(films_df.genre == user_genre) & (films_df.vote_average <= (float(user_rating)+0.5)) & (films_df.vote_average >= (float(user_rating)-0.5))]["title"]
if (rec_df.shape[0]) > 0:
    print(rec_df.to_string(index=False))
else:
    print("We can't find any recommendations. Please try a different rating.")







