menu = []

menu.append(["egg", "bacon", "spam"])
menu.append(["bacon", "egg", "sausage"])
menu.append(["bacon", "spam", "spam"])
menu.append(["egg", "spam", "bacomn", "spam"])
menu.append(["spam", "spam", "spam"])
menu.append(["bacon", "egg", "spam"])

for meal in menu:
    if not "spam" in meal:
        for dish in meal:
            print(dish)

