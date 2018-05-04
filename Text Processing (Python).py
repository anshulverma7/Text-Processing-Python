# Author: Anshul Verma

# Text Processing 

# EM624 - Exercise 08

import pandas as pd

# to open the csv file
file = open("H_Clinton-emails.csv","r")

# to create dataframe from csv file
df = pd.read_csv(file)
df = df.replace('\n',' ', regex=True)

# to create a list of the senders (MetadataFrom)
df1 = df["MetadataFrom"]

# to create a list of contents (RawText)
df2 = df["RawText"]

# to calculate and print top 15 senders
df3 = df['MetadataFrom'].value_counts()
print df3[:15].to_string(header=False)

# to create list of words
text = ' '.join(df2)
words=[]
for i in text.strip().split():
    words.append(i)

# to create list of stopwords
stop = ("UNCLASSIFIED U.S. Department of State Case No. Doc No. Date: STATE DEPT. - PRODUCED TO HOUSE SELECT BENGHAZI COMM. SUBJECT TO AGREEMENT ON SENSITIVE INFORMATION & REDACTIONS. NO FOIA WAIVER. RELEASE IN FULL From: Sent: To: Subject: FW: mailto: H Abedin Huma Milss Cheryl D Sullivan Jacob J sbwhoep Jiloty Lauren C Valmoro Lona J Slaughter Anne-Marie Verma Richard R PIR McHale Judith A hrod17 clintonemail Muscatine Lissa MillsCD state.gov Verveer Melanna S United States Original Message Part B6 HDR22 state gov said will today")
stopwords=[]
for i in stop.strip().split():
    stopwords.append(i)

# to create list of filtered words
filtered_words=[]
for i in words:
    if i not in stopwords:
        filtered_words.append(i)

# to create wordcloud of top words
from wordcloud import WordCloud
import matplotlib.pyplot as plt

string = ' '.join(filtered_words)
wc1 = WordCloud(background_color="white", max_words=2000)
wc1.generate(string)
plt.subplot(2, 1, 1)
plt.imshow(wc1)
plt.axis('off')
plt.show()

# to create graphs for top senders
import seaborn as sns

sns.set_style('whitegrid')
fig, ax = sns.plt.subplots(1, 1, figsize=(6,4))
df3[:15].plot(y='count', ax=ax, color='red', alpha=.6)
plt.xlabel("Sender Name")
plt.ylabel("Email Count")

df3[:15].plot(kind='bar', title ="Sender list")
plt.xlabel("Sender Name")
plt.ylabel("Email Count")
plt.show()