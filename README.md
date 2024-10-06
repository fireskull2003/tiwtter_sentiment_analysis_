# tiwtter_sentiment_analysis


This repository contains a Python project that performs sentiment analysis on tweets. The project uses TextBlob to calculate the sentiment polarity of each tweet and classifies them into Positive, Negative, or Neutral categories. The results are visualized using matplotlib and seaborn.

Project Structure
task 1/Tweets.csv: The dataset containing the tweets for sentiment analysis.
sentiment_analysis.py: The main script that performs data cleaning, sentiment analysis, and visualization.
README.md: This file providing an overview of the project.
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.x
Pandas
TextBlob
Matplotlib
Seaborn
You can install the required packages using pip:

pip install pandas textblob matplotlib seaborn

Dataset
The dataset Tweets.csv should be placed in the task 1/ directory. It contains a column text that holds the content of the tweets.

Running the Project
To run the sentiment analysis script:

Clone the repository.
Make sure the dataset is in the correct directory.
Run the sentiment_analysis.py script.
bash
Copy code
python sentiment_analysis.py
The script performs the following steps:

Data Cleaning: Converts the text to lowercase.
Sentiment Analysis: Uses TextBlob to calculate the polarity of each tweet.
Sentiment Classification: Classifies the sentiment into Positive, Negative, or Neutral based on the polarity score.
Visualization: Plots the distribution of sentiments using seaborn.
Example Output
After running the script, the sentiment labels (Positive, Negative, Neutral) are printed along with the sentiment distribution:

 Sentiment Distribution:
 Positive    500
 Neutral     300
 Negative    200
 A bar plot will also be displayed showing the sentiment distribution.

Code Breakdown
clean_text(text): Converts the tweet text to lowercase.
get_sentiment(text): Uses TextBlob to calculate the sentiment polarity.
classify_sentiment(polarity): Classifies the sentiment based on polarity value:
Positive: Polarity > 0
Negative: Polarity < 0
Neutral: Polarity == 0
Visualizations
The project uses seaborn to plot a countplot that visualizes the distribution of Positive, Negative, and Neutral tweets.
