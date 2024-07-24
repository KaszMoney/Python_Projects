

def main():
    players = ['charles', 'martina', 'micheal', 'florence', 'eli']
    print(players[0:3])
    #Slicing starts at the first listed number and ends at the second one
    #Must remember the fact that indexes start at 0 and are shifted
    #If the first number is not included then shifting will begin at the first entry in the list
    #If the second number is not included, then the slice will include all entries after the given index
    print(players[2:])
    #prints the third, fourth, and fifth elements in the list  

    #Using negative indexes can give you elements from the end of the list without knowing the lenght of the list
    print(players[-3:])
    #Also prints the 3rd, 4th, and 5th elements in the list 

    print("Here are the first three players on my team: ")
    for player in players[:3]:
        print(player.title())

if __name__ == "__main__":
    main()