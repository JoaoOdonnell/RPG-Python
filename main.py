import random

# MONSTROS
lista_monstros = []


def criar_monstro(level):
    novo_monstro = {
        'nome': f"Monstro #{level}",
        'level': level,
        'ataque': 15 * level,
        'defesa': 2 * level,
        'vida': 100 * level,
        'vida_max': 100 * level,
        'exp': 0,
        'exp_max': 10 * level,
    }
    return novo_monstro


def gerar_monstro(n_monstro):
    for x in range(n_monstro):
        monstro = criar_monstro(x + 1)
        lista_monstros.append(monstro)


def exibir_monstros():
    print("\n=== MONSTROS DISPONÍVEIS ===")
    for monstro in lista_monstros:
        mostrar_atributos(monstro)


def mostrar_atributos(personagem):
    print("\n=== ATRIBUTOS ===")
    for chave, valor in personagem.items():
        print(f"{chave}: {valor}")
    print("=============================\n")


# Menu
def menu_principal():
    print("========================")
    print(" Bem vindo ao RPG PIRATA! ")
    print("========================")
    print("Classes disponíveis:\n")
    print("1. MAGO")
    print("2. GUERREIRO")
    print("3. ARQUEIRO")
    escolha_classe = int(input("digite o número da classe para escolher: "))
    jogador = escolha_menu(escolha_classe)
    return jogador


# Função para mostrar a escolha do menu
def escolha_menu(escolha_classe):
    if escolha_classe == 1:
        print("\n=== Você escolheu a classe MAGO! ===")
        mostrar_atributos(classe_mago)
        return classe_mago
    elif escolha_classe == 2:
        print("\n=== Você escolheu a classe GUERREIRO! ===")
        mostrar_atributos(classe_guerreiro)
        return classe_guerreiro
    elif escolha_classe == 3:
        print("\n=== Você escolheu a classe ARQUEIRO! ===")
        mostrar_atributos(classe_arqueiro)
        return classe_arqueiro
    else:
        print("Opção inválida. Tente novamente.")
        return menu_principal()


def iniciar_batalha(jogador):
    print("=" * 15)
    print("Você entrou para uma batalha!")

    # sortear um inimigo
    inimigo = random.choice(lista_monstros)
    print(f"\nUm inimigo {inimigo['nome']} apareceu!")
    mostrar_atributos(inimigo)

    while jogador['vida'] > 0 and inimigo['vida'] > 0:
        print("\n -- SUA VEZ -- ")
        print("1. Atacar")
        print("2. Defender")  # ainda não setado
        acao = input("Escolha uma ação: ")

        if acao == "1":
            dano = jogador['ataque'] - inimigo['defesa']
            if dano < 0:
                dano = 0
            inimigo['vida'] -= dano
            print(f"Você causou {dano} de dano!")
        elif acao == "2":
            print("Você se defendeu! (ainda não setado)")
        else:
            print("Ação inválida")

        # Verificando se o inimigo morreu
        if inimigo['vida'] <= 0:
            print(f"- Você derrotou o inimigo {inimigo['nome']}! - ")
            break

        # TURNO INIMIGO
        print("\n -- VEZ DO INIMIGO --")
        dano_inimigo = inimigo['ataque'] - jogador['defesa']
        if dano_inimigo < 0:
            dano_inimigo = 0
        jogador['vida'] -= dano_inimigo
        print(f"O inimgio {inimigo['nome']} deu {dano_inimigo} de dano!")

        # verificar se o jogdaor morreu
        if jogador['vida'] <= 0:
            print(" -- VOCÊ FOI DERROTADO! -- ")
            break

        # mostrar status atuais
        print(
            f"Sua vida atual: {jogador['vida']} | Vida atual do {inimigo['nome']}: {inimigo['vida']} ")


    # classes
classe_mago = {
    "classe": "Mago",
    "vida": 100,
    "vida_max": 100,
    "ataque": 30,
    "defesa": 7,
    "mana": 100,
    "mana_max": 100,
    'exp': 0,
    'exp_max': 30,
}

classe_guerreiro = {
    "classe": "Guerreiro",
    "vida": 120,
    "vida_max": 120,
    "ataque": 20,
    "defesa": 10,
    "mana": 30,
    "mana_max": 30,
    'exp': 0,
    'exp_max': 30,
}

classe_arqueiro = {
    "classe": "Arqueiro",
    "vida": 90,
    "vida_max": 90,
    "ataque": 40,
    "defesa": 5,
    "mana": 60,
    "mana_max": 60,
    'exp': 0,
    'exp_max': 30,
}

# Função para mostrar os atributos


jogador = menu_principal()
gerar_monstro(3)
exibir_monstros()
iniciar_batalha(jogador)
