from client import*
from datetime import*

ako=client()

 
bancomat={
    200:0,
    100:0,
    50:0,
    10:0,
    }
def banca(value="10",count=0,acceskey=False):
    if acceskey:
        global bancomat
        bancomat[value]+=count
        return bancomat
    else:
        return "Neautorizat"
    
def takeOut(suma=0,client=ako):
    global bancomat
    check200=bancomat[200]
    check100=bancomat[100]
    check50=bancomat[50]
    check10=bancomat[10]
    takeCoins=[0,0,0,0,True]
    
    while True:
        if suma<ako.money():
            
            if suma>=200 and check200>=1:
                suma-=200
                check200-=1
                takeCoins[0]+=1
                
            elif suma>=100 and check100>=1:
                suma-=100
                check100-=1
                takeCoins[1]+=1
                
            elif suma>=50 and check50>=1:
                suma-=50
                check50-=1
                takeCoins[2]+=1
                
            elif suma>=10 and check10>=1:
                suma-=10
                check10-=1
                takeCoins[3]+=1
            
            elif suma==0:
                return takeCoins
                break
            else:
                print("Nu s-a putut efectua retragerea(Bancomat scos din functiune momentan)")
                takeCoins=[0,0,0,0,False]
                return takeCoins
                break
        else:
            print("Nu s-a putut efectua retragerea (Sold insuficient pentru a retrage asceasta suma)")
            takeCoins=[0,0,0,0,False]
            return takeCoins
            break               
            
        
        
def updateBancomat(takeCoins):
    global bancomat
    bancomat[200]-=takeCoins[0]
    bancomat[100]-=takeCoins[1]
    bancomat[50]-=takeCoins[2]
    bancomat[10]-=takeCoins[3]
    return bancomat
    



y=datetime.now()
o=int(y.strftime("%S"))
print("se incarca datele")
bacnote=[0,0,0,0]
dataCard=["name",0]
for x in range(1):
    card=open("card.txt","rt")
    coin=open("bancomat.txt","rt")
    loaded=True
    for x in range(4):
        bacnote[x]=int(coin.readline())
    for x in range(2):
        dataCard[x]=card.readline()
        
    banca(200,bacnote[0],True)
    banca(100,bacnote[1],True)
    banca(50,bacnote[2],True)
    banca(10,bacnote[3],True)

    ako.moneyAdd(int(dataCard[1]))
    card.close()
    coin.close()
    
    mainMenu={
        "1":"Interogare sold",
        "2":"Retrage cash",
        "3":"Depune cash",
        "0":"Exit",
        }
print(dataCard[0])    
while True:
    print("\n")
    for x in mainMenu.keys():
        print(x,"-->",mainMenu[x])
        
    option=input("Alegeti va rog operatia\n")
    
    if option=="4":
        key=input("introduceti cheia de acces pt a deschide bancomatul\n")
        if key=="":
            keyValue=[0,0,0,0]
            for x in range(4):
                a=input("insert\n")
                keyValue[x]=int(a)
            banca(200,keyValue[0],True)
            banca(100,keyValue[1],True)
            banca(50,keyValue[2],True)
            banca(10,keyValue[3],True)
            
    elif option=="1":
        acces=open("card.txt","at")
        y=datetime.now()
        data=y.strftime("\n%d-%m-%Y  %H:%M\n")
        acces.write(data)
        print("Aveti ",ako.money(),"in cont la ora actuala")
        sold="Soldul interogat a fost {} \n\n"
        acces.write(sold.format(ako.money()))
        acces.close()

    elif option=="2":
        take=open("card.txt","at")
        y=datetime.now()
        data=y.strftime("\n%d-%m-%Y  %H:%M\n")
        take.write(data)
        sold="\nAu fost retrasi {} din cont"
        takeKey=int(input("Cati bani doriti sa retrageti?(multipli de 10)\n"))
        takeCoins=takeOut(takeKey)
        UPbanca=updateBancomat(takeCoins)
        
        if takeCoins[4]:
            x="\nAti primit :\n {} bacnote de 200\n{} bacnote de 100\n{} bacnote de 50\n{} bacnote de 10"
            take.write(sold.format(takeKey))
            take.write(x.format(takeCoins[0],takeCoins[1],takeCoins[2],takeCoins[3]))
            ako.moneySdd(takeKey)
            print(x.format(takeCoins[0],takeCoins[1],takeCoins[2],takeCoins[3]))
        else:
            take.write(sold.format(0))
            print("Nu s-a putut retrage")
            #UPDATE CARD
        with open("card.txt","rt") as hjkg:
            lines=hjkg.readlines()
                 
        lines[1]=str(str(ako.money())+"\n")
         
        with open("card.txt","wt") as po:
            po.writelines(lines)
             
        take.close()
        
        #Update file bancomat.txt
        bancomatKey=open("bancomat.txt","wt")
        data=str(str(UPbanca[200])+"\n"+str(UPbanca[100])+"\n"+str(UPbanca[50])+"\n"+str(UPbanca[10])+"\n")
        bancomatKey.write(data)
        bancomatKey.close()

        
    elif option=="3":
        take=open("card.txt","at")
        y=datetime.now()
        data=y.strftime("\n\n%d-%m-%Y  %H:%M\n")
        take.write(data)
        sold="\n\nAu fost depusi {} in cont"
        putKey=int(input("Cati bani doriti sa depuneti?\n"))
        ako.moneyAdd(putKey)
        take.write(sold.format(putKey))
        take.close()
        with open("card.txt","rt") as hjkg:
            lines=hjkg.readlines()
                 
        lines[1]=str(str(ako.money())+"\n")
         
        with open("card.txt","wt") as po:
            po.writelines(lines)
             
        #after with isn't necesary close() function 
        

        
        
    elif option=="0":
        break
    else:
        print("invalid option")
        
        
accesat=open("card.txt","at")
accesat.write("\n---------------------")
accesat.close()
        
        
