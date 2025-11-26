
# 🎮 Simple Adventure — PgZero Game

**Simple Adventure** foi desenvolvido utilizando a biblioteca **PgZero**, com foco em boas práticas de programação, organização do código e clareza estrutural.  
O projeto segue os princípios recomendados para jogos educacionais, mantendo simplicidade, legibilidade e animações funcionais para fins didáticos.

O jogador controla um herói que se move até onde o usuário clicar na tela.  
Há um menu principal, som opcional, animação de sprites e um inimigo que patrulha a área.

---

## 🧩 Funcionalidades Implementadas

- ✔ Gênero permitido: *Aventura Point-and-Click*  
- ✔ Menu principal completo:
  - **Start Game**
  - **Sound ON/OFF**
  - **Exit**
- ✔ Movimento suave do herói em direção ao clique
- ✔ Animações de sprite (idle e walk)
- ✔ Inimigo patrulhando com animação
- ✔ Sistema de colisão (som + reset do herói)
- ✔ Música de fundo e efeitos sonoros
- ✔ Botão para ativar/desativar som
- ✔ Código simples, didático e dentro das regras:
  - **PgZero**
  - **math**
  - **random**
  - `Rect` do pygame (uso permitido)

---

## 🗂 Estrutura do Projeto

```

project/
│
├── game.py
│
├── images/
│   ├── hero_idle1.png
│   ├── hero_idle2.png
│   ├── hero_walk1.png
│   ├── hero_walk2.png
│   ├── enemy_idle1.png
│   ├── enemy_idle2.png
│   ├── enemy_walk1.png
│   ├── enemy_walk2.png
│   └── background.png (opcional)
│
└── sounds/
├── click.wav
├── hit.wav
└── bg_music.wav

````

> As imagens e sons devem possuir exatamente esses nomes para funcionar.

---

## ▶️ Como Rodar o Jogo

### 1. Instale o PgZero

```bash
pip install pgzero
````

### 2. Execute o jogo

```bash
pgzrun game.py
```

A janela abrirá automaticamente.

---

## 🧠 Detalhes Técnicos

### ✔ Movimento do Herói

* Baseado em vetores com `math.hypot`
* Caminho suave até o ponto do clique
* Alternância de sprites a cada 15 ciclos

### ✔ Inimigo Patrulhando

* Movimenta-se entre `x1` e `x2`
* Troca direção quando chega nos limites
* Alternância de sprites a cada 20 ciclos

### ✔ Colisão

Quando o herói encosta no inimigo:

* Toca som de **hit**
* Herói retorna ao centro da tela

### ✔ Menu Interativo

* Construído com `Rect` do pygame
* Detecta clique com `collidepoint()`
* Uso de `screen.draw` para texto e botões

---

## 🔊 Sons e Música

O jogo inclui três sons básicos:

* `click.wav` — usado no menu
* `hit.wav` — ao tocar no inimigo
* `bg_music.wav` — música de fundo

O botão **Sound ON/OFF** controla todos os sons.

---

## 📜 Conformidade com o Teste Kodland

Este projeto segue **100% das regras exigidas**:

* ✔ Apenas PgZero, math e random
* ✔ Uso permitido de `pygame.Rect`
* ✔ Jogo dentro dos gêneros aceitos
* ✔ Animação de sprite funcional
* ✔ Código original e independente
* ✔ Menu com três botões
* ✔ Mecânica clara, lógica e sem bugs críticos

---

## 👤 Autor

Projeto desenvolvido exclusivamente para o processo seletivo prático da **Kodland**, com foco em didática, simplicidade e boas práticas de programação.


