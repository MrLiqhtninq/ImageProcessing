import os

from rich.console import Console
from rich.theme import Theme 
from rich.markdown import Markdown

from Week3.index import Week3
from Week4.index import Week4
from Week5.index import Week5
from Homework.index import Gama,LogTransformation,ImageToNegative,TextFixer,GrayScaleToBit,Filter,SaltAndPepper
#from Week6.week6 import homework6
#from Week7.index import homework7s
custom_theme= Theme({"success":"green","error":"bold red","none":"bold blue"})
console = Console(theme=custom_theme)
MARKDOWN = """
# 2022 Image Processing

3. Hafta Ödevleri İçin => 3
4. Hafta Ödevleri İçin => 4
5. Hafta Ödevleri İçin => 5
6. Homework İçin => 6

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

MARKDOWN3 = """
# HOMEWORK

1. [Gamma Dönüşümü [3.0,4.0,5.0] ] => 1
2. [Logaritmik Dönüşüm ] => 2
3. [Negatifini alma ] => 3
4. [Üzerinde metin olan resmin yazılarını netleştirme ] => 4
5. [Gri ölçekli resmi 8,16,24 bite çevir  ] => 5
6. [Sobel - Prewitt - Robert cross filtreleme  ] => 6
7. [Tuz biber görüntü oluştur ve histogram çıkarma.  ] => 7

*
"""
def main():
    md = Markdown(MARKDOWN)
    console.print(md)
    a = input()
    if a == "3":
        os.system('clear')
        md2 = Markdown(MARKDOWN2)
        console.print(md2)
        b = input()
        Week3(b)
    elif a == "4":
        os.system('clear')
        Week4()
    elif a == "5":
        os.system('clear')
        Week5()
    elif a == "6":
        os.system('clear')
        md2 = Markdown(MARKDOWN3)
        console.print(md2)
        b = input()
        if b == "1":
            Gama()
        elif b == "2":
            LogTransformation()
        elif b == "3":
            ImageToNegative()
        elif b == "4":
            TextFixer()
        elif b == "5":
            GrayScaleToBit()
        elif b == "6":
            Filter()
        elif b == "7":
            SaltAndPepper()
        else:
            os.system('clear')   
            console.print("Böyle bir ödev mevcut değil!",style="error")
            main()
    else:
        os.system('clear')   
        console.print("Diğer haftaların ödevleri mevcut değil!",style="error")
        main()

if __name__ == '__main__':
    main()