def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except PermissionError as err:
        print("Problem trying to access. Error: " + str(err))

if __name__ == '__main__':
    main()