from PIL import Image
import hashlib
import os
import time

def gerar_chave(imagem):
    """
    Gera uma chave a partir de uma imagem usando SHA-256.
    """
    hash_imagem = hashlib.sha256(imagem.tobytes()).digest()
    return list(hash_imagem)

def encriptar_imagem(texto, imagem_chave_path, imagem_saida_path=None):
    """
    Encripta um texto em uma imagem usando uma imagem chave.

    Args:
        texto (str): Texto a ser encriptado.
        imagem_chave_path (str): Caminho para a imagem chave.
        imagem_saida_path (str, optional): Caminho para salvar a imagem encriptada. Se não fornecido, será usado um caminho padrão.

    Returns:
        str: Mensagem indicando sucesso ou falha na encriptação.
    """
    try:
        # Definir diretório padrão para imagens criptografadas
        pasta_criptografadas = os.path.join(os.getcwd(), "imagens_criptografadas")
        os.makedirs(pasta_criptografadas, exist_ok=True)

        # Se nenhum caminho for fornecido, criar um caminho padrão
        if not imagem_saida_path:
            nome_arquivo = f"encrypted_{int(time.time())}.png"
            imagem_saida_path = os.path.join(pasta_criptografadas, nome_arquivo)

        imagem_chave = Image.open(imagem_chave_path).convert("RGB")
        largura, altura = imagem_chave.size
        total_pixels = largura * altura

        if len(texto) > total_pixels:
            return "Erro: o texto é muito grande para ser inserido nesta imagem."

        chave = gerar_chave(imagem_chave)
        dados_texto = texto.encode('utf-8')
        tamanho = len(dados_texto)

        dados = tamanho.to_bytes(4, 'big') + dados_texto

        dados_encriptados = bytes([b ^ chave[i % len(chave)] for i, b in enumerate(dados)])

        imagem_saida = Image.new("RGB", (largura, altura))
        pixels_saida = imagem_saida.load()

        index = 0
        for y in range(altura):
            for x in range(largura):
                if index < len(dados_encriptados):
                    r = dados_encriptados[index]
                    index += 1
                else:
                    r = 0
                pixels_saida[x, y] = (r, 0, 0)

        imagem_saida.save(imagem_saida_path)
        return (
            "✅ Imagem encriptada com sucesso!\n\n"
            "🔒 Sua mensagem foi escondida de forma criptografada usando a imagem como chave.\n"
            "🛡️ Garantimos que ninguém poderá acessá-la sem a imagem original.\n"
            f"📁 Caminho salvo: {imagem_saida_path}"
        )
    except Exception as e:
        return f"❌ Erro ao encriptar imagem: {e}"

"""
name='Secure7Stego',
version='1.01',
author='Nelsomar Barros',
author_email='nelsom.one8@gmail.com',
changes='Versão 1.01: Adicionado caminho padrão para a pasta de saída das mensagens encriptadas e correções de bugs.
        Ajustes na função encriptar_imagem para evitar erros de ligação entre funções e na parte gráfica.'
"""

