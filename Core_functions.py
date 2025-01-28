import re
import requests
import hashlib

class PsCheck:
    @staticmethod
    #Checks that password contains only allowed characters.
    def valid(password):
        invalid_terms = [' ', '/', ':', ';', '<', '>', '%', '*', '?', '|']
        for i in password:
            if i in invalid_terms:
                return False
        return True

    @staticmethod
    # checks that password includes all necessary variations.
    def basic(password,c = 0):
        criteria = {
            "Length(>=10)": len(password) >= 10,
            "Uppercase letter (A-Z)": bool(re.search(r'[A-Z]', password)),
            "Lowercase letter (a-z)": bool(re.search(r'[a-z]', password)),
            "Numbers (0-9)": bool(re.search(r'\d', password)),
            "Special Characters (!@#$%^&*(),.?\":{}|<>)": bool(re.search(r'[!@#$%^&*(),.?":{}|<>/]', password)),
        }

        feedback = []
        for key, value in criteria.items():
            if not value:
                feedback.append(key)

        # Print requirements
        if c == 0:
            for feed in feedback:
                print(feed)

        return len(feedback) == 0

    @staticmethod
    def moderate(password):
        # Hash the password using SHA-1
        sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_hash[:5], sha1_hash[5:]

        # Query the Pwned Passwords API with the hash prefix
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url)

        if response.status_code != 200:
            print("This service is not available at this moment")
            return False

        # Check if the suffix is in the response
        hashes = response.text.splitlines()
        for line in hashes:
            hash_suffix, count = line.split(':')
            if suffix == hash_suffix:
                print(f"oops ! Password has been compromised {count} times!\n")
                return False

        print("Password is not breached.\n")
        return True