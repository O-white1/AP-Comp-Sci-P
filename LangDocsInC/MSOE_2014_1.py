def main():
    word = input("Enter Word: ")
    word = word.lower()

    dblcount = 0
    for lcv in range(0, len*(len(word)-1)):
        if word[lcv] == word[lcv+1]:
            dblcount += 1
    print(f"{word} contains {dblcount} double letters.")
    pass



if __name__ == "__main__":
    main()
