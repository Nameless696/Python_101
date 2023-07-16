print("Welcome to the pizza shop ")
print()

def take_order():
    customer_name = input("Enter your name: ")
    print()
    
    print("Pizza Menu:")
    print("1. Cheese")
    print("2. Chicken")
    print("3. Ham")
    print("4. Veggie")
    print("5. Custom Pizza")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 5:
        toppings = select_toppings()
        pizza = "Custom Pizza with " + ', '.join([topping[0] for topping in toppings])
        calculate_bill(customer_name, pizza, toppings)
    else:
        pizzas = ["Cheese", "Chicken", "Ham", "Veggie"]
        pizza = pizzas[choice - 1]
        calculate_bill(customer_name, pizza)

def select_toppings():
    print("Available toppings:")
    print("1. Pepperoni - RS 20")
    print("2. Mushrooms - RS 15")
    print("3. Onions - RS 10")
    print("4. Bell Peppers - RS 15")
    print("5. Pork - RS 80")
    print("6. Spinach - RS 15")
    print("7. Tomatoes - RS 10")
    print("8. Extra Cheese - RS 20")

    num_toppings = int(input("How many toppings do you want? :  "))
    toppings = []

    topping_prices = {
        1: 20,
        2: 15,
        3: 10,
        4: 15,
        5: 80,
        6: 15,
        7: 10,
        8: 20
    }

    for _ in range(num_toppings):
        topping_choice = int(input("Enter topping choice (1-8): "))
        if 1 <= topping_choice <= 8:
            topping_name = get_topping_name(topping_choice)
            topping_price = topping_prices[topping_choice]
            toppings.append((topping_name, topping_price))

    return toppings

def get_topping_name(topping_choice):
    topping_names = {
        1: "Pepperoni",
        2: "Mushrooms",
        3: "Onions",
        4: "Bell Peppers",
        5: "Pork",
        6: "Spinach",
        7: "Tomatoes",
        8: "Extra Cheese"
    }
    return topping_names[topping_choice]

def calculate_bill(customer_name, pizza, toppings=None):
    prices = {
        "Cheese": 350,
        "Chicken": 250,
        "Ham": 450,
        "Veggie": 200
    }
    topping_price = 1

    if pizza.startswith("Custom Pizza"):
        topping_total = sum([topping[1] for topping in toppings])
        base_price =  200
        bill = base_price + topping_total
    else:
        bill = prices[pizza]

    print(f"Your Total Bill is : RS{bill}")

    save_order(customer_name, pizza, bill)

def save_order(customer_name, pizza, bill):
    order = f"Customer Name: {customer_name}\nPizza: {pizza}\nBill: RS{bill}\n"

    with open("orders.txt", "a") as file:
        file.write(order)

    print("Order saved!")

def main():
    take_order()

if __name__ == "__main__":
    main()
