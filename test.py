# Text attributes
ALL_OFF = '\033[0m'
BOLD = '\033[1m'
UNDERSCORE = '\033[4m'
BLINK = '\033[5m'
REVERSE = '\033[7m'
CONCEALED = '\033[7m'

# Foreground colors
FG_BLACK = '\033[30m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'
FG_YELLOW = '\033[33m'
FG_BLUE = '\033[34m'
FG_MAGENTA = '\033[35m'
FG_CYAN = '\033[36m'
FG_WHITE = '\033[37m'

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Example
print(BOLD + FG_RED + BG_WHITE + 'Hello World!' + ALL_OFF)
print(UNDERSCORE + FG_GREEN + 'Hello World!' + ALL_OFF)
print(BLINK + FG_YELLOW + 'Hello World!' + ALL_OFF)
print(REVERSE + FG_BLUE + 'Hello World!' + ALL_OFF)
print(CONCEALED + FG_MAGENTA + 'Hello World!' + ALL_OFF)
print(FG_CYAN + 'Hello World!' + ALL_OFF)
print(FG_WHITE + 'Hello World!' + ALL_OFF)
print(BG_BLACK + 'Hello World!' + ALL_OFF)
print(BG_RED + 'Hello World!' + ALL_OFF)
print(BG_GREEN + 'Hello World!' + ALL_OFF)
print(BG_YELLOW + 'Hello World!' + ALL_OFF)
print(BG_BLUE + 'Hello World!' + ALL_OFF)
print(BG_MAGENTA + 'Hello World!' + ALL_OFF)
print(BG_CYAN + 'Hello World!' + ALL_OFF)
print(BG_WHITE + 'Hello World!' + ALL_OFF)
