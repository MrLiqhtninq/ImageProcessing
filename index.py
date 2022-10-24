import os
import sys

from rich.console import Console
from rich.theme import Theme 
from rich.markdown import Markdown

from Week3.index import Week3
from Week4.index import Week4
from Week5.index import Week5
#from Week6.week6 import homework6
#from Week7.index import homework7s
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)
MARKDOWN = """
# 2022 Image Processing

3. Hafta Ödevleri İçin => 3
4. Hafta Ödevleri İçin => 4
5. Hafta Ödevleri İçin => 5
6. Hafta Ödevleri İçin => 6

*
"""
MARKDOWN2 = """
# 3. HAFTA ÖDEVLERİ

[GrayScale] => 1
[Blur] => 2
[Canny] => 3
[EdgeDetection] => 4

*
"""
def clear():
    if sys.platform == 'win32':
        os.system('cls')  
    else:
        os.system('clear')
def main():
    md = Markdown(MARKDOWN)
    console.print(md)
    a = input()
    if a == "3":
        clear()
        md2 = Markdown(MARKDOWN2)
        console.print(md2)
        b = input()
        Week3(b)
    elif a == "4":
        clear()
        Week4()
    elif a == "5":
        clear()
        Week5()
    else:
        clear()   
        console.print("Diğer haftaların ödevleri mevcut değil!",style="error")
        main()

if __name__ == '__main__':
    main()