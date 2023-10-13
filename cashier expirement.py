#input
print("------WELCOME!------")
calculation = int(input("How much were the groceries?: "))
money_received = int(input("How much did the customer pay?:  "))

#maths
money_back = money_received - calculation 
twenty_euro = 20
ten_euro = 10
five_euro = 5
two_euro = 2
one_euro = 1

money_twenty = int(money_back/twenty_euro)
twenty_new_balance = money_back - money_twenty * twenty_euro

money_ten = int(twenty_new_balance/ten_euro)
ten_new_balance = twenty_new_balance - money_ten * ten_euro

money_five = int(ten_new_balance/five_euro)
five_new_balance = ten_new_balance - money_five * five_euro

money_two = int(five_new_balance/two_euro)
two_new_balance = five_new_balance - money_two * two_euro
   
money_one = int(two_new_balance/one_euro)
one_new_balance = two_new_balance - money_one * one_euro




#output
print(str(money_back) + " is the amount owed")
print("-----------------------------")
print(money_twenty, "$ 20 Bill")
print(money_ten, "$ 10 Bill")
print(money_five, "$ 5 Bill")
print(money_two, "$ 2 Bill")
print(money_one, "$ 1 Bill")
#print("-----------------------------")