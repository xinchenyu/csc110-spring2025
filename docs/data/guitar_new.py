def print_head():
    print("      ___")
    pattern = "    o|* *|o"
    print(pattern)
    print(pattern)
    print(pattern)
    print("     \===/")

def print_retro_head():
    print("     ._-_.")
    print("    +|\G/|+")
    pattern = "    +|\./|+"
    print(pattern)
    print(pattern)
    print("     \===/")

def print_neck():
    print("      |||" + "\n" + "      |||")
    
def print_body():
    print("   ___|||___")
    pattern = "  /   |||   \ " + "\n" + " /    |||    \ " 
    print(pattern)
    print("|     |||     |")
    print(" \   (|||)   /")
    print("  |   |||   |")
    print(pattern)
    print("/     |||     \ ")
    print("|    [===]    |")
    print(" \           /")
    print("  '.       .'")
    print("   '-------'")

def print_classic_guitar():
    print_head()
    print_neck()
    print_body()

def print_retro_guitar():
    print_retro_head()
    print_neck()
    print_body()
    
def print_long_guitar():
    print_head()
    print_neck()
    print_neck()
    print_body()

def main():
    print_classic_guitar() # print classic guitar
    print_retro_guitar() # print retro head guitar
    print_long_guitar() # print long neck guitar

main()
  