import random

print("welcome to password generator!!! \n")

number_of_passwords_needed = int(input("How many passwords do you want to generate?"))
number_of_chars_in_password = int(input("how many characters would you prefer for your password?"))
def generate():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$"
    process = (random.choices(characters, k=number_of_chars_in_password))
    generated_password = ""
    for items in process:
        generated_password += str(items)
    print(generated_password)

generated_passwords = 0

while True:
    if generated_passwords < number_of_passwords_needed:
        generate()
        generated_passwords += 1
        continue

    else:
        break

