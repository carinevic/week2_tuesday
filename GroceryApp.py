
shoppinglists =[]
items =[]
user_input =""

while user_input !="q":

    name = input("enter store name: ")
    address =input("enter address: ")
    items = input("enter item: ")
item = input("enter item")

class Shoppinglist:
    def _init_(self,name, address):
     self.name = name
     self.address = address

shoppinglist = shoppinglists(name,address, item)
shoppinglists.append(Shoppinglist)

for g in Shoppinglist:
 print(g.name)
print(g.address)
print(g.item)

user_input = input("enter any key to continue")



class Items(Shoppinglist):
    def _init_(self,name,address):

        self.item = items
        #self.quantity = quantity

    items.append(items)

for(shoppinglist,items) in range(shoppinglist,items):
    print("shoppinglist: " ,shoppinglist, "items: ",items)