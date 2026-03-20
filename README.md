# 📄 PDF to JPEG Converter (CLI)

Um conversor interativo CLI (Command Line Interface) que transforma arquivos PDF em JPEG de forma offline, prática, eficiente, organizada e com boa resolução. 

Desenvolvido em Python, foi idealizado por uma necessidade pessoal, permitindo, com maior facilidade, sem anúncios, sem extensões e sem internet, manipular imagens dos PDFs sem recorrer a prints de tela, que prejudicam muito a qualidade do arquivo. 

## ✨ Funcionalidades

- **Menu Interativo:** Interface limpa no terminal para seleção de arquivos.
- **Leitura Automática:** Identifica todos os arquivos `.pdf` no diretório atual.
- **Adaptabilidade:** Opção de converter o arquivo inteiro ou selecionar um intervalo específico de páginas.
- **Auto-Organização:** Cria automaticamente uma pasta dedicada para salvar as imagens, salvando-as de forma organizada e enumerada.

## 🚀 Como Usar

Para utilizar esta ferramenta, você precisará do executável e do motor de renderização de PDFs chamado **Poppler**. Siga o passo a passo abaixo:

### 1. Baixando os Arquivos
1. Vá até a aba **[Releases](https://github.com/guirv/PDF-to-JPEG-Converter-CLI/releases/latest)** deste repositório.
2. Baixe os dois arquivos disponíveis:
   - `pdf-to-image.exe` (O programa)
   - `poppler.zip` (O motor de renderização)

### 2. Configurando o Poppler (Apenas na primeira vez)
O Windows precisa saber onde o Poppler está para que a conversão funcione.

1. Extraia o arquivo `poppler.zip` em um local fixo no seu computador (Recomendação: `C:\poppler`).
2. Abra o menu Iniciar do Windows e digite **"Editar as variáveis de ambiente do sistema"** e aperte Enter.
3. Clique no botão **"Variáveis de Ambiente..."**.
4. Na lista inferior (**Variáveis do sistema**), procure a variável **`Path`**, selecione-a e clique em **Editar**.
5. Clique em **Novo** e cole o caminho completo da pasta `bin` que está dentro do Poppler extraído.
   - *Exemplo: `C:\poppler\Library\bin` (verifique onde a pasta bin está no seu arquivo extraído).*
6. Clique em **OK** em todas as janelas para salvar.

### 3. Usando o Conversor
1. Coloque o arquivo `pdf-to-image.exe` na **MESMA PASTA** onde estão os arquivos PDF que você deseja converter.
2. Dê um duplo clique no `.exe` e siga as instruções na tela do terminal!

### 💻 Exemplo Interface-Resultado

![Exemplo Interface-Resultado](assets/pdf-to-image-print.jpg)

## 🛠️ Tecnologias Utilizadas

- **Python 3**

- **pdf2image:** Wrapper para conversão dos PDFs.

- **Pillow (PIL):** Manipulação e salvamento dos arquivos de imagem.

- **Poppler:** Motor de renderização do PDFs.

- **PyInstaller:** Empacotamento do script e dependências em um executável autônomo.

## 👨‍💻 Autor

- Desenvolvido por **Guilherme Rodrigues Viaro.**
