"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# Create a dictionary to store the products and their costs
products = {
"Product 1": 10,
"Product 2": 20,
"Product 3": 30,
"Product 4": 40
}
# Initialize the total cost to 0
total_cost = 0
# Start the while loop
while True:
    # Ask the user if they want to make a purchase
    purchase = input("Do you want to make a purchase? (Yes/No) ")
    # If the user does not want to make a purchase, exit the loop
    if purchase.lower() != "yes":
        break
    # Present the user with the menu of options
    print("Menu:")
    for i, (product, cost) in enumerate(products.items()):
        print(f"{i+1}. {product}: {cost}")
    # Prompt the user to select a product
    selection = input("Enter the number of the product you want to purchase: ")
    # Get the selected product and cost from the dictionary
    selected_product = list(products.keys())[int(selection) - 1]
    selected_cost = products[selected_product]
    # Prompt the user to enter the quantity
    quantity = int(input("Enter the quantity: "))
    # Add the cost of the selected product to the total cost
    total_cost += selected_cost * quantity
    # Ask the user if they want to continue shopping
    continue_shopping = input("Do you want to continue shopping? (Yes/No) ")
    # If the user does not want to continue shopping, exit the loop
    if continue_shopping.lower() != "yes":
        break
# Print the total cost
print(f"Total cost: {total_cost}")