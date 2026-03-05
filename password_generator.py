import secrets
import string

def password_generator():
    print("Strong Password Generator")
    print()
    try: 
        lenght = int(input("Enter password length: "))

        if lenght < 4:
            print("Warning: For security reasons, password should be at least 8-12 characters.")
            return
    
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        all_characters = letters + digits + symbols

        password = ''.join(secrets.choice(all_characters) for _ in range(lenght))

        print("\n" + "="*30)
        print(f"Generated Password: {password}")
        print("="*30)

    except ValueError:
        print("Error: Please enter a valid numerical value.")

if __name__ == "__main__":
    password_generator()

