#Ресторант отваря врати и предлага няколко менюта на преференциални цени:
#•	Пилешко меню –  10.35 лв.
#•	Меню с риба – 12.40 лв.
#•	Вегетарианско меню  – 8.15 лв.
#Напишете програма, която изчислява колко ще струва на група хора да си поръчат храна за вкъщи.
#Групата ще си поръча и десерт, чиято цена е равна на 20% от общата сметка (без доставката).
#Цената на доставка е 2.50 лв и се начислява най-накрая.

chicken_menu = int(input("Брой пилешки менюта: "))
fish_menu = int(input("Брой ribni менюта: "))
vegi_menu = int(input("Брой вегетариански менюта: "))

chicken_menu_sum = chicken_menu * 10.35
fish_menu_sum = fish_menu * 12.40
vegi_menu_sum = vegi_menu * 8.15
total_menu_sum = chicken_menu_sum + fish_menu_sum + vegi_menu_sum
desert_price = total_menu_sum * 0.2
delivery_total = total_menu_sum + desert_price + 2.50
print(delivery_total)