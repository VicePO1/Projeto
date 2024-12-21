from random import randint
from time import sleep

dinheiro=100
leite=30
cafe=30
acucar=30
dia=0
pedidosS=0
pedido=[]
qcafe=0
qleite=0
qacucar=0

while dinheiro>0:
    print("cafe:",cafe,"leite:",leite,"acúcar:",acucar)
    sleep(1)
    selecao=int(input("O que queres fazer (1-pedido,2-comprar)"))
    sleep(1)
    print()
    if selecao==1:
        pedido=[]

        for x in range(1,4):
            pedido.append(randint(1,30))
        if pedido[0]<10:
            pedido[0]=9

        if pedido[0]<10:
            qcafe="pequeno"
        elif 20>pedido[0]>=10:
            qcafe="medio"
        elif pedido[0]>=20:
            qcafe="grande"
        if pedido[1]<10:
            qleite="pouco"
        elif 20>pedido[1]>=10:
            qleite="algum"
        elif 20<=pedido[1]:
            qleite="muito"
        if pedido[2]<10:
            qacucar="pouco"
        elif 20>pedido[2]>=10:
            qacucar="algum"
        elif 20<=pedido[2]:
            qacucar="muito"

        print("Quero um café",qcafe,"com",qleite,"leite e",qacucar,"acucar")

        pcafe=int(input("café:"))
        pleite=int(input("leite:"))
        pacucar=int(input("acúcar:"))
        sleep(3)
        print()

        if pedido[0]+4>=pcafe>=pedido[0]-4 and pedido[1]+4>pleite>pedido[1]-4 and pedido[2]+4>pacucar>pedido[2]-4:
            print("Obrigado!(+10 euros)")
            dinheiro=dinheiro+10
            cafe=cafe-pcafe
            leite = leite - pleite
            acucar=acucar-pacucar
        else:
            print("Não gostei(+0 euros)")
            cafe = cafe - pcafe
            leite = leite - pleite
            acucar = acucar - pacucar
        print()





