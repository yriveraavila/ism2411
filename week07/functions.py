#======================================================================================================================================================#

#Self Assessment 1: I only noticed the error after asking AI, which says that my current debugging insticts are not strong enough. I need to practice
# more debugging exercsises to improve, especially before the midterm.

#Self Assessment 2: It seems the code takes the customers price and tier of discount that is available for said customer, and then returns the price
# after the discount and tax has been applied. A colleauge could use this code, as long as they are given appropriate names and information about the 
# about the customer.

#Self Assessment 3: I used ChatGPT to help me debug the coding by explaining the erros found in the code, so that I could understand what steps I could
# take to the fix the code. The usage of ChatGPT actually expanded my understanding on how to debug the code because I didn't ask directly how to fix
# it, but rather, asked for an explanation of what the errors meant, which allowed me to come up with solutions to those errors.

#======================================================================================================================================================#

#-------------------- Exercise 1: calculate_tax ----------------------------------------------------------------------------#

def calculate_tax(price, rate):
    return price *rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#-------------------- Exercise 2: apply_discount -------------------------------#

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier =="silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#-------------------- Exercise 3: Compose them ----------------------------------#

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#-------------------- Exercise 4: Loop + function -------------------------------#

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} |Total: ${total:.2f}")

#-------------------- Exercise 5: Debug First, Then Ask ------------------------------------------------------------#

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:   # The first bug is 'SyntaxError: expected ':'', the reason for this is the semicolon
     count += 1      # missing in the for loop part of 'for sale in sales'. 
print(f"Count: {count}")

i = 0
while i < len(sales):    # The second bug is 'IndexError: list index out of range', 
    print(sales[i])      # the reason for this is that the loop stops before i reaches 5, 
    i += 1               # there is no index 5 in the sales list according to python, therefore,
                         #  the loop should be 'while i < len(sales):

                         # The third bug is 'IndentationError: unindent does no match any 
                         # outer indentation level', the reason for this is that the print statement
                         # is not indented properly, it should be indented to the match the while loop.
                      
    #-------------------- Exercise 6: Scope experiment ------------------------------#

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)


