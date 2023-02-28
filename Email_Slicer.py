emailAddress = input("Enter your email address! ")

checker = True
sign = '@'
period = '.'
username = ""
domain = ""
counter = 0
locationOfSign = 0

while True:
    if sign and period in emailAddress:
        break
    else:
        input("That is not a valid Email Address! Please enter a valid one. ")
        continue

while counter<len(emailAddress):
    if emailAddress[counter] == "@":
        counter += 1
    elif counter>locationOfSign:
        domain += emailAddress[counter]
    else:
        username += emailAddress[counter]

print("Your username is " + username + ". Your domain is " + domain + ". ")
