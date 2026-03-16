import re


def main():
    name = input("Enter your first name followed by last name, using capital letters for each name: ")
    postal_code = input("Enter your postal code: ")

    regex_name = r'[A-Z][a-z]{2,}\s[A-Z][a-z]+'
    regex_postal_code = r'[A-Za-z]\d[A-Za-z]\s?[0-9][A-Za-z]\d'

    name_match = re.match(regex_name, name)
    postal_code_match = re.match(regex_postal_code, postal_code)

    if not name_match:
        print("Invalid Name")
    if not postal_code_match:
        print("Invalid Postal Code")

if __name__ == '__main__':
    main()