import pandas as pd

# Load the movie and reviews data
reviews_file = "rotten_tomatoes_critic_reviews.csv/rotten_tomatoes_critic_reviews.csv"
movie_file = "rotten_tomatoes_movies.csv/rotten_tomatoes_movies.csv"

# Read the Excel files
movies_df = pd.read_csv(movie_file)
reviews_df = pd.read_csv(reviews_file)

# Group reviews by "rotten_tomatoes_link" and concatenate them into a single string per movie
reviews_df = reviews_df.dropna(subset=["review_content"])
reviews_grouped = reviews_df.groupby("rotten_tomatoes_link")["review_content"].apply(lambda x: " || ".join(x)).reset_index()

# Merge with movies_df
movies_with_reviews_df = movies_df.merge(reviews_grouped, on="rotten_tomatoes_link", how="left")

# Rename the column for clarity
movies_with_reviews_df.rename(columns={"review_content": "all_reviews"}, inplace=True)

# Save the modified movie dataset
modified_movie_file = "modified_sample_movie.xlsx"
movies_with_reviews_df.to_excel(modified_movie_file, index=False)

print(f"Modified movie dataset saved as {modified_movie_file}")
