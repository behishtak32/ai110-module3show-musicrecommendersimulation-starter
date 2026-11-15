"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = {
        "Profile 1: High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
        },
        "Profile 2: Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.2,
        },
        "Profile 3: Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.85,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print("-" * len(profile_name))
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} (Score: {score:.2f})")
            print(f"   Reasons: {explanation}")


if __name__ == "__main__":
    main()
