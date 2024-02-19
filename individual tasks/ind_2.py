def add_sequence_numbers(source_file, target_file):
    try:
        with open(source_file, 'r') as source:
            lines = source.readlines()

            with open(target_file, 'w') as target:
                for i, line in enumerate(lines, start=1):
                    target.write(f"{i}: {line}")
        
        print(f"Sequence numbers added and saved to {target_file} successfully.")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

def main():
    source_file = input("Enter the name of the source file: ")
    target_file = input("Enter the name of the target file: ")

    add_sequence_numbers(source_file, target_file)

if __name__ == "__main__":
    main()
