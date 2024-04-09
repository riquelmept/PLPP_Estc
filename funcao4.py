# script funcao4.py

# captando os valores do campo Input
valores = input()

# separando os valores pelo espaço em branco e
# transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    nova_lista = list(lista)
    nova_lista[2] = nova_lista[2] + 10
    return nova_lista  # Retorna a nova lista alterada


def main():
    # Chama a função altera_lista() duas vezes, mas atribui o resultado da primeira chamada a uma nova variável
    nova_lista_1 = altera_lista(valores)
    nova_lista_2 = altera_lista(nova_lista_1)

    print("Nova lista 1:", nova_lista_1)
    print("Nova lista 2:", nova_lista_2)

if __name__ == "__main__":
    main()