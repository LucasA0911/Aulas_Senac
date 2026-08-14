##(w1*x1) + (w2*x2) + ... + (wn*xn) +- b

## Logica simples para o sistema de uma lampada automática, segundo o exemplo do professor

hora = 22 # hora do dia
w1 = 5
x1 =0
if hora >= 6 and hora < 18:
    x1 = 0 # dia
else: 
    x1 = 1 # noite

pessoa = 0 #se tem pessoa
w2 = 3
x2 = 0
if pessoa == 1:
    x2 = 1 # tem pessoa
else:
    x2 = 0 # não tem pessoa

pouco_seguro = 6 # vies para quando eu quero que o sistema esteja apagado com mais facilidade
mais_seguro = 2 # vies para quando eu quero que o sistema acenda com mais facilidade

z = (w1 * x1) + (w2 * x2) - pouco_seguro
print(z)
if z >= 0:
    print('Luz acesa')
else: 
    print('Luz apagada')