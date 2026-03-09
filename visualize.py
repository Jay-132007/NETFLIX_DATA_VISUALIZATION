import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)

df=pd.read_csv(r'C:\Users\Nadkarni Omkar\OneDrive\Desktop\AI_ML journey\data cleaning\data visualization\netflix_dirty_1200_rows.csv')


# clean data 
print(df.shape)
df=df.dropna(subset=['type','release_year','rating','country','duration'])
print(df.shape)

# tv show vs movie
type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=['orange','blue'])
plt.title("no. of TV SHOWS vs MOVIE")
plt.xlabel('type')
plt.ylabel('count')
plt.tight_layout()
plt.savefig('tvshow_vs_movie.png')
plt.show()

# pie chart for rating
rating_count=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title("percentage of content RATING")
plt.tight_layout()
plt.savefig('rating_pie.png')
plt.show()

# duration of movie 
movie_df=df[df['type']=='Movie'].copy()
movie_df = movie_df[movie_df['duration'].str.contains('min', na=False)]
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)
plt.hist(movie_df['duration_int'],bins=5,color='purple',edgecolor='black')
plt.title("distribution of movie duration")
plt.xlabel('duration in minutes')
plt.ylabel('no. of movies')
plt.tight_layout()
plt.savefig('duration_histogram.png')
plt.show()


# release year vs no. of shows 
release_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_count.index,release_count.values,color='green')
plt.title("release year vs no. of shows ")
plt.xlabel("release year")
plt.ylabel("no. of shows")
plt.tight_layout()
plt.savefig('release_scatter.png')
plt.show()



# country count (bar - horizntal)
country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='green')
plt.title("top 10 countries by no. of shows ")
plt.xlabel("No. of shows ")
plt.ylabel("country")
plt.tight_layout()
plt.savefig('country_barh.png')
plt.show()


# subplots 
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# Second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Years')

plt.tight_layout()
plt.savefig("movies_vs_tvshows.png")
plt.show()


