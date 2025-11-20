def classificar_heroi(xp: int) -> str:
    if xp <= 1000:
        return "Ferro"
    elif xp <= 2000:
        return "Bronze"
    elif xp <= 5000:
        return "Prata"
    elif xp <= 7000:
        return "Ouro"
    elif xp <= 8000:
        return "Platina"
    elif xp <= 9000:
        return "Ascendente"
    elif xp <= 10000:
        return "Imortal"
    else:
        return "Radiante"


def main():
    nome = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de XP: "))

    nivel = classificar_heroi(xp)

    print(f"O Herói de nome {nome} está no nível {nivel}")


if __name__ == "__main__":
    main()
