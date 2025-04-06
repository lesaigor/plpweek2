# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

#Print the final price after applying the discount, or if no discount was applied, print the original price.
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price < original_price:
    print(f"Discount applied {final_price:.2f}")
else:
    print(f"No discount applied {original_price:.2f}")