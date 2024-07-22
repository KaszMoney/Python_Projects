

def remove(simple_url):
    return simple_url.removeprefix('https://')

#Can add in further implementation to figure out if there is proper input or not

def main():
    string = input("Enter a url ")
    print(remove(string))


if __name__ == "__main__":
    main()