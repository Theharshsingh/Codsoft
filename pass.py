import random
import string

def generate_password(length):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation


    all_characters = lowercase + uppercase + digits + special_characters

   
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
   
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
            elif length > 128:
                print("Password length should not exceed 128 characters.")    
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

   
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
