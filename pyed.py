import os.path
import sys


# TODO: Add a prompt option
def show_help() -> None:
    """Print help message and exit normally."""
    print("Usage: pyhelp [options] [file]\n")
    print("Ed inspired editor written in Python.\n")
    print("Options:")
    print(" -h  --help   Prints this help message")
    sys.exit(0)


def edit_file(file) -> None:
    """Open the file in the editor."""

    # Check if the file exists
    if not os.path.isfile(file):
        print(f"{file} no such file or directory.")
        file = open(file, "w+")  # Create the file
    else:
        # Open file
        file = open(file, "a+")

    # Open the file in the editor
    editing: bool = True
    lines: list = []
    while editing:
        command = input("")
        if command == ".":
            print("Done editing")
            for line in lines:
                file.write(line + "\n")
            file.close()
            editing = False
        else:
            lines.append(command)
    print("done")


if __name__ == "__main__":
    args = sys.argv[1:]

    # If no arguments show the help documentation
    if len(args) == 0:
        show_help()
    # If the user provides the help flags
    elif args[0] == "-h" or args[0] == "--help":
        show_help()
    # Assume a file was passed
    else:
        edit_file(args[0])
