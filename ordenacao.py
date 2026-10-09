def quick_sort(valores):
    if len(valores) <= 1:
        return valores
    else:
        menores = []
        maiores = []
        iguais = []
        pivo = valores[0]
        for n in valores:
            if n < pivo:
                menores.append(n)
            elif n > pivo:
                maiores.append(n)
            else:
                iguais.append(n)
        print(f"Menores: {menores}, Maiores: {maiores}, Iguais: {iguais}")
        return quick_sort(menores) + iguais + quick_sort(maiores)
#                      
print(quick_sort([5, 3,8, 6, 2, 7,5, 4, 1,]))
