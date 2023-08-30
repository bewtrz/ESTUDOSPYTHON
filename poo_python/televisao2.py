import televisao #part.2

TvOn = True
Tv = televisao.Television()

while(TvOn):
    print("########"*5)
    print("# Escolha sua funçaõ desejada abaixo #")
    print("# 1 Aumentar Volume                  #")
    print("# 2 Baixar Volume                    #")
    print("# 3 Aumentar Canal                   #")
    print("# 4 Baixar Canal                     #")
    print("# 5 Mudar Canal                      #")
    print("# 6 Desligar Tv                      #")
    print("########"*5)

    funcao = int(input("Selecione a Opção desejada"))
    if funcao == 1 :
        Tv.AumentarVolume()
        print(f"Volume da Tv: {Tv.Volume}" )
    elif funcao == 2 :
        Tv.BaixarVolume()
        print(f"Volume da Tv: {Tv.Volume}" )
    elif funcao == 3 :
        Tv.AumentarCanal()
        print(f"Canal da Tv: {Tv.Canal}" )
    elif funcao == 4 :
        Tv.BaixarCanal()
        print(f"Canal da Tv: {Tv.Canal}" )
    elif funcao == 5 :
        Tv.MudarCanal(int(input('Digite o canal desejado: ')))
        print(f"Canal da Tv: {Tv.Canal}" )
    else :
        TvOn = False