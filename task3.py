"""
Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список сворачивает.
"""
def get_ranges(number_list):

    zone_one = list(filter(lambda x: x <= 4, number_list))
    zone_two = list(filter(lambda x: x >= 5 and x <= 6, number_list))
    zone_three = list(filter(lambda x: x >= 7 and x <= 9, number_list))
    zone_four = list(filter(lambda x: x >= 10, number_list))
    if len(zone_one) != 0:
        if len(zone_one) == 1:
            print(zone_one)
        else:
            print(min(zone_one), "-", max(zone_one))
    if len(zone_two) != 0:
        if len(zone_two) == 1:
            print(zone_two)
        else:
            print(min(zone_two)), "-", max(zone_two)
    if len(zone_three) != 0:
        if len(zone_three) == 1:
            print(zone_three)
        else:
            print(min(zone_three), "-", max(zone_three))
    if len(zone_four) != 0:
        if len(zone_four) == 1:
            print(zone_four)
        else:
            print(min(zone_four), "-", max(zone_four))

get_ranges([2, 4, 10])