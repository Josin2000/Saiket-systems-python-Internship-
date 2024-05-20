def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except IOError:
        print(f"Error: An IOError occurred while reading the file at {file_path}.")
        return None

def write_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
        print(f"Data successfully written to {file_path}.")
    except IOError:
        print(f"Error: An IOError occurred while writing to the file at {file_path}.")

def find_and_replace(data, target, replacement):
    return data.replace(target, replacement)

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'
    target_word = input("Enter the word to be replaced: ")
    replacement_word = input("Enter the replacement word: ")

    
    data = read_file(input_file)
    if data is not None:
       
        updated_data = find_and_replace(data, target_word, replacement_word)
        
        
        write_file(output_file, updated_data)

if __name__ == "__main__":
    main()
