ch=input()
n = ord(ch)
if (ch.isalpha()):
    if n==97 or n==101 or n==105 or n==111 or n==117 or n==65 or n==69 or n==73 or n==79 or n==85:
        print("Vowel.")
    else:
        print("Consonant.")
else:
    print("Not an alphabet.")
    