def secure_archive(
    file_name: str, mode: str, content: str
) -> tuple[bool, str]:
    error = True
    message = ""
    read = ""
    try:
        with open(file_name, mode) as file:
            if "r" in mode:
                read = file.read()
            if "w" in mode:
                file.write(content)
    except FileNotFoundError:
        error = False
        message = f"[Errno 2] No such file or directory: '{file_name}'"
        print("Using 'secure_archive' to read from a nonexistent file:")
    except PermissionError:
        error = False
        message = f"[Errno 13] Permission denied: '{file_name}'"
        print("Using 'secure_archive' to read from an inaccessible file:")
    except Exception:
        error = False
        print("Using 'secure_archive' to Unknom!:")

    if "r" in mode and error:
        message = read
        print("Using 'secure_archive' to read from a regular file:")
    elif "w" in mode and error:
        message = content
        print(
            "Using 'secure_archive' to write previous content to a new file:"
        )
    return error, message


def main() -> None:
    print("=== Cyber Archiven Security ===\n")
    print(secure_archive("happy", "r", "i love!"), end="\n\n")
    print(secure_archive("/etc/master.passwd", "r", ":D"), end="\n\n")
    print(secure_archive("valid_file.txt", "r", "potato"), end="\n\n")
    print(secure_archive("valid_file2.txt", "w", "I like banana!\n"))


if __name__ == '__main__':
    main()
