import pandas as pd

def _load_dataframe(caminho_polo):
    try:
        df = pd.read_csv(caminho_polo)
        print("Sucesso: DataFrame carregado com êxito!")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_polo}' não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def popular_dicts_a_partir_de_df(df):
    if df is None or df.empty:
        print("Aviso: DataFrame vazio ou inválido. Não foi possível popular os dicionários.")
        return {}, {}

    map_nome_codigo = dict(zip(df['nome_fantasia'], df['codigo']))
    map_nome_link = dict(zip(df['nome_fantasia'], df['link_landing_page']))

    if not map_nome_codigo or not map_nome_link:
        print("Aviso: Os dicionários podem estar vazios ou incompletos após o preenchimento (verifique as colunas).")
    else:
        print("Sucesso: Dicionários populados com êxito!")

    return map_nome_codigo, map_nome_link

def carrega_e_popula_polos(caminho_polo):
    df = _load_dataframe(caminho_polo)
    if df is None:
        return None, None

    map_nome_codigo, map_nome_link = popular_dicts_a_partir_de_df(df)
    return map_nome_codigo, map_nome_link


if __name__ == "__main__":
    caminho_polo = "assets/link_landing_polo.csv"
    map_nome_codigo, map_nome_link = carrega_e_popula_polos(caminho_polo)

    if map_nome_codigo is not None and map_nome_link is not None:
        print("\n--- Conteúdo carregado e populado diretamente (amostra) ---")
        print("map_nome_codigo:", list(map_nome_codigo.items())[:2], "...")
        print("map_nome_link:", list(map_nome_link.items())[:2], "...")
    else:
        print("\nNão foi possível carregar os dados para teste direto.")