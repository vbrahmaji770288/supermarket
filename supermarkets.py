name=input("enter the name:")

list=['''

rice 10kg,
sugar 2kg,
dal 2kg,
salt 12kg,
boost 10kg,
carrot 4kg
'''
]

price=0
pricelist=[]
totalprice=0
finalprice=0
itemlist=[]
quantitylist=[]
pricelist=[]



items={"rice":10,"sugar":2,"dal":2,"salt":12,"boost":10,"carrot":4}
while True:
    option=input("press 1 for list or 2 to exit")
    if option=="2":
        print("thank for shooping")
        break
    elif option=="1":
        print(list)
        while True:
            inp1=input("to buy press 1 or 2 to exit")
            if inp1=="2":
                print("thank you shooping")
                break
            elif inp1=="1":
                item=input("choose items").lower()
                while True:
                    quantity_input=input("enter the quantity")
                    if quantity_input.isdigit():
                        quantity=int(quantity_input)
                        break
                    else:
                        print("enter the valid quantity")
                if item in items:
                    price=quantity * items[item]
                    pricelist.append((item,quantity,items[item],price))

                    totalprice+=price
                    itemlist.append(item)
                    quantitylist.append(quantity)
                    # pricelist.append(price)
                else:
                    print("select item is not availble")
            if totalprice>0:
              tax=(totalprice*18)/100
              finalprice=tax+ totalprice

              print(23*"_", "supermarket", 23*"_" )
              print(30*"-","hyderbad")
              print("name",name,30*" ","august 5 2026")
              print(70*"_")
              print("sno",10*" ","items",8*" " ,"quantity",10*" ", "price")
              for i in range(len(pricelist)):
                  print(i,10*" ",itemlist[i],8*" ",quantitylist[i],8*" " ,pricelist[i])

              print(75*"_")
              print(50*" ","total amount","rs",totalprice)
              print("tax amount",50*" ","rs",tax)
              print(75*"_")
              print(50*" ","final amount",finalprice)
              print(75*"_")
              print(20*" ","thank you visit again")
              print(78*"_")
                
              
                    





    