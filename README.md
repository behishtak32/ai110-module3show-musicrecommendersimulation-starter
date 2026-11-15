# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Music apps like Spotify and YouTube recommend songs based on what people like, listen to, or skip. They also look at what similar users enjoy and the type of songs a person likes. My music recommender will focus on finding songs that match the user's favorite genre, mood, and energy level. Songs that match more preferences will be recommended first.

Song Features

Title: Name of the song
Artist: Who sings the song
Genre: Type of music, like pop or rock
Mood: How the song feels, like happy or sad
Energy: Whether the song is calm or energetic
Tempo: How fast or slow the song is

UserProfile Features

Favorite genre: Type of music the user likes
Preferred mood: Mood the user enjoys

Preferred energy: Whether the user likes calm or energetic songs

Preferred tempo: Whether the user prefers fast or slow songs

How Recommendations Work

My program will compare the user's preferences with each song. The more features that match, the higher the song's score will be. Songs with the highest scores will be recommended first.

---
My Algorithm Recipe

My music recommender will give points to songs based on how well they match the user's music taste.

Genre: Add 1.5 points if the genre matches.

Mood: Add 1.5 points if the mood matches.

Energy: Add up to 1 point depending on how close the song's energy is to the user's preferred energy.

The program will add the points together. Songs with higher scores will be recommended first.


Possible Biases

My music recommender might recommend too many songs from the user's favorite genre and miss good songs from other genres. It also only looks at a few features, so it might not always understand what the user really likes.

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:


2. Rooftop Lights (Score: 2.46)
   Reasons: mood match (+1.5), energy closeness (+0.96)

3. Gym Hero (Score: 2.37)
   Reasons: genre match (+1.5), energy closeness (+0.87)

4. Night Drive Loop (Score: 0.95)
   Reasons: energy closeness (+0.95)

5. Golden Steps (Score: 0.94)
   Reasons: energy closeness (+0.94)


---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



