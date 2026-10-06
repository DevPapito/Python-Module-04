import sys
import typing


def transform_data(read: str) -> str:
    line = ""
    for word in read.splitlines():
        line += f"{word}#\n"
    return line


def main() -> typing.Optional[None]:
    error = 0
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    read = ""
    try:
        with open(sys.argv[1], "r") as file:
            read = file.read()
            print(f"---\n\n{read}\n---")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        error = 1
    finally:
        if not error:
            print(f"File '{sys.argv[1]}' closed.")
    if error:
        return
    new_read = transform_data(read)
    print("Transform data:")
    print(f"---\n\n{new_read}\n---")
    user_input = input("Enter new file name (or empty): ")
    if not len(user_input):
        print("No saving data.")
        return
    error = 0
    try:
        with open(user_input, "x") as file:
            file.write(new_read)
    except Exception as e:
        error = 1
        print(f"Error opening file '{user_input}': {e}")
    finally:
        if not error:
            print(f"Data saved in file '{user_input}'")
        else:
            print("Data not saved.")


if __name__ == '__main__':
    main()
