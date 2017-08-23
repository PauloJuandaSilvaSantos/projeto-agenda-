import json


def main(args=[]):
     while True:
         try:
             f = open("meses.txt","r", encoding="utf8")
             linhas = f.readlines()

             for linhas in linhas:
                 print(linhas.strip())
             break
         except FileNotFoundError:
             print("arquivo não encontrado")


if __name__ == "__main__":
    main()
