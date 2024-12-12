## Sentiment Analysis on YouTube Comments 📊

### 📋 Project Overview
Analyzing YouTube video comments to extract insights into viewer sentiment using Natural Language Processing (NLP). By examining text data, this project provides a comprehensive understanding of audience engagement and emotional responses.

### 🎯 Objective
To determine the sentiment of YouTube comments (positive, neutral, or negative) and analyze trends such as emoji usage, word frequency, and category popularity.

### ✨ Key Insights and Features
- **Sentiment Analysis**: Categorized comments into positive, neutral, and negative sentiments using TextBlob.
- **Emoji Analysis**: Identified the top 10 most frequently used emojis and visualized them.
- **Category Trends**: Explored which content categories received the most likes and audience engagement.
- **Wordclouds**: Created visual representations for commonly used words in positive and negative comments.
- **Correlation Analysis**: Analyzed the relationships between views, likes, and dislikes using regression plots and heatmaps.

### 🛠 Tools and Technologies Used
- **Python Libraries**: Pandas, NumPy, TextBlob, Seaborn, Matplotlib, Plotly, WordCloud.
- **Data Visualization**: Plotly for interactive visualizations, Seaborn for statistical plots.
- **Data Handling**: CSV, JSON data processing.

### 📚 Project Learnings
- Handling missing data effectively.
- Implementing sentiment analysis using NLP techniques.
- Visualizing data insights with wordclouds and bar charts.
- Understanding the influence of user engagement metrics (like/dislike rates).

### 🛠 How to Use
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis script:
   ```bash
   python analyze_youtube_comments.py
   ```
4. Access the visualizations and summary reports in the output folder.

### 📈 Graph Visualizations
#### Wordclouds
- **Positive Sentiments**: Visualizing frequent positive words (e.g., amazing, awesome, best).
- **Negative Sentiments**: Highlighting common negative words.

#### Emoji Analysis
- Bar chart of the top 10 emojis used in comments.

#### Regression and Heatmaps
- **Regression Plots**: Showing the correlation between views, likes, and dislikes.
- **Heatmaps**: Representing the strength of these correlations.

### 🌟 Why This Project Matters
Understanding audience sentiment can help content creators refine their strategies and engage their viewers more effectively. This project showcases the power of data analytics and visualization in improving user interaction and content optimization.

### 💬 Feedback
We value your feedback! Please feel free to open issues or submit pull requests to enhance this project further. Connect with us on GitHub Discussions.
