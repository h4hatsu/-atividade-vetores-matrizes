dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
chamados = []

for a in range(5):
    valor = -1
    while valor < 0:
        valor = int(input(f"|digite a quantidade de chamados durante o dia| - {dias[a]}: "))
        if valor < 0:
            print('|esse valor não é aceito| -')
    chamados.append(valor)

total = 0
for a in range(5):
    total = total + chamados[a]

media = total / 5

qtd_maior = 0
for a in range(1, 5):
    if chamados[a] > chamados[qtd_maior]:
        qtd_maior = a

print('----------|relatório|----------')
for a in range(5):
    print(f"{dias[a]}: {chamados[a]}")

print(f"|total de chamados| - {total}")
print(f"|média diária| - {media}")
print(f"|dia com maior demanda| - {dias[qtd_maior]} ({chamados[qtd_maior]} - chamados)")

#não consegui colocar os dias acima da média