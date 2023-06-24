from io import TextIOWrapper
import os.path
import sys

# Default file name if none provided
file_name: str = "default.txt"
file_handle: TextIOWrapper
file_contents: list[str] = []


# TODO: Add a prompt option
def show_help() -> None:
    """Print help message and exit normally."""
    print("Usage: pyhelp [options] [file]\n")
    print("Ed inspired editor written in Python.\n")
    print("Options:")
    print(" -h  --help   Prints this help message")
    sys.exit(0)


def create_open_file(file) -> None:
    """
    Create the file if it does not exist or open it.
    Args:
        file: The file to open or create
    """
    global file_name
    global file_handle

    # Check if the file exists
    if not os.path.isfile(file_name):
        # Ed will warn that the file does not exist
        # but will allow you to continue anyway
        print(f"{file} no such file or directory.")
        # Create the file in read and write mode
        file_handle = open(file, "w+")
    else:
        # Open file in read and append mode
        file_handle = open(file, "a+")


def edit_file() -> None:
    """Take user input and append to gloabl file_contents."""
    global file_contents
    while True:
        line = input()
        # Start a command
        if line == ".":
            command_mode()
        # Append the line to the files file_contents
        else:
            file_contents.append(line + "\n")


def write_file() -> None:
    """Write the file to disk."""
    global file_handle
    global file_contents

    # Write the file to disk
    file_handle.writelines(file_contents)
    # Close the file
    file_handle.close()


def command_mode() -> None:
    """Enter command mode."""
    while True:
        # TODO: Respect prompt once implemented
        command = input("")
        # Quit without saving
        if command == "q":
            sys.exit(0)
        # Write the file
        elif command == "w":
            write_file()
        # Write the file and quit
        elif command == "wq":
            write_file()
            sys.exit(0)
        # Go back to editing
        elif command == "a":
            edit_file()
        else:
            print("?")


if __name__ == "__main__":
    args = sys.argv[1:]

    # If no arguments show the help documentation
    if len(args) == 0:
        show_help()
    # If the user provides the help flags
    elif args[0].lower() == "-h" or args[0].lower() == "--help":
        show_help()
    # Assume a file was passed
    else:
        create_open_file(args[0])
        command_mode()
