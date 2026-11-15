# 🎧 Model Card: Music Recommender Simulation

# Music Recommender Model Card

## 1. Model Name

**MusicMatch 1.0**

## 2. Intended Use

My music recommender helps users find songs based on their favorite genre, mood, and energy level. It assumes users know what type of music they like. This project is mainly for classroom learning, not a real music streaming app.

## 3. How the Model Works

My recommender compares the user's music preferences with each song. It gives 1.5 points for matching the genre and 1.5 points for matching the mood. It also gives up to 1 point based on how close the song's energy is to what the user likes. The program adds the points, ranks the songs, and shows the top five with explanations. I added these scoring rules to the starter program.

## 4. Data

My dataset has 18 songs. It includes different genres like pop, rock, jazz, country, reggae, classical, and EDM. There are also different moods like happy, chill, intense, romantic, sad, and peaceful. I added 8 new songs to the original 10. The dataset is small and doesn't represent everyone's music taste.

## 5. Strengths

My recommender works well when users have clear music preferences. For example, someone who likes intense rock music can receive songs that match that style. The program also explains why each song was recommended.

## 6. Limitations and Bias

My recommender only uses genre, mood, and energy to score songs. It doesn't consider lyrics, favorite artists, or listening history. It might recommend too many songs from one genre and miss good songs from other genres. The small dataset also limits the recommendations.

## 7. Evaluation

I tested my recommender using rock/intense and pop/happy music preferences. I checked whether the program ranked songs correctly and explained their scores. For the rock/intense profile, Storm Runner ranked first. I also tested whether the program loaded all 18 songs correctly.

## 8. Future Work

In the future, I would add more songs and genres. I would also include tempo, favorite artists, and listening history to improve the recommendations. I would like the program to learn from songs users like or skip.

## 9. Personal Reflection

I learned how music recommendation systems use data to predict what users might enjoy. I found it interesting that changing the scoring points can change which songs are recommended. This project helped me understand how apps like Spotify and YouTube suggest music based on user preferences.