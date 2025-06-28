import random
import string

def create_password(length, include_upper, include_lower, include_numbers, include_symbols):
    """Create a random password based on user choices."""
   
    # Start with an empty string for the characters
    characters = ""
    
    # Add character types based on user choices
    if include_upper:
        characters += string.ascii_uppercase 
    if include_lower:
        characters += string.ascii_lowercase  
    if include_numbers:
        characters += string.digits         
    if include_symbols:
        characters += string.punctuation      
    # Check if at least one character type is selected
    if not characters:
        return "Please choose at least one type of character."
    
    # Create the password
    password = []
    
    
    if include_upper:
        password.append(random.choice(string.ascii_uppercase))
    if include_lower:
        password.append(random.choice(string.ascii_lowercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice(string.punctuation))
    

    for _ in range(length - len(password)):
        password.append(random.choice(characters))
    
    # Shuffle the password to mix the characters
    random.shuffle(password)
    
    return ''.join(password)  # Join the list into a single string

def main():
    print("🔒 Welcome to the Simple Password Generator 🔒")
    
    # Ask the user for the password length
    length = int(input("Enter the password length (8-128): "))
    while True:
        if 8 <= length <= 128:
            break
        else:
            length = int(input("Invalid length. Please enter a length between 8 and 128: "))
    
    # Ask the user what types of characters to include
    include_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
    include_lower = input("Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers (0-9)? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols (!@#$%^&*)? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = create_password(length, include_upper, include_lower, include_numbers, include_symbols)
    
    # Show the generated password
    print("\nYour Generated Password:")
    print(password)

if __name__ == "__main__":
    main()


      