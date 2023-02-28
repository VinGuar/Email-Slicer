emailAddress = input("Enter your email address! Both Internet and Intranet emails are valid. ")

checker = True
sign = '@'
username = ""
domain = ""
counter = 0

while True:
    if ((sign in emailAddress) and emailAddress.rfind("@")>0 and (len(emailAddress)-1)>emailAddress.rfind("@")):
            break
    else:  
        emailAddress = input("That is not a valid Email Address! Please enter a valid one. ")

        
locationOfSign = emailAddress.rfind("@")

while counter<len(emailAddress):
    if counter == locationOfSign:
        counter += 1
    elif counter>locationOfSign:
        domain += emailAddress[counter]
        counter += 1
    else:
        username += emailAddress[counter]
        counter += 1

print("Username: " + username + "      Domain: " + domain)
