import os
import tkinter as tk
from tkinter import filedialog
from Core_functions import PsCheck
psc = PsCheck()

# Creating interface
print("\nWelcome to Password Strength Checker !!\n")
print("What would you like to do today")

while True:
    print("1. Check if a password is safe to use.")
    print("2. Check a list of passwords from a file and classify them as weak, string and invalid.")
    print("3. Check if a password is breached.")
    print("4. Exit.")
    print("Enter your choice as number.")

    # Handling exception
    try:
        ch = int(input())
    except:
        ch = 4

    # Single password check
    if ch == 1:

        # Makes sure password is entered
        psw = ""
        while len(psw) <= 1:
            psw = input("Enter password\n")

        # valid password check
        if psc.valid(psw):
            print("Your password is valid")

            # All Criteria fulfilled
            if psc.basic(psw):
                print("Your password passes all basic Criterion")

                # Password is not compromised
                if psc.moderate(psw):
                    print("WOW ! Your password is safe to use.\n")
                else:
                    print("Your password is correctly formed but has been compromised in previous breaches.\n")
            else:
                print("Your password needs to work on above criterion.\n")
        else:
            print("Your password contains invalid character.\n")

    # List of passwords categorisation
    elif ch == 2:
        # Choosing the file
        # Initialize the Tkinter root
        root = tk.Tk()
        # Hide the root window
        root.withdraw()
        # Open the file dialog GUI to select txt files
        fpath = filedialog.askopenfilename(
            title="Select the file",
            filetypes=[("Text Files","*.txt")]
        )

        # File selected
        if fpath:
            with open (fpath,encoding="utf-8") as file:
                weak,strong,invalid = [],[],[]
                for psw in file.readlines():
                    psw = psw.strip()
                    if not psc.valid(psw):
                        invalid.append(psw+"\n")
                    elif not psc.basic(psw,1):
                        weak.append(psw+"\n")
                    else:
                        strong.append(psw+"\n")

            # get parent directory
            rpath = os.path.dirname(fpath)
            # Creates file for Strong passwords
            with open (rpath + "/strong_passwords.txt", 'w',encoding="utf-8") as str:
                for i in strong:
                    str.write(i)
            str.close()

            # Creates file for weak passwords
            with open (rpath + "/weak_passwords.txt", 'w',encoding="utf-8") as wk:
                for i in weak:
                    wk.write(i)
            wk.close()

            # Creates file for invalid passwords
            with open (rpath + "/invalid_passwords.txt", 'w',encoding="utf-8") as iv:
                for i in invalid:
                    iv.write(i)
            iv.close()

            file.close()

            print("Files named : \n")
            print("strong_passwords.txt")
            print("weak_passwords.txt")
            print("invalid_passwords.txt Has been created....\n")
        else:
            print("No file selected.")
            print("Exiting...\n")

    # Checks if password is breached
    elif ch == 3:

        psw = ""
        while len(psw) == 0:
            psw = input()

        psc.moderate(psw)

    elif ch == 4:
        break

    else:
        print("Invalid selection Try Again !\n\n")

print("Checkin Again !!")