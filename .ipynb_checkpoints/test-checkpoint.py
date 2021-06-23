{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "fileName = \"anime_list.csv\"\n",
    "df = pd.read_csv(fileName)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step1 find the top 100 liked aime from the data, regrouping them into a new table in csv format"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "top_100_score_series = df[\"score\"].nlargest(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_based_on_score = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for index, value in top_100_score_series.iteritems():\n",
    "    df_based_on_score = df_based_on_score.append(df.iloc[index, :])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step2 find the most appeared genre of the top 100 liked anime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "genres_dict = {}\n",
    "for i in range(len(df_based_on_score)):\n",
    "    temp_str = df[\"genres\"].iloc[i]\n",
    "    temp_lst = temp_str.split(\", \")\n",
    "    for j in range(len(temp_lst)):\n",
    "        if temp_lst[j] in genres_dict:\n",
    "            genres_dict[temp_lst[j]] += 1\n",
    "        else:\n",
    "            genres_dict[temp_lst[j]] = 1\n",
    "# With a through observation we find people who watch anime enjoy the genres of\n",
    "# \"Action\" -> 45,\n",
    "# \"Comedy\" -> 51,\n",
    "# \"Drama\" -> 55,\n",
    "# \"Sci-fi\" -> 45\n",
    "# the most."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Step3 find which studios are successful in terms of producing top rated anime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "producer_dict = {}\n",
    "for i in range(len(df_based_on_score)):\n",
    "    temp_str = df[\"producers\"].iloc[i]\n",
    "    temp_lst = temp_str.split(\", \")\n",
    "    for j in range(len(temp_lst)):\n",
    "        if temp_lst[j] in producer_dict:\n",
    "            producer_dict[temp_lst[j]][0] += 1\n",
    "        else:\n",
    "            producer_dict[temp_lst[j]] = [1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "producer_dataframe = pd.DataFrame.from_dict(producer_dict)\n",
    "producer_series = producer_dataframe.iloc[0].squeeze()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(producer_series.nlargest())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Result of above command:<br>\n",
    "Bandai Visual     16<br>\n",
    "Sotsu             14<br>\n",
    "TV Tokyo Music    12<br>\n",
    "TV Tokyo          10<br>\n",
    "Fuji TV            9"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
