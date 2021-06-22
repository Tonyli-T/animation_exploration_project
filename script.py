import pandas as pd

fileName = "anime_list.csv"
df = pd.read_csv(fileName)

# Step1 find the top 100 liked aime from the data, regrouping them into a new table in csv format
top_100_score_series = df["score"].nlargest(100)

df_based_on_score = pd.DataFrame()

for index, value in top_100_score_series.iteritems():
    df_based_on_score = df_based_on_score.append(df.iloc[index, :])

# Step2 find the most appeared genre of the top 100 liked anime
genres_dict = {}
for i in range(len(df_based_on_score)):
    temp_str = df["genres"].iloc[i]
    temp_lst = temp_str.split(", ")
    for j in range(len(temp_lst)):
        if temp_lst[j] in genres_dict:
            genres_dict[temp_lst[j]] += 1
        else:
            genres_dict[temp_lst[j]] = 1
# With a through observation we find people who watch anime enjoy the genres of
# "Action" -> 45,
# "Comedy" -> 51,
# "Drama" -> 55,
# "Sci-fi" -> 45
# the most.

# Step3 find which studios are successful in terms of producing top rated anime
producer_dict = {}
for i in range(len(df_based_on_score)):
    temp_str = df["producers"].iloc[i]
    temp_lst = temp_str.split(", ")
    for j in range(len(temp_lst)):
        if temp_lst[j] in producer_dict:
            producer_dict[temp_lst[j]][0] += 1
        else:
            producer_dict[temp_lst[j]] = [1]

producer_dataframe = pd.DataFrame.from_dict(producer_dict)
producer_series = producer_dataframe.iloc[0].squeeze()

print(producer_series.nlargest())

# Result of above command:
# Bandai Visual     16
# Sotsu             14
# TV Tokyo Music    12
# TV Tokyo          10
# Fuji TV            9