import os
import sys
from pdf2image import convert_from_path, pdfinfo_from_path

def limpar_terminal():
    ''' Limpa o terminal para uma melhor experiência de usuário '''
    os.system('cls' if os.name == 'nt' else 'clear')

def listar_pdfs():
    ''' Retorna uma lista de todos os arquivos .pdf no diretório atual.'''
    arquivos = os.listdir('.')
    pdfs = [arq for arq in arquivos if arq.lower().endswith('.pdf')]
    return pdfs

def obter_caminho_poppler():
    ''' Verifica se o poppler está como .py ou como .exe '''
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como .exe, pega o caminho da pasta temporária
        return os.path.join(sys._MEIPASS, 'poppler')
    else:
        # Se estiver rodando como .py, usa a Variável de Ambiente
        return None
    
def main():
    while True:
        limpar_terminal()
        print("=== 📄 PDF to Image Converter ===")
        print("\n=== by Guilherme Rodrigues Viaro ===")
        
        # 1. Encontrar PDFs no diretório
        pdfs = listar_pdfs()
        
        if not pdfs:
            print("\nNenhum arquivo PDF encontrado nesta pasta.")
            print("\nColoque arquivos .pdf na mesma pasta e tente novamente.")
            break

        print("\nPDFs encontrados no diretório atual:\n")
        for i, pdf in enumerate(pdfs, 1):
            print(f"[{i}] {pdf}")
            
        print(f"[0] Sair do programa")

        # 2. Selecionar o PDF
        try:
            escolha_pdf = int(input("\nInforme o número do PDF desejado: "))
            if escolha_pdf == 0:
                print("\nEncerrando o programa...\n")
                break

            if escolha_pdf < 1 or escolha_pdf > len(pdfs):
                print("Opção inválida.")
                input("Pressione Enter para tentar novamente...")
                continue

        except ValueError:
            print("Por favor, digite um número válido.")
            input("Pressione Enter para tentar novamente...")
            continue

        arquivo_selecionado = pdfs[escolha_pdf - 1]
        
        # Obter o número total de páginas
        try:
            info = pdfinfo_from_path(arquivo_selecionado)
            total_paginas = info["Pages"]

        except Exception as e:
            print(f"Erro ao ler o PDF. Detalhes: {e}")
            break

        print(f"\nO arquivo '{arquivo_selecionado}' possui {total_paginas} página(s).")
        
        # 3. Selecionar Intervalo
        print("\nIncluir:")
        print("\n[1] Todas as páginas")
        print("[2] Informar intervalo")
        
        try:
            escolha_intervalo = int(input("\nOpção: "))
            if escolha_intervalo not in [1, 2]:
                raise ValueError
            
        except ValueError:
            print("\nOpção inválida. Voltando ao menu inicial...")
            input("\nPressione Enter para continuar...")
            continue

        pagina_inicial = 1
        pagina_final = total_paginas

        if escolha_intervalo == 2:
            try:
                pagina_inicial = int(input(f"\nPágina inicial (1 a {total_paginas}): "))
                pagina_final = int(input(f"Página final ({pagina_inicial} a {total_paginas}): "))
                
                # Validação lógica do intervalo
                if pagina_inicial < 1 or pagina_final > total_paginas or pagina_inicial > pagina_final:
                    print("\nIntervalo inválido. Verifique os números e tente novamente.\n")
                    input("\nPressione Enter para voltar ao menu...")
                    continue

            except ValueError:
                print("\nEntrada inválida. Você deve digitar números.")
                input("\nPressione Enter para voltar ao menu...")
                continue

        # 4. Preparar pasta de saída e Converter
        nome_base = os.path.splitext(arquivo_selecionado)[0]
        pasta_saida = f"images_{nome_base}"
        
        # Cria a pasta se não existir
        os.makedirs(pasta_saida, exist_ok=True)
        caminho_absoluto = os.path.abspath(pasta_saida)

        print(f"\nConvertendo páginas {pagina_inicial} até {pagina_final} de '{arquivo_selecionado}'...")
        print("\nIsso pode levar alguns segundos dependendo do tamanho do PDF.\n")

        try:
            # O parâmetro first_page e last_page otimiza o uso de memória
            imagens = convert_from_path(
                arquivo_selecionado, 
                dpi=300, 
                first_page=pagina_inicial, 
                last_page=pagina_final,
                poppler_path=obter_caminho_poppler()
            )
            
            # Salvar as imagens
            numero_pagina_atual = pagina_inicial
            for imagem in imagens:
                nome_imagem = f"page_{numero_pagina_atual}.jpg"
                caminho_imagem = os.path.join(pasta_saida, nome_imagem)
                imagem.save(caminho_imagem, 'JPEG')
                print(f"Salvo: {nome_imagem}")
                numero_pagina_atual += 1
                
            print(f"\nSucesso! As imagens foram salvas em:")
            print(f"{caminho_absoluto}")
            
        except Exception as e:
            print(f"\nOcorreu um erro durante a conversão: {e}")

        # 5. Loop final
        continuar = input("\nDeseja converter outro arquivo? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nEncerrando o programa!\n")
            break

if __name__ == "__main__":
    main()