import string
import getpass

def check_pwd(password):
    #pasword = getpass.getpass("Enter password:")
    strength  = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == '':
            wspace_count += 1
        else:
            special_count += 1

        if lower_count >=1:
            strength +=1
        if upper_count >=1:
            strength +=1
        if num_count >=1:
            strength +=1
        if wspace_count >=1:
            strength +=1
        if special_count >=1:
            strength +=1

        if strength ==1:
            remarks = "Very Bad"
        elif strength ==2:
            remarks = "Not a good password"
        elif strength ==3:
            remarks = "Weak password"
        elif strength ==4:
            remarks = "Good password"
        elif strength ==5:
            remarks = "Strong password"

        print("Your password has: ")
        print(f"{lower_count} lowercase characters")
        print(f"{upper_count} lowercase characters")
        print(f"{num_count} lowercase characters")
        print(f"{wspace_count} lowercase characters")
        print(f"{special_count} lowercase characters")

        print(f"Password strength:{strength}")

print("Welcom to password checker")

password = input("Enter your password:")

check_pwd(password)





