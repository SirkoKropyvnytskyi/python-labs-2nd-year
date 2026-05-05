def log_error_to_file(error_text):
    with open("error_log.txt", "a", encoding="utf-8") as file:
        file.write(error_text + "\n")

def main():
    user_input = input("Enter number to convert from string to number: ")

    try:
        number = float(user_input)
        
    except ValueError:
        error_message = f"ERROR: Cannot convert '{user_input}' to a number."
        print(error_message)
        
        log_error_to_file(error_message)
        
    else:
        print(f"Result of conversion: {number}")
        
    finally:
        print("Program execution completed.")

if __name__ == "__main__":
    main()