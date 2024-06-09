import pandas as pd
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import squarify
from IPython.display import display
df = pd.read_csv("netflix_titles.csv")
#print(df.head())
show_id = df['show_id'].tolist()
typee = df['type'].tolist()
title = df['title'].tolist()
director = df['director'].tolist()
cast = df['cast'].tolist()
country = df['country'].tolist()
date_added = df['date_added'].tolist()
release_year = df['release_year'].tolist()
rating = df['rating'].tolist()
duration = df['duration'].tolist()
listed_in = df['listed_in'].tolist()
description = df['description'].tolist()
# Display the first few elements of each list
"""print("show_id:", show_id[:5])
print("type:", typee[:5])
print("title:", title[:5])
print("director:", director[:5])
print("cast:", cast[:5])
print("country:", country[:5])
print("date_added:", date_added[:5])
print("release_year:", release_year[:5])
print("rating:", rating[:5])
print("duration:", duration[:5])
print("listed_in:", listed_in[:5])
print("description:", description[:5])"""
value_counts = Counter(listed_in)
most_common, least_common =[],[]
for elem in range (len(value_counts.most_common())):
    if value_counts.most_common()[elem][1]==value_counts.most_common()[0][1]:
        most_common.append(value_counts.most_common()[elem][0])
    elif value_counts.most_common()[elem][1]==value_counts.most_common()[-1][1]:
        least_common.append(value_counts.most_common()[elem][0])





#--------------------------------------------Some Basic Interpretations--------------------------------------------------------------------------------------------------

print("total number of show recorded in the dataset:",len(show_id))
print("most common type of the shows:",max(typee))
print("list of shows with most common genre:",most_common)
print("\n")
print("list of shows with least common genre:",least_common)
print("\n")
print(f"most common genre of the shows is almost {round((value_counts.most_common()[0][1])/len(show_id)*100,2)}%")
print(f"least common genre of the shows is almost {round((value_counts.most_common()[-1][1])/len(show_id)*100,2)}%")
"""for value, count in value_counts.items():
    print(f"{value}: {count}")"""


#-------------------------------------------Analyzing availability of movie released over Years-------------------------------------------------------------------------


ll=Counter(release_year).most_common()
"""for i in range(len(ll)):
    print(f"Total number of movies available in Netflix that was released in the year {ll[i][0]} is {ll[i][1]}")"""
