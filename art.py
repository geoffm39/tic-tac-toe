from util import clear_console

RED_TEXT = "\033[91m"
BLUE_TEXT = "\033[94m"
RESET = "\033[0m"


def logo():
    clear_console()
    print(f"""
{RED_TEXT} ______  ____    __ {RESET}      {BLUE_TEXT} ______   ____    __ {RESET}      {RED_TEXT} ______   ___     ___ {RESET}
{RED_TEXT}|      Tl    j  /  ]{RESET}      {BLUE_TEXT}|      T /    T  /  ]{RESET}      {RED_TEXT}|      T /   \   /  _]{RESET}
{RED_TEXT}|      | |  T  /  / {RESET}_____ {BLUE_TEXT}|      |Y  o  | /  / {RESET}_____ {RED_TEXT}|      |Y     Y /  [_ {RESET}
{RED_TEXT}l_j  l_j |  | /  / {RESET}|     |{BLUE_TEXT}l_j  l_j|     |/  / {RESET}|     |{RED_TEXT}l_j  l_j|  O  |Y    _]{RESET}
{RED_TEXT}  |  |   |  |/   \_{RESET}l_____j{BLUE_TEXT}  |  |  |  _  /   \_{RESET}l_____j{RED_TEXT}  |  |  |     ||   [_ {RESET}
{RED_TEXT}  |  |   j  l\     |{RESET}      {BLUE_TEXT}  |  |  |  |  \     |{RESET}      {RED_TEXT}  |  |  l     !|     T{RESET}
{RED_TEXT}  l__j  |____j\____j{RESET}      {BLUE_TEXT}  l__j  l__j__j\____j{RESET}      {RED_TEXT}  l__j   \___/ l_____j{RESET}                                                                    
""")
