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
npc="???"
pedidosGer=0
pedidosTia=0
pedidosJoa=0
pedidoGer=[0]
pedidoTia=[0]
pedidoJoa=[0]


while dinheiro>0:
    print("cafe:",cafe,"leite:",leite,"acúcar:",acucar)
    sleep(1)
    selecao=int(input("O que queres fazer (1-pedido,2-comprar): "))
    sleep(1)
    print()
    if selecao==1:
        pedido=[]

        npcgerado=randint(1,5)
        if npcgerado==10:
            npcescolhido=randint(1,3)
            match npcescolhido:
                case 1:
                    npc="Germias"
                case 2:
                    npc="João"
                case 3:
                    npc="Tiago"

        if npc=="Germias" and pedidoGer[0]>0:
            pedido=pedidoGer
        elif npc=="João" and pedidoJoa[0]>0:
            pedido=pedidoJoa
        elif npc=="Tiago" and pedidoTia[0]>0:
            pedido=pedidoTia
        else:
            for i in range(1,4):
                pedido.append(randint(1,10))
                if pedido[0]>10:
                    pedido[0]=10

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

        print(npc,": Quero um café",qcafe,"com",qleite,"leite e",qacucar,"acucar")

        pcafe=int(input("café:"))
        pleite=int(input("leite:"))
        pacucar=int(input("acúcar:"))
        sleep(3)
        print()

        if pedido[0]+4>=pcafe>=pedido[0]-4 and pedido[1]+4>pleite>pedido[1]-4 and pedido[2]+4>pacucar>pedido[2]-4:
            match npc:
                case "Germias":
                    pedidoGer=pedido
                    if pedidosGer==2:
                        dinheiro=dinheiro+60
                        print("Recebeste uma corjeta do Germias (+60 euros)")
                    pedidosGer=pedidosT+1
                case "João":
                    pedidoJoa = pedido
                    if pedidosJoa == 2:
                        dinheiro = dinheiro + 30
                        print("Recebeste uma corjeta do João (+30 euros)")
                    pedidosJoa = pedidosJoa + 1
                case "Tiago":
                    pedidoTia = pedido
                    if pedidosTia == 2:
                        dinheiro = dinheiro + 30
                        print("Recebeste uma corjeta do Tiago (+30 euros)")
                    pedidosTia = pedidosTia + 1

            print("Obrigado!(+30 euros)")
            dinheiro=dinheiro+30
            cafe=cafe-pcafe
            leite = leite - pleite
            acucar=acucar-pacucar
        else:
            print("Não gostei(+0 euros)")
            cafe = cafe - pcafe
            leite = leite - pleite
            acucar = acucar - pacucar
        print()





