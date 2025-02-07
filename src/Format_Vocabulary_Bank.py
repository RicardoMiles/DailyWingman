import sys
import re

# Import msvcrt for Windows-specific input handling
import msvcrt

def format_string(input_str):
    # Clean unwanted control characters
    input_str = input_str.replace("\x07", "").replace("\x1A", "").strip()

    # Ensure space after '=' if missing
    input_str = re.sub(r'=(\S)', r'= \1', input_str.strip())

    lines = input_str.split("\n")
    formatted_lines = []
    last_eq_index = -1  # Track last '=' position

    for i, line in enumerate(lines):
        if '=' in line:
            eq_pos = line.index('=')

            # Highlight text before '=' up to the closest previous newline
            if last_eq_index == -1:
                before_eq = line[:eq_pos].strip()
            else:
                before_eq = " ".join(lines[last_eq_index + 1:i]).strip() + " " + line[:eq_pos].strip()

            after_eq = line[eq_pos + 1:].strip()

            # Apply bold formatting
            formatted_line = f"**{before_eq.strip()}** = {after_eq}"

            last_eq_index = i  # Update last '=' position
        else:
            formatted_line = line

        formatted_lines.append(formatted_line)

    return "\n".join(formatted_lines)


def read_input_windows():
    print("Enter your text (Press Ctrl+Z then Enter to finish):")
    lines = []
    current_line = ""

    while True:
        char = msvcrt.getwche()  # Read character without waiting for newline

        if char == '\x1A':  # Ctrl+Z detected (EOF)
            break
        elif char == '\r':  # Enter key pressed
            lines.append(current_line)
            current_line = ""
            print()  # Move to the next line
        else:
            current_line += char

    # Append any remaining text
    if current_line:
        lines.append(current_line)

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])  # Read from command-line arguments
    else:
        # ✅ Use msvcrt for proper EOF detection on Windows
        input_text = read_input_windows().strip()

    if not input_text:
        print("\nNo input received. Exiting.")
        sys.exit(1)

    output_text = format_string(input_text)

    print("\nFormatted Output:\n")
    print(output_text)

    # Save formatted output for easy copy-paste
    with open("formatted_output.txt", "w", encoding="utf-8") as file:
        file.write(output_text)
    print("\nFormatted text saved as 'formatted_output.txt'. You can open and copy it from there.")
