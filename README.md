# Sistema de Desconto Progressivo - Agenda 06

Atividade prática desenvolvida para a disciplina de **Desenvolvimento de Sistemas I (DS I)** do curso Técnico em Desenvolvimento de Sistemas da ETEC.

---

## 📌 Descrição do Projeto

O objetivo deste programa em Python é simular um sistema de desconto progressivo para uma loja virtual. O software recebe o valor total da compra inserido pelo usuário e determina automaticamente a porcentagem de desconto aplicável de acordo com as seguintes faixas:

* **Compras abaixo de R$ 200,00:** 5% de desconto.
* **Compras entre R$ 200,00 e R$ 299,99:** 10% de desconto.
* **Compras a partir de R$ 300,00:** 15% de desconto.

Ao final, o programa exibe um resumo detalhado contendo o valor original, o desconto concedido (em porcentagem e em reais) e o total final a ser pago pelo cliente.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Conceitos aplicados:** Entrada e saída de dados formatada, conversão de tipos primitivos (`float`), operadores aritméticos e estruturas condicionais encadeadas (`if / elif / else`).

---

## 🚀 Como Executar

1. Certifique-se de ter o Python instalado em seu computador.
2. Clone o repositório ou faça download do arquivo `GabrielMoraisMarcondes_Ag6_DS_I.py`.
3. Abra o terminal na pasta do arquivo e execute:

```bash
python GabrielMoraisMarcondes_Ag6_DS_I.py

🧪 Evidências de Teste

Os testes foram realizados cobrindo os três cenários de negócio previstos no enunciado:

**Cenário 1 (Menor que R200,00):∗∗CompradeR 150.00 com 5% de desconto (R7.50)→Total:R 142.50.
Cenário 2 (Entre R200,00eR 299,99): Compra de R250.00com10 25.00) → Total: R$ 225.00.
**Cenário 3 (A partir de R300,00):∗∗CompradeR 300.00 com 15% de desconto (R45.00)→Total:R 255.00.

👤 Autor
Aluno: [Gabriel Morais Marcondes]
Curso: Técnico em Desenvolvimento de Sistemas - ETEC
Componente Curricular: Desenvolvimento de Sistemas I (DS I) - Agenda 06

### Dica rápida para a imagem no GitHub:
Coloque o arquivo de imagem na mesma pasta do repositório com o nome `image.png` (ou ajuste o caminho caso decida colocar dentro de uma pasta como `assets/` ou `img/`). Assim o GitHub carregará a imagem diretamente na página inicial do projeto.
