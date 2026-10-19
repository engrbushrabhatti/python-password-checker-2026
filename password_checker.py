import string

# Ask the user to enter a password.
password = input("Enter a password to check: ")

# Start by assuming each password requirement is not met.
has_uppercase = False
has_lowercase = False
has_number = False
has_special_character = False

# Check each character in the password.
for character in password:
    if character.isupper():
        has_uppercase = True
    if character.islower():
        has_lowercase = True
    if character.isdigit():
        has_number = True
    if character in string.punctuation:
        has_special_character = True

# Check whether the password is at least 8 characters long.
is_long_enough = len(password) >= 8

# Show which requirements the password meets.
print("\nPassword check:")
print("At least 8 characters:", is_long_enough)
print("Contains an uppercase letter:", has_uppercase)
print("Contains a lowercase letter:", has_lowercase)
print("Contains a number:", has_number)
print("Contains a special character:", has_special_character)

# Count how many password requirements are met.
score = 0
if is_long_enough:
    score += 1
if has_uppercase:
    score += 1
if has_lowercase:
    score += 1
if has_number:
    score += 1
if has_special_character:
    score += 1

# Give a strength rating based on the score.
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Moderate"
else:
    strength = "Strong"

print("\nPassword strength:", strength)

# Suggest ways to improve a password that is missing requirements.
if not is_long_enough:
    print("Suggestion: Use at least 8 characters.")
if not has_uppercase:
    print("Suggestion: Add an uppercase letter, such as A.")
if not has_lowercase:
    print("Suggestion: Add a lowercase letter, such as a.")
if not has_number:
    print("Suggestion: Add a number, such as 5.")
if not has_special_character:
    print("Suggestion: Add a special character, such as ! or #.")
