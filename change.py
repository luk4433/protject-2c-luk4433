print("Please enter an amount in cents less than a dollar.")
change = int(input())
quarters = change // 25
change_dimes = change % 25
dimes = change_dimes // 10
change_nickles = change_dimes % 10
nickles = change_nickles // 5
change_pennies = change_nickles % 5
pennies = change_pennies // 1

print("Your change will be: ")
print("Q: " + str(quarters))
print("D: " + str(dimes))
print("N: " + str(nickles))
print("P: " + str(pennies))