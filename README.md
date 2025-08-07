# 🏴‍☠️ RPG Pirata em Python

Projeto desenvolvido como prática de lógica de programação com Python, utilizando estruturas como funções, dicionários, laços de repetição e entrada de dados. Neste jogo simples de RPG por texto, o jogador escolhe uma classe e enfrenta monstros aleatórios em batalhas por turnos.

## 🎮 Funcionalidades

- Escolha entre 3 classes:
  - Mago 🧙‍♂️
  - Guerreiro ⚔️
  - Arqueiro 🏹
- Geração aleatória de monstros com níveis diferentes
- Sistema de atributos (vida, ataque, defesa, mana, experiência)
- Lógica de combate por turnos (atacar, receber dano)
- Exibição dos status atuais do jogador e do inimigo
- Sistema de derrota e vitória

## 🧠 Conceitos aplicados

- Funções
- Dicionários
- Listas
- Estruturas condicionais (`if`, `elif`, `else`)
- Laços de repetição (`for`, `while`)
- Importação de biblioteca (`random`)
- Modularização de código (funções organizadas por responsabilidade)

## 🗂️ Estrutura do código

- `menu_principal()` → Exibe o menu inicial e retorna o personagem escolhido
- `escolha_menu()` → Retorna os atributos da classe escolhida
- `gerar_monstro()` → Cria monstros com atributos escaláveis por nível
- `iniciar_batalha()` → Controla o fluxo do combate
- `mostrar_atributos()` → Mostra os atributos do personagem ou monstro

## 🚀 Como rodar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
3. Acesse a pasta do projeto:
    ```bash
   cd Projeto-Jogo_RPG_Python

   
4. Execute o jogo:
    ```bash
    python main.py