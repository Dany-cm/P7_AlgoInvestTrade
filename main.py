from bruteforce import bruteforce, get_info_from_file
import time

def Menu():
    print('Main Menu:')
    print('1. Bruteforce')
    print('2. Optimized')
    print('3. Quit')

while True:
    Menu()
    try:
        choice = int(input('Select an option: '))
        if choice == 1:
            start = time.time()
            result = bruteforce(500, get_info_from_file(input('Select a CSV file: ')))
            print(f"Voici la liste d'action les plus rentable {result[1]} pour un budget maximum de 500€, notre bénéfice total s'élève à {result[0]} €")
            end = time.time()
            print(f"Temps d'exécution: {end - start} secondes")
        if choice == 2:
            print('NYI')
        if choice == 3:
            quit()
    except ValueError:
        print("You must enter a number from the menu")

