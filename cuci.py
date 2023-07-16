
def take_order():
    customer_name = input("Enter your name: ")
    print("Pizza Menu:")
    print("1. Cheese")
    print("2. Chicken")
    print("3. Ham")
    print("4. Veggie")
    print("5. Custom Pizza")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 5:
        toppings = input("Enter toppings : ")
        pizza = "Custom Pizza with " + toppings
    else:
        pizzas = ["Cheese", "Chicken", "Ham", "Veggie"]
        pizza = pizzas[choice - 1]
        
    print(f"You ordered: {pizza}")
    calculate_bill(customer_name, pizza)
    
def calculate_bill(customer_name, pizza):
    prices = {
        "Cheese": 199,
        "Chicken": 250,
        "Ham": 150,
        "Veggie": 180,
        "Custom Pizza": 299
    }
    topping_price = 1
    toppings_count = 0
    
    if pizza == "Custom Pizza":
        toppings = input("Enter toppings : ")
        toppings_count = len(toppings.split(","))
        
    bill = prices[pizza] + (topping_price * toppings_count)
    print(f"Bill: ${bill}")
    
    save_order(customer_name, pizza, bill)
    
def save_order(customer_name, pizza, bill):
    order = f"Customer Name: {customer_name}\nPizza: {pizza}\nBill: ${bill}\n"
    
    with open("orders.txt", "a") as file:
        file.write(order)
    
    print("Order saved!")
    
def main():
    take_order()
    
if __name__ == "__main__":
    main()