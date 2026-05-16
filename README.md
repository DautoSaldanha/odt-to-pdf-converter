# Conversor de ODT para PDF

Python automation tool that converts ODT documents into PDF files quickly and efficiently using LibreOffice.

## Funcionalidades

- Conversão de arquivos `.odt` para `.pdf`
- Utiliza LibreOffice em modo headless
- Geração automática do PDF na mesma pasta do arquivo original
- Suporte para pasta de saída personalizada
- Tratamento de erros

## Tecnologias

- Python 3
- LibreOffice

## Requisitos

Certifique-se de ter o LibreOffice instalado.

### Ubuntu / Linux

```bash
sudo apt update
sudo apt install libreoffice
```

### Windows

Baixe e instale o LibreOffice:

https://www.libreoffice.org/download/download-libreoffice/

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Conversor_de_ODT_para_PDF.git
```

Entre na pasta do projeto:

```bash
cd Conversor_de_ODT_para_PDF
```

## Como usar

Edite o nome do arquivo no código:

```python
arquivo_odt = "documento.odt"
```

Execute o script:

```bash
python main.py
```

O arquivo PDF será gerado automaticamente na mesma pasta do `.odt`.

## Exemplo

Entrada:

```text
curriculo.odt
```

Saída:

```text
curriculo.pdf
```

## Estrutura do Projeto

```text
📦 Conversor_de_ODT_para_PDF
 ┣ 📜 main.py
 ┣ 📜 README.md
 ┗ 📜 LICENSE
```