# tolors
A minimal library adding colors to terminal apps written in python

# NOTE(31.12.22):-

`tolors` will no longer be supported by me anymore...

# Things to add:-

- Add bright colors

# Usage

```python
from tolors import *
tolorful_print(text="A" , bg=BLACKB , fg=REDF)
tolorful_print(text="B" , bg=BLACKB , fg=BLUEF)
tolorful_print(text="C" , bg=BLACKB , fg=GREENF)
tolorful_print(text='D' , bg=BLACKB , fg=YELLOWF)
tolorful_print(text="E" , bg=BLACKB , fg=CYANF)
tolorful_print(text='F' , bg=BLACKB , fg=MAGENTAF)
tolorful_print(text="G" , bg=REDB , fg=BLACKF)
tolorful_print(text="H" , bg=BLUEB , fg=BLACKF)
tolorful_print(text="I" , bg=GREENB , fg=BLACKF)
tolorful_print(text='J' , bg=YELLOWB , fg=BLACKF)
tolorful_print(text="K" , bg=CYANB , fg=BLACKF)
tolorful_print(text='L' , bg=MAGENTAB , fg=BLACKF)
tolorful_print(text='' , bg=RESET , fg=RESET)
```

![master](src/test.png)

# Colors

| Variable Name    | Color Name |
| ----------- | ----------- |
| BLACKF    | Black(Foreground) 
| REDF   | Red(Foregroud)  |
| BLUEF   | Blue(Foreground)       |
| GREENF   | Green(Foreground)   |
| YELLOWF   | Yellow(Foreground)       |
| MAGENTAF   | Magenta(Foreground        |
| CYANF   | Cyan(Foreground)       |
| WHITEF   | White(Foreground)        |
| BLACKFB    | Black Bright(Foreground) 
| REDFB   | Red Bright(Foregroud)  |
| BLUEFB   | Blue Bright(Foreground)       |
| GREENFB   | Green Bright(Foreground)   |
| YELLOWFB   | Yellow Bright(Foreground)       |
| MAGENTAFB   | Magenta Bright(Foreground        |
| CYANFB   | Cyan Bright(Foreground)       |
| WHITEFB   | White Bright(Foreground)        |
| BLACKB  | Black(Background)       |
| REDB   | Red(Background)        |
| GREENB   | Green(Background)        |
| BLUEB  | Blue(Background)     |
| YELLOWB   | Yellow(Background)        |
| CYANB   | Cyan(Background)        |
| MAGENTAB  | Magenta(Background)        |
| WHITEB  | White(Background)        |
| BLACKBB  | Black Bright(Background)       |
| REDBB   | Red Bright(Background)        |
| GREENBB   | Green Bright(Background)        |
| BLUEBB  | Blue Bright(Background)     |
| YELLOWBB   | Yellow Bright(Background)        |
| CYANBB   | Cyan Bright(Background)        |
| MAGENTABB  | Magenta Bright(Background)        |
| WHITEBB  | White Bright(Background)        |

# NOTE

Tolors uses ANSI color codes so that is why the table is there:-
