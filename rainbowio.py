def print_rgb(color, text):
    match color:
        case "red":
            print(f"\033[91m{text}\033[0m")
        case "green":
            print(f"\033[92m{text}\033[0m")
        case "blue":
            print(f"\033[94m{text}\033[0m")

def input_rgb(color, text):
    match color:
        case "red":
            return input(f"\033[91m{text}\033[0m")
        case "green":
            return input(f"\033[92m{text}\033[0m")
        case "blue":
            return input(f"\033[94m{text}\033[0m")

def logo():
    print_rgb("blue", "-" * 20)
    print_rgb("green", "|  reminder-words  |")
    print_rgb("blue", "-" * 20)
