# Atividade: Agenda 6 - Desenvolvimento de Sistemas I
# Objetivo: Calcular desconto progressivo de compras em loja online

# 1. Entrada de dados: leitura do valor da compra
valor_compra = float(input("Informe o valor total da compra (R$): "))

# 2. Estrutura de decisão: definição do percentual de desconto com base nas faixas de valor
if valor_compra < 200.00:
    porcentagem_desconto = 5
    fator_desconto = 0.05
elif valor_compra < 300.00:
    # Como a condição anterior já cobriu valores menores que 200,
    # aqui o valor obrigatoriamente é maior ou igual a 200 e menor que 300.
    porcentagem_desconto = 10
    fator_desconto = 0.10
else:
    # Para compras de R$ 300,00 ou mais
    porcentagem_desconto = 15
    fator_desconto = 0.15

# 3. Processamento: cálculo do desconto e valor final a pagar
valor_desconto = valor_compra * fator_desconto
valor_final = valor_compra - valor_desconto

# 4. Saída de dados: apresentação detalhada dos resultados
print("\n" + "=" * 35)
print("       RESUMO DA COMPRA")
print("=" * 35)
print(f"Valor original da compra : R$ {valor_compra:.2f}")
print(f"Desconto aplicado ({porcentagem_desconto}%): R$ {valor_desconto:.2f}")
print(f"Valor total a pagar      : R$ {valor_final:.2f}")
print("=" * 35)