
def main():
    alien_0 = {'color': 'green', 'points': 5}

    print(alien_0)

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25

    print(alien_0)
    print(alien_0['x_position'])

    speed_value = alien_0.get('speed', 'No speed value assigned')
    print(speed_value)
    #If there's a chance that the key you're looking for might not exist, then use the get() methd instead of square brackets

    for key, value in alien_0.items():
        print(f"\nKey: {key}")
        print(f"\nKey: {value}")

if __name__ == "__main__":
    main()