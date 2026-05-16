import os
import subprocess


def converter_odt_para_pdf(
        caminho_odt,
        pasta_saida=None,
        novo_nome=None
):
    if not os.path.exists(caminho_odt):
        raise FileNotFoundError(
            f"Arquivo não encontrado, digite: '.odt' no final: {caminho_odt}"
        )

    if pasta_saida is None:
        pasta_saida = os.path.dirname(
            os.path.abspath(caminho_odt)
        )

    os.makedirs(
        pasta_saida,
        exist_ok=True
    )

    try:
        comando = [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            caminho_odt,
            "--outdir",
            pasta_saida
        ]

        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True
        )

        if resultado.returncode != 0:
            raise Exception(
                resultado.stderr
            )

        nome_original = (
            os.path.splitext(
                os.path.basename(
                    caminho_odt
                )
            )[0]
        )

        nome_pdf = (
            f"{nome_original}.pdf"
        )

        caminho_pdf = os.path.join(
            pasta_saida,
            nome_pdf
        )

        if not os.path.exists(
                caminho_pdf
        ):
            raise Exception(
                "PDF não foi gerado."
            )

        if novo_nome:
            novo_caminho = os.path.join(
                pasta_saida,
                f"{novo_nome}.pdf"
            )

            os.rename(
                caminho_pdf,
                novo_caminho
            )

            caminho_pdf = novo_caminho

        print(
            f"PDF criado: "
            f"{caminho_pdf}"
        )

        return caminho_pdf

    except Exception as erro:
        print(
            f"Erro ao converter: "
            f"{erro}"
        )
        return None


arquivo_odt = input(
    "Digite o nome do arquivo .odt: "
)

resposta = input(
    "Deseja alterar o nome do PDF? "
    "(s/n): "
).strip().lower()

novo_nome = None

if resposta == "s":
    novo_nome = input(
        "Digite o novo nome "
        "do PDF: "
    ).strip()

pdf_gerado = (
    converter_odt_para_pdf(
        arquivo_odt,
        novo_nome=novo_nome
    )
)

if pdf_gerado:
    print(
        "Conversão finalizada "
        "com sucesso!"
    )