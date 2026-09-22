# Name: Yashvi Himanshu Gaglani
# Andrew ID: ygaglani
# solution 1
with open('movies.tsv', 'r') as f:
    movieList = []
    for line in f:
        fields = line.strip().split('\t')
        movie = {
            "id": fields[0],
            "name": fields[1].strip('"'),
            "year": int(fields[2]),
            "country": fields[3].strip('"'),
            "genres": [genre.strip() for genre in fields[4:]]
        }
        movieList.append(movie)
    # a - total number of movies
    print("Total number of movies:", len(movieList))

    # b - print first 5 movies
    print("First 5 movies:", movieList[:5])

    # c - print oldest movie 
    oldest_movie = min(movieList, key=lambda x: x['year'])
    print("Oldest movie:", oldest_movie)

    # d - print newest movie
    newest_movie = max(movieList, key=lambda x: x['year'])  
    print("Newest movie:", newest_movie)


# solution 2
def createMovieDictionary(filename: str) -> dict:

    movieDict = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            fields = line.split('\t')
            movieId = fields[0]
            title = fields[1]
            year = fields[2]
            country = fields[3]
            genres = [g for g in fields[4:] if g]

            movieDict[title] = {
                'id': movieId,
                'year': year,
                'country': country,
                'genre': genres
            }
    return movieDict


filename = "movies.tsv"
movieDict = createMovieDictionary(filename)

while True:
    title = input("Enter a movie title (or 'Done' to quit): ")
    if title == 'Done':
        break
    if title in movieDict:
        info = movieDict[title]
        print(f"Title: {title}")
        for key, value in info.items():
            print(f"  {key.capitalize()}: {value}")
    else:
        print("Not found")

# 3. Create a set named genreSet. Read the file and insert every genre into the set. After processing the file:
# a. Display the total number of unique genres.
# b. Convert the set into a sorted list named genreList.
# c. Display all genres alphabetically.
# d. Display the first and last genre alphabetically.

# solution 3
genreSet = set()
with open("movies.tsv", "r") as f:
    for line in f:
        fields = line.strip().split('\t')
        for genre in fields[4:]:
            if genre:
                genreSet.add(genre)
# a
print("Total number of unique genres:", len(genreSet))

# b
genreList = sorted(list(genreSet))
print("All genres alphabetically:", genreList)

# c
print("First genre alphabetically:", genreList[0])

# d
print("Last genre alphabetically:", genreList[-1])


# solution 4
yearDict = {}
with open("movies.tsv", "r") as f:
    for line in f:
        fields = line.strip().split('\t')
        year = fields[2]
        title = fields[1].strip('"')
        if year not in yearDict:
            yearDict[year] = []
        yearDict[year].append(title)

# a
print("Number of unique years:", len(yearDict))

# b
busiest_year = max(yearDict, key=lambda y: len(yearDict[y]))
print("Year with the most movies:", busiest_year)

# c
print("First ten movies from that year:", yearDict[busiest_year][:10])

# d
while True:
    year = input("Enter a year (or 0 to quit): ")
    if year == '0':
        break
    if year in yearDict:
        print(f"Movies from {year}:", yearDict[year])
    else:
        print("Not found")