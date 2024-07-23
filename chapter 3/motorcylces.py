

def main():
    motorcyles = ['suzuki', 'yamaha', 'harley']
    print(motorcyles)
    motorcyles.append('ducati')
    print(motorcyles)
    motorcyles.insert(0, 'honda')
    print(motorcyles)

    del motorcyles[2]
    print(motorcyles)

    popped_motorcycles = motorcyles.pop()
    print(popped_motorcycles)
    length = len(motorcyles)
    middle = length // 2
    motorcyles.insert(middle, 'bossman')
    print(motorcyles)

if __name__ == "__main__":
    main()