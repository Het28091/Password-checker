# Password Strength Checker


---

This project contains simple functions to check whether a password is secure to use. It has two Python files containing functions that accurately perform the required computations.

### Tech Stack

#### Language
- Python (main programming language)

#### Imports
1. `tkinter` - Helps in selecting the password file easily.
2. `requests` - Used to get API responses.
3. `hashlib` - Encodes and decodes in SHA-1.
4. `unicodedata` - Checks for symbols and emojis.
5. `math` - Used for entropy calculations.
6. `re` - Checks character inclusions.
7. `os` - Helps with file locating.

## Core_functions.py

This file contains the following functions within the `PsCheck` class:

1. **`valid()`**  
   This function ensures that passwords do not contain any invalid characters. It employs a simple brute-force method by comparing each character of the password against a list of invalid characters. Additionally, it checks for any symbols or emoji characters.

2. **`basic()`**  
   This function verifies whether the password meets five criteria, along with an entropy check. The five criteria are:
   - Length
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Special characters

   Entropy is calculated using another function that returns a percentage value representing the randomness of the password. If a password meets at least three of the five criteria and has entropy greater than 40%, it is considered strong. These thresholds were manually chosen by testing various password lists.

3. **`moderate()`**  
   This function checks if the password has been compromised in any previous breaches. It utilizes the "Have I Been Pwned" API to gather data. The security of the entered password is maintained by only sending the first five characters of the SHA-1 hashed password to the API. The returned list of hashes is then checked for a match.

4. **`entropy_cal()`**  
   This function calculates the entropy of a password using Shannon's formula and returns the entropy percentage.

## Main.py

This Python file creates a user-friendly CLI interface, allowing users to select the operations they want to perform:

1. Check a single password.
2. Check a list of passwords and categorize them as **strong**, **weak**, or **invalid**.
3. Check if a password has been breached.

A list of passwords can be checked by storing them in a `.txt` file. The categorization results will also be saved in `.txt` files.