df_release_year_counts = pd.DataFrame(ll, columns=['Release Year', 'Number of Movies'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Release Year', y='Number of Movies', data=df_release_year_counts, palette='viridis',hue='Release Year', legend=False)
plt.xlabel('Release Year',fontsize=12, fontweight='bold', color='blue')
plt.ylabel('Number of Movies',fontsize=12, fontweight='bold', color='blue')
plt.title('Movie release year VS availability',fontsize=12, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# old movies are less available in Netflix. 




#--------------------------------------------categorizing the movies based on the given description---------------------------------------------------------









#-------------------------------------------Web_series VS Other_shows---------------------------------------------------------------------------

tt=Counter(duration).most_common()

print(tt)  # This is a list containing duration vs total number of shows that provides web-series with 1 season is maximum in number (1793) 
           # where as shows which are longer than 3 hrs are very less in numbers 
webseries, others,s1,s2=[],[],0,0
for i in range(len(tt)):
    if 'Seasons' in tt[i][0] or 'Season' in tt[i][0] or 'season' in tt[i][0] or 'seasons' in tt[i][0]:
        s1+=tt[i][1]
        webseries.append(tt[i])
    else:
        s2+=tt[i][1]
        others.append(tt[i])
print('total number of webseries', s1)
print('total number of 1-time show',s2)
categories = ['Web Series', 'Other Shows']
values = [s1, s2]
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
colors = sns.color_palette('muted')
wedges, texts, autotexts = ax.pie(values, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)
# Adjust parameters for a 3D-like appearance
for w in wedges:
    w.set_linewidth(2)
    w.set_edgecolor('white')
plt.title('Comparison of Web Series and Other Shows', fontsize=12, fontweight='bold', color='red')
plt.show()

# mostly one timer shows are available in Netflix which is more than double of total webseries




#----------------------------------------analyzing any trends with movie producing countries----------------------------------------------------------------------------------


cc_=Counter(country).most_common()
print("Top 10 movie producing coutries from the dataset")
print("\n")
for i in range(11):
    if cc_[i][0]=='Unknown':
        print(f"Country name not provided: {cc_[i][1]}")
    else:
        print(f"{cc_[i][0]}: {cc_[i][1]}")

#Top 10 movie producing countries from the dataset 

"""
United States: 2818
India: 972
Country name not provided: 831
United Kingdom: 419
Japan: 245
South Korea: 199
Canada: 181
Spain: 145
France: 124
Mexico: 110

"""


#---------------------------------------------------analyze if there's a relationship between the release year of a show and its duration------------------------------


movies = []
web_series = []

# Iterate over each item in duration and release_year lists
for year, dur in zip(release_year, duration):
    if 'min' in dur:  # Check if duration contains 'min'
        movies.append((year, dur))
    elif 'Season' in dur or 'Seasons' in dur:  # Check if duration contains 'Season' or 'Seasons'
        web_series.append((year, dur))

#print("Movies:", movies)
#print("Web Series:", web_series)

from collections import defaultdict
# Initialize dictionaries to store total duration and count of movies/web series for each year
movie_data = defaultdict(list)
web_series_data = defaultdict(list)

# Iterate over each item in duration and release_year lists
for year, dur in zip(release_year, duration):
    if 'min' in dur:  # Check if duration contains 'min'
        movie_data[year].append(int(dur.split()[0]))  # Extract duration in minutes and convert to integer
    elif 'Season' in dur or 'Seasons' in dur:  # Check if duration contains 'Season' or 'Seasons'
        web_series_data[year].append(int(dur.split()[0]))  # Extract number of seasons and convert to integer

# Calculate average duration for each year
movies = [(year, round((sum(durations) / len(durations)),2)) for year, durations in movie_data.items()]
web_series = [(year, round((sum(durations) / len(durations)),2)) for year, durations in web_series_data.items()]

print("Average Movie Durations:", movies)
print("Average Web Series Durations:", web_series)


df_mm_counts = pd.DataFrame(movies, columns=['Release Year', 'Duration'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Release Year', y='Duration', data=df_mm_counts, palette='viridis',hue='Release Year', legend=False)
plt.xlabel('Release Year',fontsize=12, fontweight='bold', color='blue')
plt.ylabel('Duration (min)',fontsize=12, fontweight='bold', color='blue')
plt.title('Release year VS Duration (Movies)',fontsize=12, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

df_web_counts = pd.DataFrame(web_series, columns=['Release Year', 'Duration'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Release Year', y='Duration', data=df_web_counts, palette='viridis',hue='Release Year', legend=False)
plt.xlabel('Release Year',fontsize=12, fontweight='bold', color='blue')
plt.ylabel('Number of seasons',fontsize=12, fontweight='bold', color='blue')
plt.title('Release year VS Duration (Web Series)',fontsize=12, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#----------------------------analyze if there's a difference in the distribution of content ratings between movies and TV shows---------------------------------------


a,b=[],[]
for i in range(len(typee)):
    if typee[i]=='TV Show':
        a.append(rating[i])
    else:
        b.append(rating[i])

tv_show=Counter(a).most_common()
movv=Counter(b).most_common()

df_tvv_counts = pd.DataFrame(tv_show, columns=['Rating', 'Number of Shows'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Rating', y='Number of Shows', data=df_tvv_counts, palette='viridis',hue='Rating', legend=False)
plt.xlabel('Rating',fontsize=12, fontweight='bold', color='blue')
plt.ylabel('Number of Shows',fontsize=12, fontweight='bold', color='blue')
plt.title('Number of shows VS rating (for TV show)',fontsize=12, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

df_movv_counts = pd.DataFrame(movv, columns=['Rating', 'Number of Shows'])
plt.figure(figsize=(10, 6))
sns.barplot(x='Rating', y='Number of Shows', data=df_movv_counts, palette='viridis',hue='Rating', legend=False)
plt.xlabel('Rating',fontsize=12, fontweight='bold', color='blue')
plt.ylabel('Number of Shows',fontsize=12, fontweight='bold', color='blue')
plt.title('Number of shows VS rating (for Movies)',fontsize=12, fontweight='bold', color='red')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
