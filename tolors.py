from os import system

global BLACKF, BLUEF, REDF, GREENF, YELLOWF, CYANF, MAGENTAF, WHITEF , BLACKB , REDB
BLACKF = "\u001b[30m"
REDF = "\u001b[31m"
GREENF = "\u001b[32m"
YELLOWF = "\u001b[33m"
BLUEF = "\u001b[34m"
MAGENTAF = "\u001b[35m"
CYANF = "\u001b[36m"
WHITEF = "\u001b[37m"
BLACKB = "\u001b[40m"
REDB = "\u001b[41m"
GREENB = "\u001b[42m"
YELLOWB = "\u001b[43m"
BLUEB = "\u001b[44m"
MAGENTAB = "\u001b[45m"
CYANB = "\u001b[46m"
WHITEB = "\u001b[47m"
RESET = "\u001b[0m"

def tolorful_print(text , background=RESET, foreground=BLACKF):
    if not text==None:
        system("printf " + '"' + background +foreground+ text + "\n" + '"')
    else:
        exit(255)