import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore, Style
from time import sleep


#Funcao filter
def filter_html(url, tag=None, attr=None):
    response = requests.get(url, headers={'User-Agent': 'html-digz'}, timeout=9, allow_redirects=True)
    soup = BeautifulSoup(response.text, "lxml")

    if tag:
        results = soup.find_all(tag)
    elif attr:
        results = soup.find_all(attrs={attr: True})
    else:
        return []
        
    return [result.get(attr) if attr else result for result in results]


#Parser
parser = argparse.ArgumentParser(description='Filtrar Tags e Atributos de Source-Code')
parser.add_argument('url', type=str, help='A URL a ser filtrada')
parser.add_argument('-tag', type=str, help='O nome da tag HTML a ser filtrada')
parser.add_argument('-attr', type=str, help='O nome do atributo HTML a ser filtrado')
parser.add_argument('-o', '--output', type=str, help='Nome do arquivo de saida')



args = parser.parse_args()

results_filtrados = filter_html(args.url, args.tag, args.attr)

print("""
███████████████▀██████████████████████████████████████████
█▄─▄▄▀█▄─▄█─▄▄▄▄█░▄▄░▄█▀▀▀▀▀██─▄─▄─█─▄▄─█─▄▄─█▄─▄███─▄▄▄▄█
██─██─██─██─██▄─██▀▄█▀██████████─███─██─█─██─██─██▀█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀ v2
""")
sleep(2)

#Fixed error: Repeat error mensages
founds = False
for result in results_filtrados:
    if result:
        print(f'{Fore.GREEN}Found:{Style.RESET_ALL} [{result}]')
        founds = True

if founds != True:
    print(f'{Fore.RED}Not found{Style.RESET_ALL}')


if args.output:
    sleep(2)
    print("\n Contruindo Arquivo de Saida")
    with open(args.output, 'w') as f:
        for result in results_filtrados:
            if result:
                f.write(f'{result}\n')
            else:
                f.write('Write File Fail\n')
    sleep(2)            
    print(f'{Fore.GREEN}Arquivo de Saida: Finished!{Style.RESET_ALL}')
