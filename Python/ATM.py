import getpass
import os

PIN_LENGTH = 4
ACCOUNT_NUMBER_MIN_LENGTH = 8
ACCOUNT_NUMBER_MAX_LENGTH = 18


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def is_valid_account_number(account_number):
    return (
        account_number.isascii()
        and account_number.isdigit()
        and ACCOUNT_NUMBER_MIN_LENGTH <= len(account_number) <= ACCOUNT_NUMBER_MAX_LENGTH
    )


def is_valid_pin(pin):
    return pin.isascii() and pin.isdigit() and len(pin) == PIN_LENGTH


def main():
    clear_screen()
    print("Welcome to the ATM")
    print("-------------------")

    while True:
        account_number = input("Enter Account Number: ").strip()
        if is_valid_account_number(account_number):
            break
        print(
            f"Enter digits only ({ACCOUNT_NUMBER_MIN_LENGTH}-"
            f"{ACCOUNT_NUMBER_MAX_LENGTH} digits)."
        )

    while True:
        pin = getpass.getpass("Enter your 4-digit PIN: ")
        if is_valid_pin(pin):
            break
        print(f"PIN must contain exactly {PIN_LENGTH} digits.")

    clear_screen()
    print("Account details accepted.")
    print(f"Account Number: {'*' * (len(account_number) - 4)}{account_number[-4:]}")
    print("PIN: hidden")
    input("\nPress Enter to clear the screen...")
    clear_screen()


if __name__ == "__main__":
    main()
