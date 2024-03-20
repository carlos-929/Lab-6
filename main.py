def encode_password(password):
    return ''.join(str((int(digit) + 3) % 10) for digit in password)


def decode_password(password):
    return ''.join(str((int(digit) - 3) % 10) for digit in password)

def menu():
    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        try:
            choice = int(input("Please enter an option: "))
            if choice == 1:
                password = input("Please enter your password to encode: ")
                if not password.isdigit() and len(password) != 8:
                    raise ValueError("Password must be an 8-digit integer.")
                encoded_password = encode_password(password)
                print("Your password has been encoded and stored!")
            elif choice == 2:
                original_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            elif choice == 3:
                break
            else:
                print("Invalid option! Please enter a valid option.")
        except ValueError as ve:
            print("Error:", ve)


def main():
    menu()


if __name__ == "__main__":
    main()

