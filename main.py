from bruteforce import bruteforce
from optimized import optimized
from optimized_dynamic import optimized_dynamic

from file import get_info_from_file
import timeit

def Menu():
    print('Menu Principal:')
    print('1. Force brute')
    print('2. Optimisé')
    print('3. Optimisé Dynamique')
    print('4. Quitter')

while True:
    Menu()
    try:
        choice = int(input('Sélectionner une option: '))
        if choice == 1:
            choice = input('Sélectionner un fichier CSV: ')
            start = timeit.default_timer()
            result = bruteforce(500, get_info_from_file(choice))
            end_time = round(timeit.default_timer() - start, 2)
            print(f"Voici la liste d'action les plus rentable pour un budget maximum de 500€", '\n')
            for action in result[1]:
                print(action)

            print(f"Notre bénéfice total s'élève à {result[0]}€", '\n')
            print(f"Temps d'exécution: {end_time} secondes", '\n')
        if choice == 2:
            choice = input('Sélectionner un fichier CSV: ')
            start = timeit.default_timer()
            result = optimized(500, get_info_from_file(choice))
            end_time = round(timeit.default_timer() - start, 2)
            print(f"Voici la liste d'action les plus rentable pour un budget maximum de 500€", '\n')
            for action in result[1]:
                print(action)
            print(f"Notre bénéfice total s'élève à {result[0]}€", '\n')
            print(f"Temps d'exécution: {end_time} secondes", '\n')
        if choice == 3:
            choice = input('Sélectionner un fichier CSV: ')
            start = timeit.default_timer()
            result = optimized_dynamic(500, get_info_from_file(choice))
            end_time = round(timeit.default_timer() - start, 2)
            print(f"Voici la liste d'action les plus rentable pour un budget maximum de 500€", '\n')
            for action in result[1]:
                print(action)
            print(f"Notre bénéfice total s'élève à {result[0]}€", '\n')
            print(f"Temps d'exécution: {end_time} secondes", '\n')
        if choice == 4:
            quit()
    except ValueError:
        print("Sélectionner un numéro valide")
