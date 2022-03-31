print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to leave? 15, 20, 25? "))
people = int(input("How many people are you splitting between? "))

bill_w_tip = tip / 100 * bill + bill
per_person = bill_w_tip / people
bill_total = "{:.2f}".format(bill_w_tip)
split_total = "{:.2f}".format(per_person)


print("Total with tip: $" + (bill_total))
print(f"Split between {people} people is: $${split_total} per person.")

