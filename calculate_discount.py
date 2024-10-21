# Function to calculate the final price after applying the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Apply the discount
        return final_price
    else:
        return price  # Return the original price if no discount is applied

# Prompt the user to enter the original price and the discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price == price:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
