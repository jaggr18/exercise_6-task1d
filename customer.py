from vehicle import *
import random

class Customer(object):
    
    def __init__(self,name):
        self.__name = name
        self.__score = Customer.credit_score(self)

    def __str__(self):
        return "Customer: %s" % self.__name

    def credit_score(self):
        if random.randint(0,100) > 60:
            return True
        else:
            return False

    def get_score(self):
        return self.__score


class VIP_Customer(Customer):
    def __init__(self, name):
        Customer.__init__(self, name)
        self.__score = VIP_Customer.credit_score(self)

    def credit_score(self):
        return True

### test cases ###

# initialising customer instances

Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heidi

print(Wendy.get_score()) # expected output: True or False depending on random score
print(Heidi.get_score()) # expected output: True
