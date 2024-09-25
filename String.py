def contar_letras_a(s):

    contagem = s.count('a')
    contagem_1 = s.count('A')

    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
        print(f"A letra 'A' aparece {contagem_1} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")


texto = input("Informe uma string: ")


contar_letras_a(texto)