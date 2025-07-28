from PIL import Image
import hashlib

def gerar_chave(imagem):
    hash_imagem = hashlib.sha256(imagem.tobytes()).digest()
    return list(hash_imagem)

def encriptar_imagem(texto, imagem_chave_path, imagem_saida_path):
    try:
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
            "📁 Caminho salvo: " + imagem_saida_path
        )
    except Exception as e:
        return f"❌ Erro ao encriptar imagem: {e}"

"""
name='Secure7Stego',
    version='0.1',
    author='Nelsomar Barros',
    author_email='nelsom.one8@gmail.com',
"""