# Каждый из N школьников некоторой школы знает Mi языков.
# Определите, какие языки знают все школьники и языки,
# которые знает хотя бы один из школьников.

children = int(input("Количество школьников: "))
languages = []
for i in range(children):
    if i <= children:
        languages_num = int(input("Количество языков школьника: "))
        for j in range(languages_num):
            if j <= languages_num:
                languag = input("Введите языки: ")
                languages.append(languag)
set_languages = set(languages)
languages_all = []
for i in languages:
    if languages.count(i) == children:
        if i not in languages_all:
            languages_all.append(i)
print("Кол-во языков, которые знают все школьники:", len(languages_all))
print("Языки, которые знают все школьники: ", languages_all)
print("Кол-во языков,которые знает хотя бы один школьник:", len(set_languages))
print("Языки, которые знает хотя бы один школьник:", set_languages)
