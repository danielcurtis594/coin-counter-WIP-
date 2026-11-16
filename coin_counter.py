cointypeloop=True
bagloop=True
name=input("enter your name")

while cointypeloop==True:
    coin_type=input("enter coin type in p").replace("p","")
    coin_type=coin_type.replace(" ","")
    coin_type=coin_type.lower()
    if coin_type=="200" or coin_type=="100" or coin_type=="50" or coin_type=="20" or coin_type=="10" or coin_type=="5" or coin_type=="2" or coin_type=="1":
        cointypeloop=False
    else:
        cointypeloop=True

coin_type=int(coin_type)
print(coin_type)

while bagloop==True:
    bag_weight=input("enter bag weight")
    if bag_weight.isdigit():
        bagloop=False
    else:
        bagloop=True

bag_weight=int(bag_weight)
print(bag_weight,"g")
