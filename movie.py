# AI Recommendation System

# Movie database
movies = {
    "Action": [
        "Avengers: Endgame",
        "John Wick",
        "Mad Max: Fury Road"
    ],
    "Comedy": [
        "3 Idiots",
        "The Hangover",
        "Free Guy"
    ],
    "Horror": [
        "The Conjuring",
        "Insidious",
        "A Quiet Place"
    ],
    "Sci-Fi": [
        "Interstellar",
        "Inception",
        "The Martian"
    ],
    "Drama": [
        "The Pursuit of Happyness",
        "Forrest Gump",
        "The Shawshank Redemption"
    ]
}

print("=== Movie Recommendation System ===")

print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

user_choice = input("\nEnter your favorite genre: ")

if user_choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[user_choice]:
        print("✔", movie)
else:
    print("\nSorry! Genre not found.")