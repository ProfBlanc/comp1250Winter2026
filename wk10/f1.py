import re

def main():
    text = "My phone number is 416-415-2000"
    regex1 = r'[0-9]+-\d{2,}-[0-9]{4}'

    # hits = re.findall(pattern=regex1, string=text)  # search the entire string
    # print(hits)
    regex2 = r'[^\d]+[0-9]+-\d{2,}-[0-9]{4}$'
    # match the entire string from the begining
    matches = re.match(pattern=regex2, string=text)
    if matches:
        print(matches)  # match object
        print(matches.group()) # result of the match
    else:
        print("No matches")

if __name__ == "__main__":
     main()