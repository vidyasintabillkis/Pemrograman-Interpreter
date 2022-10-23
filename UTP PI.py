print("    __  ________   ________  ______    ____  __ __ ____________   __    ___  ________________  _______ ")
print("   /  |/  /  _/ | / /  _/  |/  /   |  / __ \/ //_// ____/_  __/  / /   /   |/_  __/ ____/ __ \/  _/   |")
print("  / /|_/ // //  |/ // // /|_/ / /| | / /_/ / ,<  / __/   / /    / /   / /| | / / / __/ / /_/ // // /| |")
print(" / /  / // // /|  // // /  / / ___ |/ _, _/ /| |/ /___  / /    / /___/ ___ |/ / / /___/ _, _// // ___ |")
print("/_/  /_/___/_/ |_/___/_/  /_/_/  |_/_/ |_/_/ |_/_____/ /_/    /_____/_/  |_/_/ /_____/_/ |_/___/_/  |_|")
title ="\n---------------------------------------welcome to our store--------------------------------------------"  
subtitle = "----------------------------Place where you can get everything you need--------------------------------\n"                                              
print(title.upper())
print(subtitle.title())

kategoriBarang = {1:["1. Staple Food","1. Rice","2. Flour","3. Wheat","4. Bread"], 
                  2:["2. Drink", "1. Milk", "2. Coffe & Tea", "3. Yogurt", "4. Mineral Water"], 
                  3:["3. Snack", "1. Chips", "2. Biscuit", "3. Chocolate", "4. Candy"], 
                  4:["4. Frozen Food", "1. Nuggets", "2. Sausage", "3. Meatball", "4. Fish Sticks"], 
                  5:["5. Toiletries", "1. Shampoo & Soap", "2. Toothpaste","3. Laundry Detergent", "4. Dish Soap"]}

stapleFood = {1:['Pandan Wangi 5Kg', 'Ramos Super 5Kg', 'Pulen Wangi 5Kg', 'Ketan Putih 500G', 'Ketan Hitam 500G'],
              2:['Segitiga Biru 1Kg','Cakra Kembar 1Kg','Maizena 328 1Kg','Pak Tani 500G','Rose Brand 500G'],
              3:['Quaker Oatmeal Instant 800G','Quaker Oatmel Quick 800G','Captain Oats Instant 12x40G','Naturich Wheat Flour 1Kg','Polococoa Oatmeal 400Gr'],
              4:['Sari Roti Tawar Double Soft','Sari Roti Tawar Jumbo','Mr. Bread Roti Tawar','Mr. Bread Roti Kasur','Sari Roti Milky Soft']}

Drink = {1:['Ultra Milk 1L', 'Cimory Milk 1L','Greenfields 1L', 'Anlene Vanilla 590g', 'Nestle Dancow 800g'],
         2:['ABC Kopi Susu 200Ml', 'Tora Cafe 180Ml', 'Nescafe latte 240Ml','Teh Botol 1L', 'Teh SariWangi 250'],
         3:['Cimory Yogurt Squeeze 120g', 'Heavenly Blush Yogurt 200Ml', 'Hilo Smoothie Bowl 240g', 'Biokul Natural Set 100Ml', 'Biokul Stirred 100Ml'],
         4:['Danone Aqua 600Ml', 'Le Minerale 600Ml', 'Cristaline 600Ml', 'Pristine 600Ml', 'Prim-a 600Ml']}

Snack = {1:['Chitato Sapi Panggang 205g', 'Lays Nori Seaweed 120g', 'Chiki Balls Choco 200g', 'Jetz Stick Chocofiesta 200g', 'Pota Bee Rumput Laut 200g'],
         2:['Roma Sari Gandum 240g', 'Monde Pie Bis Almond 190g', 'Nissin Lemonia Lemon 190g', 'Regal Marie Biscuit 185g', 'Biskuit Roma Kelapa 300g'],
         3:['Toblerone', 'Dairy Milk', 'Silverqueen', 'Kisses', 'Lindt'],
         4:['Fox\'s Fruits 50pcs', 'Tamarind 50pcs', 'Chupa Chups 1seeds', 'Yupi Love 50pcs', 'Sugus Strawberry']}

frozenFood = {1:['Nugget Merk Belfoods 450g', 'So Good Chicken Nugget 400g', 'Nugget Merk Champ 350g', 'Fiesta Chicken Nugget 500g', 'Kanzler Chrispy Nugget450g'], 
              2:['Kanzler Beef Cocktail Sausage', 'Horeca Pack Beef Breakfast Sausage', 'Kemfood Sosis Sapi Beef Wiener ', 'KIBIF Smoked Sosis Sapi Lada Hitam', 'Champ Beef Sausages Serbaguna'],
              3:['So Good Bakso Kuah', 'Fiesta Bakso Keju', 'Champ Bakso Ayam', 'Sumber Selera Bakso', 'Belfoods Bakso Ayam'],
              4:['Cedea Stick Fish 1Kg', 'So Eco Fish Stick 500g', 'Salimah Food Stick 500g', 'Shifudo Nori Stick 500g','Dongwon Eomuk Stick 500g']}

