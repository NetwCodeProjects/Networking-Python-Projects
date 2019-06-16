# "quick" method uses only deposit
# then returns
# full price and early price monthly cost
# and price of tuition: full and early

# "long" method requires bootcamp cost
# and deposit amount
# returns total cost after deposit
# and monthly cost

print("Choose method: quick or long")
method = input()

if method == "quick":
	print("Input deposit amount")
	deposit = input()
	def monthly(deposit, bc_cost):
		return (bc_cost - deposit) / 6
	full = 11495
	early = 10495
	fullprice = monthly(int(deposit), full)
	earlyprice = monthly(int(deposit), early)
	post_fulldeposit = int(full) - int(deposit)
	post_earlydeposit = int(early) - int(deposit)
	print("_______________________")
	print("Full price of tuition is {}".format(full))
	print("Price after deposit {}".format(post_fulldeposit))
	print("Monthly cost at full price {}"
	.format(fullprice))
	print("________________________")
	print("Early price of tuition is {}".format(early))
	print("Price after deposit {}".format(post_earlydeposit))
	print("Monthly cost at early price {}"
	.format(earlyprice))

elif method == "long":
	print("Input bootcamp cost")
	a = int(input())
	print("Input deposit amount")
	b = int(input())
	c = a - b
	d = c / 6
	print("Total cost after deposit {}"
	.format(c))
	print("Total monthly cost {}"
	.format(d))

else:
	print("[-] Error check spelling.")