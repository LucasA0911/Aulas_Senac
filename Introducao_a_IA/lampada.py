##(w1*x1) + (w2*x2) + ... + (wn*xn) +- b

## Logica simples para o sistema de uma lampada automática, segundo o exemplo do professor
def lampada(x1:int,x2:int,b:int):
    """Logica simples de um perceptron.

        Args:
            x1 (int): Defina a hora com um valo inteiro. EX: 6, 22.
            pessoa (int): Defina 1 se tiver uma pessoa, e 0 se não tiver uma pessoa. 
            seguro (int) Digite 1 se quer uma programação mais segura, e 0 se quiser menos segura.

        Returns:
            str: Retorna se a luz esta acesa ou apagada.
    """
    w1 = 5 # define o peso da variável x1
    if x1 >= 6 and x1 < 18: #Verifica se está de dia ou de noite
        x1 = 0 # dia
    else: 
        x1 = 1 # noite

    w2 = 3 # define o peso da váriavel x2
    if x2 == 1: #verifica se tem alguém no local
        x2 = 1 # tem pessoa
    else:
        x2 = 0 # não tem pessoa
    
    if b == 1:
        b = 2 # vies para quando eu quero que o sistema acenda com mais facilidade
    else:
        b = 6 # vies para quando eu quero que o sistema esteja apagado com mais facilidade

    z = (w1 * x1) + (w2 * x2) - b
    if z >= 0:
        print('Luz acesa')
    else: 
        print('Luz apagada')

lampada(6,1,0)