import sys
import typing


def main() -> None:
    error = 0
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f: typing.TextIO
        with open(sys.argv[1], "r") as file:
            read = file.read()
            print(f"---\n\n{read}\n---")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        error = 1
    finally:
        if not error:
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
