import requests
import time
from data_loader import carrega_e_popula_polos

def validar_links(map_nome_link):
    if not map_nome_link:
        print("Aviso: O dicionário de links está vazio. Nenhuma validação será feita.")
        return {}

    link_status = {}
    print("\nIniciando Validação")
    for nome_fantasia, link in map_nome_link.items():
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
            response = requests.get(link, timeout=10, headers=headers)

            if response.status_code == 200:
                link_status[nome_fantasia] = "OK (200)"
                print(f"  Link {nome_fantasia}: OK (200)")
            else:
                link_status[nome_fantasia] = f"Erro ({response.status_code})"
                print(f"  Link {nome_fantasia}: Erro ({response.status_code})")
        except requests.exceptions.MissingSchema:
            link_status[nome_fantasia] = f"Erro: URL inválida (falta esquema como 'http://' ou 'https://'). Link: {link}"
            print(f"  Link {nome_fantasia}: Erro - URL inválida")
        except requests.exceptions.ConnectionError:
            link_status[nome_fantasia] = f"Erro de conexão: Não foi possível conectar ao servidor. Link: {link}"
            print(f"  Link {nome_fantasia}: Erro - Problema de conexão")
        except requests.exceptions.Timeout:
            link_status[nome_fantasia] = f"Erro de timeout: O servidor não respondeu a tempo. Link: {link}"
            print(f"  Link {nome_fantasia}: Erro - Timeout")
        except requests.exceptions.RequestException as e:
            link_status[nome_fantasia] = f"Erro geral na requisição: {e}. Link: {link}"
            print(f"  Link {nome_fantasia}: Erro geral - {e}")
        time.sleep(0.1)

    print("\nValidação de Links concluida")
    return link_status

if __name__ == "__main__":
    caminho_polo = "assets/link_landing_polo.csv"

    map_nome_codigo, map_nome_link = carrega_e_popula_polos(caminho_polo)


    if map_nome_link is not None:
        links_status = validar_linkls(map_nome_link)

        print("\n-- Validação de links --")
        if links_status:
            for nome, status in links_status.items():
                print(f" {nome}: {status}")
            
            else:
                print("Erro bna validação")

        else:
            print("\nNão fopi possivel encontrar os links para validação, Verifique o arquivo csv")
