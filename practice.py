

class Shoppinglist:
        def _init_(self, name, address):
         self.name = name
         self.address = address



        def show(self):
           print(self.name,self.address)

class Items(Shoppinglist):
    def _init_(self):
        self.qty = 'qty'
        self. price= 'price'


Shoppinglist.show()



#not input to this app.