#define the menu of the restaurant
menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Burger": 60,
    "Salad": 60,
    "Coffee": 80,
}
print(menu)

#Greet Message

print("Welcome to New Generation Restaurant")
print("\npizza:Rs40\nPasta:Rs50\nBurger:Rs60\nSalad:Rs60\nCoffee:Rs80")

order_total = 0
item_1 = input("Enter the name of the item u want to order:")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"your item {item_1} has been added into your order")
else:
    print(f"Ordered item{item_1}is not available yet!")
another_order = input("Do u want to order something else?(Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of another item u want to order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Ordered item{item_2}has been added into your order")
    else:
        print(f"Ordered item{item_2}is not available yet!!")
    print(f"The total amount you have to pay is  {order_total} ")