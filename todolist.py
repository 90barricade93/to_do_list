# todo lijst 2023
# Voor educatieve doeleinden

# 1. initialiseer een leeg lijstje om taken in op te slaan
tasks = []

# 2. Loop het programma tot de gebruiker 'stop' ingeeft
while True:
    # toon de menu opties
    print()
    print("Menu:")
    print("1. toon taken")
    print("2. voeg een taak toe")
    print("3. verwijder een taak")
    print("4. verplaats een taak naar boven")
    print("5. verplaats een taak naar beneden")
    print("6. stop")
    print()

    # vraag de gebruiker om een keuze
    choice = input("Wat wil je doen? ")

    # toon de taken
    if choice == "1":
        print("Taken:")
        for task in tasks:
            print(task)

    # voeg een taak toe
    elif choice == "2":
        task = input("Geef een taak in: ")
        tasks.append(task)

    # verwijder een taak
    elif choice == "3":
        task = input("Welke taak wil je verwijderen? (typ de taak in!)")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Taak niet gevonden")

    # verplaats een taak naar boven
    elif choice == "4":
        task = input("Welke taak wil je naar boven verplaatsen? (typ de taak in!)")
        if task in tasks:
            index = tasks.index(task)
            if index > 0:
                tasks[index], tasks[index-1] = tasks[index-1], tasks[index]
            else:
                print("Taak kan niet naar boven verplaatst worden")
        else:
            print("Taak niet gevonden")

    # verplaats een taak naar beneden
    elif choice == "5":
        task = input("Welke taak wil je naar beneden verplaatsen? (typ de taak in!)")
        if task in tasks:
            index = tasks.index(task)
            if index < len(tasks) - 1:
                tasks[index], tasks[index+1] = tasks[index+1], tasks[index]
            else:
                print("Taak kan niet naar beneden verplaatst worden")
        else:
            print("Taak niet gevonden")

    # stop het programma
    elif choice == "6":
        break

    # ongeldige keuze
    else:
        print("Ongeldige keuze")

# 3. toon de taken
print("Taken:")
for task in tasks:
    print(task)

# 4. stop het programma
print("Tot ziens!")

# Einde programma
