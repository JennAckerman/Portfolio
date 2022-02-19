# Spotify Concert Genre Assignment

**Daugherty Point of Concept**

### Problem Statement:

The US based record label JAMM suffered large dips in both music and concert revenue due to the ongoing Covid-19 pandemic.  As higher percentages of the Worlds population become vaccinated, concert halls are beginning to open back up, and people are now looking forward to experience-based entertainment.  This has come to the attention of JAMM senior level management, and are now tasked with coming up with a business plan that can accelerate its revenue by the end of most major Covid-19 restrictions and consumers' confidence in healthy participation rises.  With this in mind, JAMM aspires to understand the demand for the genres that they offer in a Post-Pandemic setting. 

JAMM has reached out to our consulting company with the knowledge that a previous assignment found customers have been looking for more upbeat, energetic music styles recently, to discern the factors that seperates each genre from one another to implement a future assignment concerning highest revenue probability of future concerts.  

Notably, JAMM wants to find significant variables in genre types, which variables tend to coincide with one another, and which genre types group best together in terms of those variables and variable parings.

### Business Goal:

Our consulting team is tasked with modeling the variables as they fit with other variables and genres.  This will then proceed to be reported to stakeholders for them to understand how each genre fits the customers' demand, where they then can correct the current business approach to meet the new market.

## Understanding the Data

**Data Source**

https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify/discussion/206958

### Data Description

![Spotify Conceptual](https://user-images.githubusercontent.com/99898494/154557342-c14e4231-cc61-4804-a148-1da0c9dcbd72.jpeg)


The original data file that we were given consisted of 22 columns: 
![gdf](https://user-images.githubusercontent.com/99898494/154581006-7c5a447d-c8e7-4826-a23c-f7f0386aa8b8.png)

Explanation of variables left to right:

**Danceability -** describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

**Energy -** is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

**Key -** The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.

**Loudness -** The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks.   Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.

**Mode -** Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived.

**Speechiness -** Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

**Acousticness -** A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

**Instrumentalness -** Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

**Liveness -** Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.

**Tempo -** The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. 

**Duration_ms -** The duration of the track in milliseconds.

**Valence -** A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

**Genre -** The genre of the song. For example, pop, rock etc.
The participant is required to predict the genre of the song based on the details of the song given in test set

**Song_name -** The title of the song on spotify


### Cleaning the Data
![gdf_describe](https://user-images.githubusercontent.com/99898494/154584136-07e5711e-06b5-455d-9f61-a4d7d72e169d.png)

Total Columns: 42,305


![cleaning nulls and parameters](https://user-images.githubusercontent.com/99898494/154716478-18d2bdfe-03ef-4c78-8cec-1c3f2fdb6eed.png)


Nulls: 0
Outliers: 0 

**Removing Unwanted Columns**

![drop columns](https://user-images.githubusercontent.com/99898494/154717012-e879d9b7-fb57-448a-b181-c5f37d76af0e.png)


![clean](https://user-images.githubusercontent.com/99898494/154585043-3dfeb656-f73c-4769-badd-f2f253b227ef.png)


### Finding Insights
Our major findings:

Two major variables for customer demand was Energy and Danceability, as they both meet the requirements of upbeat, exciting experiences.  For Concerts in the short term, the findings for genre were as follows: 

![AVG breakdown 2](https://user-images.githubusercontent.com/99898494/154708865-75a071b2-c967-429c-9ad0-0f17b715d390.png)
![AVG Highest Genre](https://user-images.githubusercontent.com/99898494/154695597-c5f34221-ac2b-47f4-9bf4-f2e2f7085b97.png)

The genres "Techhouse","Psytrance", "Techno", and "Trap" all have the highest average Energy and Danceability, making them most likely to meet the requirements of our client's customers.

For Albums and subsequent concerts in the long term, we also researched into what may gain the highest return on investment in terms of both concert revenue and new album project revenue.  Following highest Danceability and Energy metrics would incur higher costs, considering Danceability and Energy is usually scored after a song has been made.  To mitigate these costs, our consulting team has found metrics in Loudness, Tempo and Speechiness that would help determine both Energy and Danceability for future mimimun viable products. 

![Loud vs Energy](https://user-images.githubusercontent.com/99898494/154606062-ecd60003-08c1-46e2-a729-55f0eea13016.png)

Loudness and Energy have a heavy correlation showing that on average, the louder a song, the more likely the higher energy it would have.  This should be used in conjunction with other correlations so that the client can reduce possible endogeneity.

![Dance to Tempo](https://user-images.githubusercontent.com/99898494/154606075-235a482e-d858-43de-a055-36ba8b82933e.png)

This was a surprising find, as our first assumption would be that the higher the tempo = the higher the danceability. However it is actually showing that there are peek tempos that have highest danceability, and luls in between that actually lower danceability scores.

![Lyrics to Danceability](https://user-images.githubusercontent.com/99898494/154606098-d2c7f9cc-48d3-4862-a84c-4efe51f00b0a.png)

This is a very light correlation which would be used best as an extra metric, after all others have been used.  It shows that the danceability of a song on average goes up if there is at least a little bit of speechiness.  

### Final Notes

For short term Concert Tours, we recommend choosing artists in the genres "Techhouse","Psytrance", "Techno", and "Trap", for highest upbeat and exciting experience.  

For long term minimum viable products that follow new customer demand, we recommend focusing on the loudness of a song, specific tempos in between 100-130 and 190-210, and after using both of those, check the lyrical density of the song.

