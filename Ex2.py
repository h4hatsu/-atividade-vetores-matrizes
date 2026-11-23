produtos = ["camisetas", "canecas", "bonés"]
periodos = ["dia 1 | manhã", "dia 1 | tarde", "dia 2 | manhã", "dia 2 | tarde"]
vendas = []

for a in range(3):
    linha = []
    for b in range(4):
        qtd = -1
        while qtd < 0:
            qtd = int(input(f"digite a quantidade de {produtos[a]} vendidos/vendidas - ({periodos[b]}): "))
            if qtd < 0:
                print("|a quantidade não pode ser negatva|")
        linha.append(qtd)
    vendas.append(linha)

total_prod = [0, 0, 0]
total_period = [0, 0, 0, 0]
total_geral = 0

for a in range(3):
    for b in range(4):
        valor = vendas[a][b]
        total_prod[a] = total_prod[a] + valor
        total_period[b] = total_period[b] + valor
        total_geral = total_geral + valor

maior_venda_prod = 0
for a in range(1, 3):
    if total_prod[a] > total_prod[maior_venda_prod]:
        maior_venda_prod = a

maior_venda_period = 0
for b in range(1, 4):
    if total_period[b] > total_period[maior_venda_period]:
        maior_venda_period = b

print("----------|relatório vendas|----------")
print('')
print('')
print("------------------------------|relatório vendas|------------------------------")

for a in range(3):
    print(f"{produtos[a]} | {vendas[a][0]} | {vendas[a][1]} | {vendas[a][2]} | {vendas[a][3]} | {total_prod[a]}")

print("------------------------------------------------------------------------------")
print(f"{'total'} | {total_period[0]} | {total_period[1]} | {total_period[2]} | {total_period[3]} | {total_geral}")

print(f"|total geral - {total_geral}")
print(f"|produto mais vendido - {produtos[maior_venda_prod]} ({total_prod[maior_venda_prod]} unidades)")
print(f"|período com maior movimento - {periodos[maior_venda_period]} ({total_period[maior_venda_period]} vendas)")