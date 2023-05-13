# Password system for Python written by Bladeskies

import time

services_enabled = True

if services_enabled == True:
    print("What text information would you like to store?")
    priv_info = input("[$] ")

    print("Successfully stored.")
    time.sleep(1)

    print("What would you like to set as the password?")
    pass_key = str(input("[$] "))

    time.sleep(2)
    print("You have been locked out of your account.")

    time.sleep(1)
    print("What is the password for your account?")
    attempt = input("[$] ")

    if attempt == pass_key:
        print("Access granted!")
        time.sleep(2)

        print("Stored information: " + priv_info)
        time.sleep(2)

    else:
        print("Access denied.")
        time.sleep(2)
