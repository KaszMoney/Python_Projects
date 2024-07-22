

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

if __name__ == "__main__":
    main()