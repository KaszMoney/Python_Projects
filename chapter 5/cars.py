
def main():
    cars = ['bmw', 'audi', 'toyota', 'subaru', 'ford']
    
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())


if __name__ == "__main__":
    main()