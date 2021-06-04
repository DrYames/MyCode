class Customer:
    def __init__(self,cust_id, firstName, lastName,
                 company, address, city, state,
                 stateZip):
        self.cust_id = cust_id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.stateZip = stateZip

    def getfullAddress(self):
        fullAddress = ""
        if self.company == "":
            fullAddress+=self.firstName+" "+self.lastName+"\n"+self.address+"\n" \
            +self.city+", "+self.state+" "+self.stateZip
        else:
            fullAddress+=self.firstName+" "+self.lastName+"\n" \
            +self.company+"\n" + self.address+"\n"+self.city+", " \
            +self.state+" "+ self.stateZip
        return fullAddress
