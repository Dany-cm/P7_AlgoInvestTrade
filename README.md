# Développer des algorithmes pour AlgoInvest&Trade

Algoinvest&trade cherche à optimiser ses stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients.


<p align="center">
  <img width="460" height="300" src="https://user.oc-static.com/upload/2020/09/18/1600429119334_P6.png">
</p>


## Installation

Python est nécessaire pour faire fonctionner l'application, télécharger le ici : 

[Windows](https://www.python.org/downloads/windows/)

[Linux](https://www.python.org/downloads/source/)

[MacOS](https://www.python.org/downloads/macos/)

## Utilisation

```python
python main.py
```

Le menu suivant apparaît :

```txt
Menu Principal:
1. Force brute
2. Optimisé Naïve        
3. Optimisé Dynamique    
4. Quitter

Sélectionner une option: 
```
Sélectionner l'algorithme souhaité, par exemple 1 est égale à Force brute.

L'application vous demandera de choisir un fichier au format CSV.

```txt
Sélectionner une option: 1
Sélectionner un fichier CSV: 
```
Entré le chemin du fichier et son nom, par exemple :

```txt
Sélectionner un fichier CSV: data/data1.csv
```
L'algorithme analysera votre fichier et une fois terminé, vous aurez une liste de vos résultats avec le bénéfice totale.

```txt
Voici la liste d'action les plus rentable pour un budget maximum de 500€

Action-4 - 70.0 - 20.0% - 14.0
Action-5 - 60.0 - 17.0% - 10.2
Action-6 - 80.0 - 25.0% - 20.0
Action-8 - 26.0 - 11.0% - 2.86
Action-10 - 34.0 - 27.0% - 9.18
Action-11 - 42.0 - 17.0% - 7.14
Action-13 - 38.0 - 23.0% - 8.74
Action-18 - 10.0 - 14.0% - 1.4
Action-19 - 24.0 - 21.0% - 5.04
Action-20 - 114.0 - 18.0% - 20.52

Notre bénéfice total s'élève à 99.08€

Temps d'exécution: 2.31 secondes
```

## Algorithmes utilisés

Force brute : Teste toutes les combinaisons possibles et ne fonctionne que sur un petit nombre d’élément.

Optimisé naïve : Trie par profit et n'ai pas très précis.

Optimisé dynamique : Cherche le meilleur compromis et est très rapide.

## License
[Danycm1](https://github.com/Danycm1)
