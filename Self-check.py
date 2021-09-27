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


print("2021 F1 Drivers")
print("=============== \n")
list_drivers = open("Drivers.txt", "r")
drivers = list_drivers.read()
driver_list = drivers.split(',')
last_name_sort = (sorted(driver_list, key = lambda x: x.split()[-1]))
driver_number_sort = (sorted(driver_list, key = lambda x: x.split()[1]))

print (last_name_sort, '\n')
print (driver_number_sort)
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
