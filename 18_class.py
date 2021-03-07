class UnderFlowError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Share:
    def __init__(self, CName, NShares, UPrice):
        self.__CName = CName
        self.__NShares = NShares
        self.__UPrice = UPrice

    def __getitem__(self, index):
        try:
            if index == 0:
                return self.__CName
            elif index == 1:
                return self.__NShares
            elif index == 2:
                return self.__UPrice
            else:
                raise IndexError("cannot get the item...")
        except IndexError as e:
            print("Index Error ", e)

    def __setitem__(self, index, value):
        try:
            if index == 0:
                self.__CName = value
            elif index == 1:
                self.__NShares = value
            elif index == 2:
                self.__UPrice = value
            else:
                raise IndexError("cannot set the value...")
        except IndexError as e:
            print("Index error ", e)

    def __add__(self, amt):
        self.__NShares = self.__NShares+amt
        return self

    def __iadd__(self, amt):
        self.__NShares = self.__NShares+amt
        return self

    def __radd__(self, amt):
        self.__NShares = self.__NShares+amt
        return self

    def __sub__(self, amt):
        if amt <= self.__NShares:
            self.__NShares = self.__NShares-amt
            return self
        else:
            raise UnderFlowError("low shares available")

    def __isub__(self, amt):
        if amt <= self.__NShares:
            self.__NShares = self.__NShares-amt
            return self
        else:
            raise UnderFlowError("low shares available")

    def __rsub__(self, amt):
        if amt <= self.__NShares:
            self.__NShares = self.__NShares-amt
            return self
        else:
            raise UnderFlowError("low shares available")

    def __str__(self):
        return "company name:"+self.__CName+"\nno.of shares:"+str(self.__NShares)+"\nunit price:"+str(self.__UPrice)

    def __repr__(self):
        return "("+self.__CName+"," + str(self.__NShares)+","+str(self.__UPrice)+")"


class NoSuchShareError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Person:
    def __init__(self, PName, share_amount):
        self.PName = PName
        self.share_amount = share_amount

    def purchaseShares(self, cname, nshares):
        try:
            if cname not in companies:
                raise NoSuchShareError(f"no such company")

            currentShare = shares[companies.index(cname)]
            NShares = currentShare[1]
            UPrice = currentShare[2]

            if NShares < nshares:
                raise UnderFlowError("company has less shares")

            self.share_amount += UPrice*nshares
            currentShare -= nshares

        except Exception as e:
            print("Exception : ", e)

    def sellShares(self, cname, nsold):
        try:
            if cname not in companies:
                raise NoSuchShareError("no such company")

            currentShare = shares[companies.index(cname)]
            UPrice = currentShare[2]

            if self.share_amount < nsold*UPrice:
                raise UnderFlowError("shares exceeded")
            self.share_amount -= UPrice*nsold
            currentShare += nsold

        except Exception as e:
            print("Exception : ", e)

    def __str__(self):
        return "person name:"+self.PName+"\namount:"+str(self.share_amount)

    def __repr__(self):
        return "person name:"+self.PName+"\namount:"+str(self.share_amount)


shares = []
persons = []
companies = []
people = []
for i in range(2):
    cname = input("company name : ")
    nshares = int(input("number of shares: "))
    price = float(input("price per unit share: "))
    shares.append(Share(cname, nshares, price))
    companies.append(cname)
    print()

for i in range(2):
    name = input(f"name of the person {i+1}: ")
    share_amount = float(input("share amount: "))
    persons.append(Person(name, share_amount))
    people.append(name)
    print()


purchases = int(input("number of shares purchased: "))
for i in range(purchases):
    cname = input("purchased from which company(name): ")
    person = input("by whom(which person): ")
    nshares = int(input("number of shares: "))
    persons[people.index(person)].purchaseShares(cname, nshares)
    print()

sold = int(input("number of shares sold by persons: "))
for i in range(purchases):
    cname = input("sold to which company(name): ")
    person = input("by whom(name of person): ")
    nshares = int(input("number of shares sold: "))
    persons[people.index(person)].sellShares(cname, nshares)
    print()

for share in shares:
    print(share, "\n")

for person in persons:
    print(person, "\n")
