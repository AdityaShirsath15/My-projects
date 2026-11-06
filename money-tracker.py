class exp:
    def menu(self): #menu gives access to then features of the app
        while True:
            print("-----STUDENT MONEY TRACKER APP------")
            print("1.ADD EXPENSE")
            print("2.SEARCH EXPENSE")
            print("3.TRANSACTION LOG")
            print("4.EXIT")
            choice=int(input("Enter your choice: "))
            if(choice==1):
                self.add_exp()
            elif(choice==2):
                self.search_exp()
            elif(choice==3):
                self.transaction()
            elif(choice==4):
                break
            else:
                print("INVALID CHOICE")
    def __init__(self): #always add this bro 
        self.data={}
        self.cat=["external","stationary","travel"]
        self.trans={}
    def add_exp(self): #handles the inputing of amount and data
        self.data["amt"]=input("Enter the amount: ")
        self.data["date"]=input("Enter Date: ")
        self.data["cat"]=input("Enter a category: ")
        if(self.data["cat"] not in self.cat):
            ask=input("Current category does not exist. Would you like to make a new category?")
            if(ask=="yes"):
                self.cat.append(self.data["cat"])
            else:
                print("Okay! Got it.")
        else:
            print("added")
            entry={"amt":self.data["amt"],"cat":self.data["cat"]}
            self.data.setdefault(self.data["date"],[]).append(entry) #it helps to store entry based on the date entered hence helping it to be searchable
            print(f"Saved Under {self.data["date"]} = {entry}")
    def search_exp(self): #helps us to search for transaction and expense based on there date
        search=input("Enter a date: ")
        choice=input("Do you want to search for Expense or Transaction:  ").lower()
        if(choice=="expense"):
            if(search in self.data):
                print(self.data[search])
            else:
                print("No Record Found")
        elif(choice=="transaction"):
            if(search in self.trans):
                print(self.trans[search])
            else:
                print("No Record Found")
        else:
            print("No Record Found In Both")

    def transaction(self):#this is the transaction section of my app where you can input the transaction
        self.trans["add_trans"]=int(input("Enter Transaction: "))
        self.trans["add_date"]=input("Enter Date Of Transaction: ")
        self.trans["add_cat"]=input("Enter Transaction Category: ")
        entry={"Amount": self.trans["add_trans"],"Date": self.trans["add_date"], "Category": self.trans["add_cat"]}
        self.trans.setdefault(self.trans["add_date"],[]).append(entry)
        print(f"Saved Under {self.trans["add_date"]}= {entry}")
obj_exp=exp()
obj_exp.menu()