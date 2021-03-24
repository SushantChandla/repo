
import smartpy as sp

TTransaction = sp.TRecord(
    stockType       = sp.TString,
    price           = sp.TInt,
    quantity        = sp.TInt,
    time            = sp.TTimestamp
)

class TransactionRecipts(sp.Contract):
    def __init__(self):
        self.init_type(sp.TRecord(
            allTransaction=sp.TMap(sp.TString,sp.TList(TTransaction)),
            stocksTotal=sp.TMap(sp.TString,sp.TMap(sp.TString,sp.TInt)))
        )
        self.init(allTransaction=sp.map(), stocksTotal=sp.map())

        
    @sp.entry_point
    def addTransaction(self, parms):
        sp.set_type(parms.username, sp.TString)
        sp.set_type(parms.price,sp.TInt)
        sp.set_type(parms.quantity,sp.TInt)
        sp.set_type(parms.stockType,sp.TString)
        
        user = parms.username
        transactions=sp.local('transaction',sp.list())
        sp.if self.data.allTransaction.contains(user):
            sp.for item in self.data.allTransaction[user]:
                transactions.value.push(item)
        
        stockType=parms.stockType
        
        price=parms.price
        quantity=parms.quantity
        time = sp.timestamp_from_utc_now()
        
        
        sp.if self.data.stocksTotal.contains(user):
            sp.if self.data.stocksTotal[user].contains(stockType):
                allstocks= self.data.stocksTotal[user]
                allstocks[stockType]=quantity+allstocks[stockType]
                self.data.stocksTotal[user]=allstocks
                
            sp.else:
                allstocks= self.data.stocksTotal[user]
                allstocks[stockType]=quantity
                self.data.stocksTotal[user]=allstocks
          
        sp.else:
            self.data.stocksTotal[user]=sp.map()
            self.data.stocksTotal[user][stockType]=quantity
               

        m = sp.record(
            stockType = stockType,
            price = price,
            quantity = quantity,
            time = time
        )
        
        transactions.value.push(m)
        self.data.allTransaction[user]=transactions.value
        
        
        

if "templates" not in __name__:
    @sp.add_test(name = "Transaction Recipts")
    def test():
        scenario = sp.test_scenario()
        main = TransactionRecipts()
        scenario.h1("Main")
        scenario += main
        scenario += main.addTransaction(username="hello",stockType="a",price=400,quantity=2)
        scenario += main.addTransaction(username="hello",stockType="b",price=400,quantity=23)
        scenario += main.addTransaction(username="secondUser",stockType="a",price=300,quantity=20)
        scenario += main.addTransaction(username="hello",stockType="a",price=40,quantity=21)