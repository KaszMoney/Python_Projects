
def main():
    cars = ['bmw', 'audi', 'toyota', 'subaru', 'ford']
    print(cars)
    print(sorted(cars))
    print(cars)
    cars.sort()
    print(cars)


    for car in cars:
        car = car.title()
        print(car)


if __name__ == "__main__":
    main()