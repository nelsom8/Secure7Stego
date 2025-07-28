from PIL import Image
import hashlib

def gerar_chave(imagem):
    hash_imagem = hashlib.sha256(imagem.tobytes()).digest()
    return list(hash_imagem)

def decriptar_imagem(imagem_saida_path, imagem_chave_path):
    try:
        imagem_saida = Image.open(imagem_saida_path).convert("RGB")
        imagem_chave = Image.open(imagem_chave_path).convert("RGB")

        largura, altura = imagem_saida.size
        pixels = imagem_saida.load()

        dados_encriptados = []
        for y in range(altura):
            for x in range(largura):
                r, g, b = pixels[x, y]
                dados_encriptados.append(r)

        chave = gerar_chave(imagem_chave)

        dados_decriptados = bytes([b ^ chave[i % len(chave)] for i, b in enumerate(dados_encriptados)])

        tamanho = int.from_bytes(dados_decriptados[:4], 'big')
        mensagem = dados_decriptados[4:4+tamanho].decode('utf-8')

        return (
            "✅ Mensagem decriptada com sucesso!\n\n"
            "📩 Conteúdo recuperado de forma segura e confidencial:\n\n" +
            mensagem
        )
    except Exception as e:
        return f"❌ Erro ao decriptar imagem: {e}"

"""
name='Secure7Stego',
    version='0.1',
    author='Nelsomar Barros',
    author_email='nelsom.one8@gmail.com',
"""