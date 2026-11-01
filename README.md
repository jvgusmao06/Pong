# 🏓 Pong Game (Python + PPlay)

Um clássico jogo Pong com mecânicas extras, desenvolvido em Python utilizando a biblioteca de jogos acadêmica **PPlay** (baseada em Pygame), desenvolvido no contexto do curso na UFF (Universidade Federal Fluminense).

---

## 🎮 Sobre o Jogo

O jogo coloca o jogador contra uma inteligência artificial (bot) em uma partida de tênis de mesa/Pong:
- O primeiro jogador a alcançar **10 pontos** vence e a partida é finalizada.
- A cada rodada pontuada, o jogo pausa e aguarda o jogador reiniciar com `Espaço`.
- **Mecânica Extra (Obstáculo Central):** Após 3 colisões com as paredes superiores/inferiores, uma barra neutra surge no centro da tela em uma posição aleatória por tempo limitado, acelerando a bola em colisões e adicionando dinamismo às jogadas!

---

## 🕹️ Controles

| Tecla | Ação |
| :--- | :--- |
| `Seta Para Cima (▲)` | Move a barra do jogador para cima |
| `Seta Para Baixo (▼)` | Move a barra do jogador para baixo |
| `Espaço` | Inicia / recomeça a rodada |
| `ESC` | Fecha o jogo |

---

## 📋 Pré-requisitos

- **Python 3.x** instalado.
- **Pygame** instalado (dependência do framework PPlay).

Instale o Pygame executando no terminal:
```bash
pip install pygame
```

---

## 🚀 Como Executar

1. Clone ou baixe este repositório para o seu computador.
2. Abra o terminal ou prompt de comando na pasta raiz do projeto.
3. Execute o script principal:
   ```bash
   python pong.py
   ```

---

## 📁 Estrutura do Projeto

```text
├── PPlay/            # Módulos da biblioteca gráfica/física PPlay
│   ├── animation.py
│   ├── collision.py
│   ├── gameimage.py
│   ├── keyboard.py
│   ├── window.py
│   └── ...
├── ball.png          # Sprite da bola
├── bar.png           # Sprite da barra (jogadores e obstáculo)
├── pong.py           # Código fonte principal e loop do jogo
└── README.md         # Documentação do projeto
```

---

## 👨‍💻 Autor

Desenvolvido por **João Vitor Gusmão de Souza** para a **UFF** (Universidade Federal Fluminense).

