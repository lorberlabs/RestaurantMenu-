print "Dear guest here comes our menu!"

day_menu = {}

while True:
    dish = raw_input("Please enter the name of the dish ")
    price = raw_input("Please enter the price of the dish ")
    day_menu[dish] = price

    print "Dish " + dish + " costs " + price + " EUR"

    new = raw_input("Do you wanna enter a new dish (Yes / NO) ")

    if new.lower() == "no".lower() :
        break

menu_file = open("menu.txt", "w+")
menu_file.write("Menu: \n")
for dish in day_menu:
    menu_file.write("The dish %s costs %s EUR\n" % (dish, day_menu[dish]))

print "Day menu: %s" % day_menu

print "THE END"