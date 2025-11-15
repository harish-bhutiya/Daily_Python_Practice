#Tip_Calculator
greeting_message = "Welcome to the tip calculator"
print(greeting_message)
total_bill = float(input("What was the total bill? $\n"))
tip = float(input("How much tip would you like to give? 10, 12 or 15?\n"))
total_tip =  (total_bill * (tip /100+1))
split_bill = int(input("How many people to split the bill?\n"))
final_amount = ( total_tip / split_bill)

print(f"Each person should pay : ${int(final_amount)}")