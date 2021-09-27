# list_drivers = open("Drivers.txt", "r")
# def last_name(list_drivers):
#     sorted_names = []

#     for element in list_drivers:
#         sorted_names.append(element.split())
#     list_drivers = []

#     for element in sorted(sorted_names, key = lambda x: x[-1]):
#         list_drivers.append(' '.join(element))
#     return list_drivers

#     print('\n2021 F1 Drivers\n', '===============', last_name(list_drivers))
drivers = [['Max', 'Verstapen', 33, 'Red Bull'], 
           ['Lewis', 'Hamilton', 44, 'Mercedes'],
           ['Valtteri', 'Bottas', 77, 'Mercedes'],
           ['Lando', 'Norris', 4, 'McLaren'],
           ['Sergio', 'Perez', 11, 'Red Bull'],
           ['Charles', 'Leclerc', 16, 'Ferrari'],
           ['Carlos', 'Sainz', 55, 'Ferrari'],
           ['Daniel', 'Ricciardo', 3, 'McLaren'],
           ['Pierre', 'Gasly', 10, 'AlphaTauri'],
           ['Fernando', 'Alonso', 14, 'Alpine'],
           ['Esteban', 'Ocon', 31, 'Alpine'],
           ['Sebastian', 'Vettel', 5, 'Aston Martin'],
           ['Lance', 'Stroll', 18, 'Aston Martin'],
           ['Yuki', 'Sonoda', 22, 'AlphaTauri'],
           ['George', 'Russell', 63, 'Williams'],
           ['Nicholas', 'Latifi', 6, 'Williams'],
           ['Kimi', 'Raikkonen', 7, 'Alfa Romeo'],
           ['Antonio', 'Giovinazzi', 99, 'Alfa Romeo'],
           ['Mick', 'Schumacher', 47, 'Haas'],
           ['Nikita', 'Mazepin', 9, 'Haas']]

print("2021 F1 Drivers - Alphabetical")
print("============================== \n")
def last_key(driver):
    return driver[1]

drivers.sort(key = last_key, reverse = False)
print(drivers)
# list_drivers = open("Drivers.txt", "r")
# drivers = list_drivers.read()
# driver_list = drivers.split(',')
# last_name_sort = (sorted(driver_list, key = lambda x: x.split()[-1]))
# with open('Drivers.txt') as drivers_list:
#    driver_list = [driver.split() for driver in drivers_list]
#    driver_number_sort = driver_list.sort(key=lambda s: s[2:3])
# driver_number_sort = (sorted(driver_list, key = lambda s: s.split()[2:3]))

# print (last_name_sort, '\n')
print("2021 F1 Drivers - Driver Number")
print("=============================== \n")
def number_key(driver):
    return driver[2]
drivers.sort(key = number_key, reverse = False)
print(drivers)
# print (driver_number_sort)
# sort Drivers.txt by last name
# sort Drivers.txt by racing number
# if name = Lewis Hamilton print "YEET!"

# driver_list = drivers.split(' ')
# drivers_list = driver_list
# list_drivers.close()
# print(drivers_list)



# list_drivers = open("Drivers.txt").readlines()
# print(list_drivers)
# driver_list = list_drivers.split(',')
# drivers_list = driver_list
# list_drivers.close()
# print(drivers_list)
