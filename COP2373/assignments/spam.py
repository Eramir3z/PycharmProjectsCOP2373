#get the email
#scan the email
#tally points on spam
#rate likelihood if spam
#display: score, likelihood, and spam words

def spam_score(email, spam_words):
    score = 0
    flagged_words = []

    for word in spam_words:
        if word in email:
            score += email.count(word)
            flagged_words.append(word)
    return score, flagged_words

def spam_likelihood(score):
    if score == 0:
        return "Not a spam email"
    elif score <= 3:
        return "Not likely to be a spam email"
    elif score <= 6:
        return "Very likely to be spam email"
    else:
        return "This is a spam email"


def main():
    spam_words = ["free", "winner", "urgent", "congratulation", "prize", "limited", "guarantee", "click", "offer",
                  "exclusive", "risk", "won", "cash", "bonus", "cheap", "discount", "debt", "loan", "lottery",
                  "million", "deal", "instant", "credit", "money", "gift", "apply", "promise", "investment", "miracle",
                  "now"]

    email = input("Enter your e-mail: ").lower()
    score, words_found = spam_score(email, spam_words)
    decision = spam_likelihood(score)

    print(f"The email scored {score} points")
    print(decision)
    if words_found:
        print(f"Here are the flagged words that were picked up: {words_found}")
    else:
        print("There were no flagged words in the email")

if __name__ == "__main__":
        main()