class Bank:
    bank_name = ""
    
    def __init__(self, name):
        self.name = name 

    @classmethod  
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name 
        print(f"Bank name is changed to: {cls.bank_name}")


b1 = Bank("National Bank of Pakistan")
b2 = Bank("Soneri Bank")

b1.change_bank_name("United Bank Limited")
b2.change_bank_name("Habib Bank Limited")
