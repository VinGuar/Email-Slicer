emailAddress = input("Enter your email address! ")

checker = True
sign = '@'
period = '.'

while checker:
    if sign or period in emailAddress:
        break;
    else:
        input("That is not a valid Email Address! Please enter a valid one. ")
        continue