Toiletries = {1:['Pantene Anti Dandruff 400ml', 'Head & Shoulders Sampo Menthol Dingin+ 850ml', 'Natur Extract Ginseng 270ml', 'Biore Ref 250ml', 'Dettol 60gr'],
              2:['Sensodyne Pasta Fresh Mint 100gr', 'Pepsodent Sensitive Expert Original', 'CLOSE UP Deep Action Fresh 160gr', 'Pepsodent White Toothpaste 225gr', 'Pepsodent Pasta Gigi Whitening 190g'],
              3:['DAIA Detergent Bubuk Violet 1.7Kg', 'Attack Jaz 1 Semerbak&Pesonan 1.7Kg', 'SOKLIN Softergent Detergent 770 gr', 'Rinso Molto Bubuk Anti Noda 1.4kg', 'Soklin liq antbact violet 1600ml'],
              4:['Sunlight Li me Sabun Cuci Piring 755ml', 'Mama Lemon Extra Clean Fresh Lemon 780Ml', 'Sunlight Sabun Extra Higienis 700 ml','SOS Cairan Pencuci Piring Lemon 750mL','Sparkle Jeruk Nipis Sabun Cuci Piring 780mL']}

staplePrice = {1:{1:79500,2:59900,3:64000,4:14700,5:18100},2:{1:24000,2:19000,3:17500,4:15000,5:5700},3:{1:52000,2:52000,3:33300,4:68000,5:52000},4:{1:15900,2:15900,3:23900,4:10200,5:7200}}
drinkPrice = {1:{1:12000,2:24500,3:29000,4:112000,5:88000},2:{1:4000,2:3500,3:9000,4:27000,5:23000},3:{1:3500,2:4000,3:16000,4:15000,5:11000},4:{1:4000,2:4500,3:5000,4:5000,5:4000}}
snackPrice = {1:{1:17000,2:11000,3:15500,4:16000,5:17000},2:{1:14000,2:23000,3:11000,4:31000,5:22000},3:{1:32000,2:16000,3:25000,4:85000,5:1000000},4:{1:23000,2:14000,3:2000,4:18000,5:4000}}
frozenPrice = {1:{1:41000,2:46000,3:24000,4:46500,5:37000},2:{1:38500,2:32500,3:45000,4:105000,5:15000},3:{1:18000,2:45000,3:23000,4:53000,5:12000},4:{1:51000,2:26000,3:25000,4:24000,5:110000}}
toiletPrice = {1:{1:35000,2:60000,3:27000,4:15900,5:3100},2:{1:23500,2:27000,3:17000,4:12300,5:36700},3:{1:29900,2:37700,3:28500,4:27500,5:43200},4:{1:29500,2:17500,3:20600,4:12700,5:11000}}

membership = (["2117051095","Jihan Haya Mufialdo",0], ["2117051029","Vidya Sinta Billkis",0], ["2117051042", "Shafa Auliya",0])

pilihMenu1,pilihMenu2,pilihMenu3 = 0,0,0
listMenu3 = []
listHarga = []
orderQuantity = []
totalPembelian = 0
totalAkhir = 0

def menu1() :
  print("\n-----Item Category-----")
  for i in range(len(kategoriBarang)) :
    print(kategoriBarang[i+1][0])
  print("-----------------------")
  global pilihMenu1
  while True :
    try : 
      pilihMenu1 = int(input("Enter Section\t : "))
      if pilihMenu1<=0 or pilihMenu1>5 :
        raise ValueError
      print("")
      break
    except :
      print("The Category Item isn't available")
  menu2()
  
def menu2() :
  global pilihMenu2
  print("\n-----Types Of Goods-----")
  for i in range(1,len(kategoriBarang)+1) :
    if pilihMenu1 <= 5:
      if pilihMenu1==i :
        for j in range(1,len(kategoriBarang[pilihMenu1])) : 
          print(kategoriBarang[pilihMenu1][j])
        print("-----------------------")
        print("<BACK = 0>")
  while True :  
    try :       
      pilihMenu2 = int(input("Enter Section\t : "))
      if pilihMenu2>=5 :
        raise ValueError
      print("")
      break
    except ValueError :
      print("The Item isn't Available")
  menu3()
  
