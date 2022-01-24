SECURE = (('A', '/|'),('a','@'),('h','4'),('u','!_!'),('l','|'))

def passwordsecure(password):
    for a,b in SECURE:
        password = password.replace(a,b)

    return password    

password = input("Please provide your password here: ") 
decision = input("Do you need UPPER case letters to be present? (y/n): ")   

if decision == 'y':
    print(f"Your new password is {passwordsecure(password)}")
else:
    print(f"Your new password is {passwordsecure(password.lower())}")

    