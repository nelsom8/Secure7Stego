# 🔐 Secure7Stego - Encriptador de Texto em Imagens com Interface Gráfica

Este projeto permite criptografar e descriptografar mensagens de texto ocultas em imagens utilizando uma interface gráfica feita com `ttkbootstrap` (Tkinter) e algoritmos simples de esteganografia + criptografia XOR baseada em imagem como chave.

  name='Secure7Stego',
    version='0.1',
    author='Nelsomar Barros',
    author_email='nelsom.one8@gmail.com',
    description=' Este projeto permite criptografar e descriptografar mensagens de texto ocultas em imagens utilizando uma interface gráfica feita com `ttkbootstrap` (Tkinter) e algoritmos simples de esteganografia + criptografia XOR baseada em imagem como chave ',
    
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
cd dist/
ls
python3 Secure7Stego.py

🧪 Como Funciona

    A imagem usada como chave é transformada em uma hash que serve como base para criptografar os bytes da mensagem.

    O texto é armazenado no canal vermelho (R) da imagem de saída.

    A mesma imagem-chave é necessária para recuperar a mensagem.
    
Parcerias e Atualizações

Fique à vontade para contribuir e se comunicar. 
Este é um projeto incial de estudos de uma carreira de CyberSecurity 
