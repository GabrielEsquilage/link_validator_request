from data_loader import carrega_e_popula_polos
from link_validator import validar_links

def main():
    caminho_polo = "assets/link_landing_polo.csv"

    print("Iniciando a aplicação...")

    map_nome_codigo, map_nome_link = carrega_e_popula_polos(caminho_polo)

    if map_nome_link is not None and map_nome_codigo is not None:
        print("\nImportação e preenchimento de dicionários concluídos com sucesso!")
        
        link_status = validar_links(map_nome_link)

        print("\n--- Relatório Final de Validação de Links ---")
        if link_status:
            for nome, status in link_status.items():
                print(f"  {nome}: {status}")
        else:
            print("Nenhum link para validar ou ocorreu um erro durante a validação.")
    else:
        print("\nFalha na importação de dados. A validação de links não será executada.")
    
    print("\nAplicação finalizada.")

if __name__ == "__main__":
    main()