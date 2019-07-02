


shoppinglist = []
items = ""
address = 5
while address >=0:
   # user_input = input("enter store name: ")
   # user_input = input("enter items: ")
   # user_input = input("enter qty: ")

    if address ==("walmart", "costco", "fiesta", "samsclub", "Aldi"):
        print("please presss 1 for store address\n")
        print("please press 2 for item bought\n")
        print("please press 3 for qty\n")
        print("please 4 to view shoppinglist\n")
        print("please press q to exit")
        if shoppinglist == 1:
            print("what did you buy:")
        shoppinglist = input("description: ")
        if shoppinglist in (address):
               print("thank you")