def menu3() :
  global price
  if pilihMenu2==0 :
    menu1()
  else :
    for j in range(5) :
      menuMerk = {1:stapleFood[pilihMenu2][j],2:Drink[pilihMenu2][j],3:Snack[pilihMenu2][j],4:frozenFood[pilihMenu2][j],5:Toiletries[pilihMenu2][j]}
      price = {1:staplePrice[pilihMenu2][j+1],2:drinkPrice[pilihMenu2][j+1],3:snackPrice[pilihMenu2][j+1],4:frozenPrice[pilihMenu2][j+1],5:toiletPrice[pilihMenu2][j+1]}
      print(str(j+1)+".",menuMerk[pilihMenu1],"\t\t\t",price[pilihMenu1])
    print("-----------------------")
    print("<BACK = 0>")

  global pilihMenu3 
  while True :
      try :       
        pilihMenu3 = int(input("Enter Section\t : "))
        if pilihMenu3==0 :
          menu2()
        elif pilihMenu3<=0 or pilihMenu3>5 :
          raise ValueError
        print("")
        break
      except ValueError :
        print("The Item isn't Available")
  menuMerk = {1:stapleFood[pilihMenu2][pilihMenu3-1],2:Drink[pilihMenu2][pilihMenu3-1],3:Snack[pilihMenu2][pilihMenu3-1],4:frozenFood[pilihMenu2][pilihMenu3-1],5:Toiletries[pilihMenu2][pilihMenu3-1]}
  price = {1:staplePrice[pilihMenu2][pilihMenu3],2:drinkPrice[pilihMenu2][pilihMenu3],3:snackPrice[pilihMenu2][pilihMenu3],4:frozenPrice[pilihMenu2][pilihMenu3],5:toiletPrice[pilihMenu2][pilihMenu3]}  
  listMenu3.append(menuMerk[pilihMenu1])
  listHarga.append(price[pilihMenu1])
  menu4()

def menu4() :
  price = {1:staplePrice[pilihMenu2][pilihMenu3],2:drinkPrice[pilihMenu2][pilihMenu3],3:snackPrice[pilihMenu2][pilihMenu3],4:frozenPrice[pilihMenu2][pilihMenu3],5:toiletPrice[pilihMenu2][pilihMenu3]}
  print("Price\t\t\t :", price[pilihMenu1])
  while True :
    try :
      quantity = int(input("Enter Order Quantity\t : "))
      orderQuantity.append(quantity)
      if quantity <= 0 :
          raise ValueError
      print("")
      break
    except ValueError :
      print("Quantity must be more than 0")
  amount = price[pilihMenu1]*quantity
  print("Total Price\t\t :",amount)
  global totalPembelian,totalAkhir
  totalPembelian+=amount
  totalAkhir = totalPembelian
  print("\nWanna Get Another Thing?")
  repeat = input("<Y/N>\t\t : ")
  if repeat=='Y' :
    menu1()
  elif repeat=='N' :
    print("\nAre You a Member?")
    mem = input("<Y/N>\t\t : ")
    if mem=="Y" :
      member()
      struk()
    elif mem=="N" :
      struk()

def struk() :

  print("\nTotal\t :",totalAkhir)
  bayar = int(input("Bayar\t : "))
  
  if bayar >= totalAkhir :
    kembalian = bayar-totalAkhir
    a ="\n-------------struk belanja-------------"
    print(a.upper())
    c ="\t  minimarket lateria"
    print(c.upper())
    print("---------------------------------------\n")
    for i in range(len(listMenu3)) :
      print(listMenu3[i],"\t\t",listHarga[i])
      print("x"+str(orderQuantity[i]),orderQuantity[i]*listHarga[i])
    print("\n\nTotal\t\t :",totalPembelian)
    print("Diskon\t\t :",totalPembelian-totalAkhir)
    print("Total\t\t :",totalAkhir)
    print("Bayar\t\t :",bayar)
    print("Kembalian\t :",kembalian)
    b ="\n-----terima kasih sudah berbelanja-----"
    print(b.upper())
  else :
    struk()

def member():
  global membership
  #global totalPembelian
  global totalAkhir
  memberInput = input("Enter Member's Username : ")
  for a in range(len(membership)) :
    if memberInput == membership[a][0]:
      print("Nama Member :",membership[a][1])
      j=400000
      poin = list(membership)
      jumlah=1
      if totalPembelian > 500000 :
        poin [a][2] += 5
      while j >= 100000 :
        if totalPembelian > j:  
          poin [a][2] += 5-jumlah
          membership = tuple(poin)
          print("Total Poin : ", membership[a][2])
          break
        jumlah+=1
        j-=100000 
      print("Wanna Convert Point? ");
      convert = input("<Y/N> : ")
      if convert=='Y' :
        diskon = membership[a][2]*2000
        totalAkhir -= diskon
        poin[a][2] = 0
        membership = tuple(poin)
      break
  else:
    print("Username not Found")
     

menu1()
