import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def save_wordcloud(text):
  wordcloud = WordCloud(width=3000,
                        height=2000,
                        random_state=1,
                        background_color='white',
                        collocations=True,
                        stopwords=STOPWORDS).generate(text)
  #Set figure size
  plt.figure(figsize=(30, 20))

  # Display image
  plt.imshow(wordcloud)

  # No axis
  plt.axis("off")

  # save the plot
  plt.savefig('images/articles_word_cloud.png')
