
#!        MEHMET KAHYA
#!         24.04.2022
#!     DNA MATCH ALGORITHM

from re import A
import time
from colorama import Fore
match = {
  "a": "t",  #Adenin -> Timin
  "g": "c",  # Guanin -> Sitozin
}

firstDna = str(input("First DNA: ")).lower()
secondDna = str(input("Second DNA: ")).lower()

DNA1 = firstDna.split()
DNA2 = secondDna.split()

list_dna1 = DNA1
list_dna2 = DNA2

print(list_dna1)
print(list_dna2)

len1 = len(list_dna1)
len2 = len(list_dna2)

if len1 != len2:
    print(Fore.RED + "len isn't matched")
    exit()

else:
    pass

finalMatchDNA = []
x = 0
for x in range(len1):
    x++1

    print(Fore.BLUE + f"X Index Val: {x}" + Fore.WHITE)
    
    if list_dna1[x]=="a" and list_dna2[x]=="t":
        print(Fore.GREEN + f"Index:{x} Match!  A-T"+ Fore.WHITE)
        finalMatchDNA.append("A     T")

    if list_dna1[x]=="t" and list_dna2[x]=="a":
        print(Fore.GREEN + f"Index:{x} Match!  T-A"+ Fore.WHITE)
        finalMatchDNA.append("T     A")

    if list_dna1[x]=="g" and list_dna2[x]=="c":
        print(Fore.GREEN + f"Index:{x} Match!  G-C"+ Fore.WHITE)
        finalMatchDNA.append("G     C")

    if list_dna1[x]=="c" and list_dna2[x]=="g":
        print(Fore.GREEN + f"Index:{x} Match!  C-G"+ Fore.WHITE)
        finalMatchDNA.append("C     G")

    time.sleep(1)
    print("\n")


print(Fore.GREEN + "FINAL DNA SEQUENCING" + Fore.WHITE)

a = 0
for a in range(len1):
    print(f"""
    | {finalMatchDNA[a]} |  
""")