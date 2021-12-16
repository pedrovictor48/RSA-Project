def toTable(texto: str) -> list:
    converter = lambda x: ord(x) - ord('a') + 2 if x != ' ' else 28
    vetor = list(map(converter, texto))
    return vetor

def toText(vetor: list) -> str:
    converter = lambda x: chr(x - 2 + ord('a')) if x != 28 else ' '
    s = ''.join(map(converter, vetor))
    return s

def printHead():
    print(
bcolors.WARNING + 
""" 
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \       \:::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    ___\:::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\____\  /\   \:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/::\   \:::\   \:::\____\/:::/  \:::\   \:::\____\ 
\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\::/    \:::\  /:::/    /
 \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \/____/ \:::\/:::/    / 
       |:::::::::/    /    \:::\   \:::\    \               \::::::/    /  
       |::|\::::/    /      \:::\   \:::\____\               \::::/    /   
       |::| \::/____/        \:::\  /:::/    /               /:::/    /    
       |::|  ~|               \:::\/:::/    /               /:::/    /     
       |::|   |                \::::::/    /               /:::/    /      
       \::|   |                 \::::/    /               /:::/    /       
        \:|   |                  \::/    /                \::/    /        
         \|___|                   \/____/                  \/____/         
"""
+ bcolors.ENDC
    )

    print(
        bcolors.HEADER + "Projeto de Criptografia RSA\n" + 
        bcolors.OKBLUE + "GRUPO:\n" + bcolors.ENDC +
        " * Daniel Sival\n * Eduardo Melo\n * Pedro Ferreira\n * Vinícius Teixeira\n" +
        bcolors.OKBLUE + "PROFESSOR:\n" + bcolors.ENDC +
        " * Bruno Almeida Pimentel\n"
    )

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
