

customer_name = input("Enter customer name: ")

product1 = input("Enter name of Product 1: ")
price1 = float(input("Enter price of Product 1: "))

product2 = input("Enter name of Product 2: ")
price2 = float(input("Enter price of Product 2: "))

product3 = input("Enter name of Product 3: ")
price3 = float(input("Enter price of Product 3: "))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0

discount = subtotal * discount_rate
final_total = subtotal - discount

print(f"\nCustomer Name: {customer_name}")

print(f"\nProduct 1: {product1}")
print(f"Price: {price1}")

print(f"\nProduct 2: {product2}")
print(f"Price: {price2}")

print(f"\nProduct 3: {product3}")
print(f"Price: {price3}")

print(f"\nSubtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")
