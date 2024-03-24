def change():
    expense = 23.75
    money = 100
    print (F"ingresar gasto:") 
    print (expense)
    print (f"dinero recibido")
    print (money)
    print ("n")
    print (f"vuelto")
    change = (money - expense)
    print (change)
    print ("\n")
    print (f"pesos:")
    print (int (change))
    centavos = (change - int (change)) * (int(money))
    print (f"centavos:")
    print (int (centavos))


change()
