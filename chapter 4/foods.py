def main():
    my_foods = ['pizza', 'chicken', 'pasta']
    friend_foods = my_foods[:]

    print(my_foods)
    print(friend_foods)

    my_foods.append('burger')
    friend_foods.append('brisket')

    print(my_foods)
    print(friend_foods)


if __name__ == "__main__":
    main()