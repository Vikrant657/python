s=input("Enter the E-mail address:")

if s[0] not in ("qwertyuiopasdfghjklzxcvbnm"):
    print("Invalid input") #As the first letter of the email id should be a alphabet
elif "@" not in s:
    print("Invalid input,@ is missing") #if Email id will not contain @ then it will display a massage that” @ is missing”
elif "gmail.com" not in s:
    print("Invalid input,gmail.com is missing") #if Email ID will not contain “gmail.com” then it  will display a massage -“gamil.com is missing”
else:
    a=s.split('@')
    print("Username:",a[0])
    print("domain:",a[1].upper())
