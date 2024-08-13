import random

SYMBOLS = [" ◎ ", " △ ", " ▞ ", " ● ", " ▣ ", 
           " ▤ ", " ▲ ", " ▼ ", " * ", " < ",
           " > ", " = ", " ≡ ", " ☼ ", " ♦ ",
           " ◭ ", " ► ", " ◘ ", " ◓ ", " ▌ "]

def print_pattern(pattern):
    width = len(pattern[0])  - 1
    top_line = "┌" + "───┬" * width + "───┐"
    print(top_line)
    for i in range(len(pattern)):
        new_row = "│"
        for j in range(len(pattern[i])):
            new_row += pattern[i][j] + "│"
        print(new_row)
        if i != len(pattern) - 1:
            print("├" + "───┼" * width + "───┤")
    bottom_line = "└" + "───┴" * width + "───┘"
    print(bottom_line)


if __name__ == "__main__":
    pattern = create_background(15, 10, 2)
    pattern = add_h_stripe(pattern, 6, 4, 6)
    pattern = add_square(pattern, 6, 4, 4, 3)
    add_triangle_a(pattern, 8, 0, 4, 17)
    add_triangle_b(pattern, 4, 0, 4, 17)
    print_pattern(pattern)

