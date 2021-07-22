"""
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся
в файле ./data_hw5/ ratings.txt.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""
from collections import Counter
import json

result_movies = []
result_years = []
result_levels = []
try:
    with open('ratings.txt') as rating_txt:
        for i, line in enumerate(rating_txt):
            if 28 <= i <= 278:
                result_levels.append((line[27:32]).strip())
                result_years.append((line[-6:-2]).strip())
                result_movies.append((line[32:-7]).strip())

    bar_graph_levels = Counter(result_levels)
    bar_graph_years = Counter(result_years)

    with open("top250_movies.txt", "w") as top250:
        json.dump(result_movies, top250, indent="\n")

    with open("levels250.txt", "w") as levels:
        json.dump(bar_graph_levels, levels, indent="\n")

    with open("years250.txt", "w") as years:
        json.dump(bar_graph_years, years, indent="\n")


except FileNotFoundError:
    print("Файл не найден")
