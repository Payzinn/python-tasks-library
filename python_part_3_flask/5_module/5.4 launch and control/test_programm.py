import sys

def main():
    print("Stdout")
    print("Stder", file=sys.stderr)
    user_input = input('Vvod: ')
    print('User input: "{}"'.format(user_input))

if __name__ == "__main__":
    main()