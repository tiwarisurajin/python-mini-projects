def operation() :
    op_input =input("Enter the operation to perform(add,print): ").lower()
    if op_input == "add":
         add()
    elif op_input == "print" :
         print1()


def add() :
    stocks = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
    add_input =input("Enter the stocks name: ").lower()
    price_input = int(input("Enter the price of stocks: "))
    if add_input in stocks :
        stocks[add_input].append(price_input)
        for i,v in stocks.items() :
            print(i,"==>",v)
def print1() :
     stocks = {"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
     for i,v in stocks.items():
            average= sum(v)/ len(v)
            round().average
            print(i,"==>",v,"AVG ==",average)

operation()