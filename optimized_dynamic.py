def optimized_dynamic(capacite, elements):
    capaciteformatrice = capacite * 100
    matrice = [[0 for x in range(capaciteformatrice + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capaciteformatrice + 1):
            if elements[i-1].priceformatrice <= w:
                matrice[i][w] = max(elements[i-1].benefice + matrice[i-1][w-elements[i-1].priceformatrice], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capaciteformatrice
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e.priceformatrice] + e.benefice:
            elements_selection.append(e)
            w -= e.priceformatrice

        n -= 1

    return matrice[-1][-1], elements_selection