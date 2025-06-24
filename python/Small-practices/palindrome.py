word_to_check = input("Please write your word here!: ")
reversed_word = word_to_check[::-1]

if word_to_check == reversed_word:
    print("Your word is a palindrome")
else:
    print("Not a palindrome")
