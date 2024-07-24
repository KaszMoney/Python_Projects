
def main():
    available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    
    print("\n We finished making your pizza!")

    #The available_toppings data structure would be much better and have better time complexity for out function if it were a set

if __name__ == "__main__":
    main()