# 🎧 Model Card: Music Recommender Simulation

# Music Recommender Model Card

## 1. Model Name

**MusicMatch 1.0**
My music recommender helps users find the top five songs that match their favorite genre, mood, and energy level.
This system should not be used as a professional music recommendation service because it has a small dataset and does not learn from real users' listening habits.
## 2. Intended Use

My music recommender helps users find songs based on their favorite genre, mood, and energy level. It assumes users know what type of music they like. This project is mainly for classroom learning, not a real music streaming app.

## 3. How the Model Works

My recommender compares the user's music preferences with each song. It gives 1.5 points for matching the genre and 1.5 points for matching the mood. It also gives up to 1 point based on how close the song's energy is to what the user likes. The program adds the points, ranks the songs, and shows the top five with explanations. I added these scoring rules to the starter program.

## 4. Data

My dataset has 18 songs. It includes different genres like pop, rock, jazz, country, reggae, classical, and EDM. There are also different moods like happy, chill, intense, romantic, sad, and peaceful. I added 8 new songs to the original 10. The dataset is small and doesn't represent everyone's music taste.

## 5. Strengths

My recommender works well when users have clear music preferences. For example, someone who likes intense rock music can receive songs that match that style. The program also explains why each song was recommended.

## 6. Limitations and Bias

My music recommender has only 18 songs, so there are not enough choices for every music taste. I noticed that giving more points to energy can make songs rank highly even when the genre does not match. Some genres have more songs than others, which can make recommendations less fair. The program also recommends similar songs repeatedly because it always chooses the highest scores. In the future, I could add more songs and improve the scoring system to give users more variety.

## 7. Evaluation

I tested my music recommender with three different profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I checked the top five songs for each profile to see whether they matched the user's music taste. The High-Energy Pop profile looks for happy pop songs with high energy, while Chill Lofi looks for calmer music. Deep Intense Rock looks for intense rock songs with higher energy. These profiles helped me see how different preferences affect the recommendations.
I also tested changing the scoring weights. I reduced genre points from 1.5 to 0.75 and increased energy points from 1 to 2. This made energy more important than genre in the scoring system. One thing I noticed is that songs can still receive points for energy even when their genre or mood does not match. This showed me that the scoring system does not always recommend songs based on genre alone.
When I compared High-Energy Pop and Chill Lofi, I noticed that they recommended different songs because their moods and energy levels were different. Deep Intense Rock focused more on intense and energetic songs compared with Chill Lofi. I also noticed that some songs appeared in different profiles because their energy levels were close to what the users preferred.
## 8. Future Work

In the future, I would add more songs and genres. I would also include tempo, favorite artists, and listening history to improve the recommendations. I would like the program to learn from songs users like or skip.

## 9. Personal Reflection
I learned how music recommendation systems use data to suggest songs based on what users like. My biggest learning moment was understanding how changing the scoring points could change the recommendations. Using AI tools helped me write the code and understand how the program works. However, I still needed to run the program and check for errors. I was surprised that a simple scoring system could recommend songs in a way that feels similar to real music apps. If I continued this project, I would add more songs and improve the recommendations based on users' listening habits.