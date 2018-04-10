class Product(object):
    def __init__(self, price, name, weight, brand, status = "For sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status 
        return self

    def tax(self):
        self.tax = .0875
        self.price = self.price * self.tax + self.price 
        return self

    def returns(self):
        if self.status == 'defective':
            self.status = "Defective"
            self.price = '$0'
        elif self.status == "like new":
            self.status = "For Sale"
        elif self.status == 'open':
            self.price = 0.80 * self.price
            self.status = "Used"
        return self

    def display_info(self):
        print "Price: " + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight) + ' ' + 'lb(s)'
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)
        return self

product_one = Product(10, 'iPhone', 1, 'Apple')
product_one.sell().tax().returns().display_info()

product_two = Product(10, 'Android', 500, 'Samsung', 'defective')
product_two.sell().tax().returns().display_info()

product_three = Product(10, 'Civic', 5000, 'Honda', "like new")
product_three.sell().tax().returns().display_info()

product_four = Product(10, 'F150', 7000, "Ford", "open")
product_four.sell().tax().returns().display_info()







