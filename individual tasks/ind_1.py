def starts_with_vowel(word):
    vowels = "aeiouAEIOU"
    return word[0] in vowels


def main():
    file_name = input("Enter the name of the file: ")

    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()

            print("Words starting with vowels:")
            for word in words:
                if starts_with_vowel(word):
                    print(word)
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")


if __name__ == "__main__":
    main()
