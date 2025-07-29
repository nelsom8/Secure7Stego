# 🔐 Secure7Stego XOR - Encriptador de Texto em Imagens com Interface Gráfica

Este projeto permite criptografar e descriptografar mensagens de texto ocultas em imagens utilizando uma interface gráfica feita com `ttkbootstrap` (Tkinter) e algoritmos simples de esteganografia + criptografia XOR baseada em imagem como chave.

  name='Secure7Stego',
    version='0.1', 28JUL2025
    author='Nelsomar Barros',
    author_email='nelsom.one8@gmail.com',
    description=' Este projeto permite criptografar e descriptografar mensagens de texto ocultas em imagens utilizando uma interface gráfica feita com `ttkbootstrap` (Tkinter) e algoritmos simples de esteganografia + criptografia XOR baseada em imagem como chave ',
    name='Secure7Stego',
    version='1.01', 29JUL2025
    changes='Versão 1.01: Adicionado caminho padrão para a pasta de saída das mensagens encriptadas e correções de bugs.',

    
    ## Projeto Inicial com licença MIT
---

## 🖼️ Funcionalidades

- 🔏 **Criptografar** texto dentro de uma imagem utilizando outra imagem como chave.
- 🔓 **Descriptografar** o texto de uma imagem de saída utilizando a imagem-chave original.
- 📁 Interface gráfica simples e moderna com suporte a tema escuro.
- ✅ Compatível com Linux (Kali), Windows e macOS.
- 📦 Pode ser empacotado como um executável `.bin` ou `.exe` para distribuição.

---

## 📂 Estrutura do Projeto

meu_projeto_encriptador/
├── app.py # Interface gráfica
├── cripto_utils.py # Função de criptografia
├── decripto_utils.py # Função de descriptografia
├── requirements.txt # Dependências do projeto
├── README.md # Instruções e documentação


---

## 💻 Requisitos

- Python 3.7+
- Pip

### Instalar dependências:

```bash
pip install -r requirements.txt

### ▶️ Como Executar

cd dist
python3 Secure7Stego.py ## Escolha a versao na pasta dist

🧪 Como Funciona

    A imagem usada como chave é transformada em uma hash que serve como base para criptografar os bytes da mensagem.

    O texto é armazenado no canal vermelho (R) da imagem de saída.

    A mesma imagem-chave é necessária para recuperar a mensagem.
    
Parcerias e Atualizações

Fique à vontade para contribuir e se comunicar. 
Este é um projeto inicial de estudos de uma carreira de CyberSecurity 



# ---------------- ATENÇÃO ao NIVEL DE SEGURANÇA DO SECURE7STEGO XOR ---------------------------------------

A segurança da criptografia implementada no código fornecido depende de vários fatores, incluindo a robustez do algoritmo de hash utilizado e a maneira como os dados são encriptados. Vamos analisar os principais aspectos:
Nível de Segurança

    Algoritmo de Hash:
        O código utiliza SHA-256 para gerar uma chave a partir da imagem. SHA-256 é um algoritmo de hash seguro e amplamente utilizado, que produz um hash de 256 bits. É considerado seguro contra ataques de pré-imagem e colisão.

    Operação XOR:
        A operação XOR (ou exclusivo) é usada para encriptar os dados. XOR é uma operação bit a bit que é reversível se a chave for conhecida. A segurança do XOR depende inteiramente da chave utilizada. Se a chave for aleatória e mantida em segredo, o XOR pode ser seguro. No entanto, se a chave for previsível ou conhecida, a segurança é comprometida.

    Chave Baseada em Imagem:
        A chave é gerada a partir da imagem fornecida. Isso significa que a segurança da encriptação depende da complexidade e da aleatoriedade da imagem utilizada como chave. Imagens complexas e aleatórias fornecem chaves mais seguras.

Pontos de Vulnerabilidade

    Previsibilidade da Chave:
        Se a imagem utilizada como chave for simples ou previsível, a chave gerada também será previsível, o que pode facilitar a quebra da encriptação.

    Ataques de Força Bruta:
        Se um atacante tiver acesso a um grande número de imagens possíveis e souber o algoritmo utilizado, ele poderia tentar um ataque de força bruta para descobrir a chave correta. No entanto, isso é computacionalmente inviável para imagens complexas e grandes.

    Ataques de Canal Lateral:
        Ataques que exploram informações físicas ou de implementação, como tempo de execução, consumo de energia, ou emissões eletromagnéticas, podem ser utilizados para extrair informações sobre a chave.

Como Quebrar a Criptografia sem a Imagem Original

    Ataque de Força Bruta:
        Tentar todas as combinações possíveis de imagens como chaves. Isso é inviável na prática devido ao grande número de possibilidades, mas tecnicamente possível.

    Análise de Padrões:
        Se o atacante tiver acesso a várias imagens encriptadas com a mesma chave, ele poderia tentar analisar padrões para deduzir informações sobre a chave.

    Engenharia Reversa:
        Se o atacante tiver acesso ao código-fonte e souber o algoritmo utilizado, ele poderia tentar engenharia reversa para entender como a chave é gerada e tentar reproduzi-la.

 ------------------  TAMANHO DE TEXTO E IMAGENS ---------------------------

No código fornecido, o tamanho do texto aceito e o tamanho das imagens são determinados por algumas condições específicas. Vamos analisar cada um deles:
Tamanho do Texto Aceito

O tamanho do texto que pode ser encriptado é limitado pelo número de pixels da imagem chave. Cada caractere do texto é armazenado em um pixel da imagem. Portanto, o tamanho máximo do texto é igual ao número total de pixels da imagem chave.

Aqui está a parte relevante do código que determina o tamanho do texto:

largura, altura = imagem_chave.size
total_pixels = largura * altura

if len(texto) > total_pixels:
    return "Erro: o texto é muito grande para ser inserido nesta imagem."

Tamanho das Imagens

O código não impõe um limite específico para o tamanho das imagens, mas as imagens devem ser grandes o suficiente para conter o texto que se deseja encriptar. A imagem de saída terá o mesmo tamanho (em pixels) que a imagem chave.

Aqui está a parte relevante do código que lida com o tamanho das imagens:

imagem_chave = Image.open(imagem_chave_path).convert("RGB")
largura, altura = imagem_chave.size
total_pixels = largura * altura

imagem_saida = Image.new("RGB", (largura, altura))

Padrão das Imagens

O código utiliza imagens no formato RGB (Red, Green, Blue). A imagem chave e a imagem de saída são convertidas para o modo RGB para garantir que tenham três canais de cor (vermelho, verde e azul).

Aqui está a parte relevante do código que define o padrão das imagens:

imagem_chave = Image.open(imagem_chave_path).convert("RGB")
imagem_saida = Image.new("RGB", (largura, altura))

Resumo

    Tamanho do Texto: O tamanho máximo do texto é igual ao número total de pixels da imagem chave (largura × altura).
    Tamanho das Imagens: Não há um limite específico para o tamanho das imagens, mas a imagem de saída terá o mesmo tamanho que a imagem chave.
    Padrão das Imagens: As imagens são convertidas para o modo RGB, garantindo que tenham três canais de cor.

Exemplo

Se a imagem chave tiver uma resolução de 100x100 pixels, o tamanho máximo do texto que pode ser encriptado será de 10.000 caracteres (100 × 100). A imagem de saída também terá uma resolução de 100x100 pixels.

Essas condições garantem que o texto possa ser encriptado e decriptado corretamente usando as imagens fornecidas.


