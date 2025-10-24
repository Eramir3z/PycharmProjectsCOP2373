import re

def get_sentences(x):
# using the code from chapter 7, I included '0-9' that way it could
# capture sentences starting with letters/numbers
    return re.findall(r"[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)", x, flags=re.DOTALL | re.MULTILINE)

def main():
# will be helpful when numbering is needed
    count = 0
# get input
    paragraph = input("Enter a paragraph: ")
# call function
    sentences = get_sentences(paragraph)
# a simple way to numerically list each sentence found
    for i in sentences:
        count+=1
        print(f"{count}.",i)
    print(f"There are {count} total sentences.")
# call main
if __name__ == '__main__':
    main()