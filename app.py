import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from PIL import Image
import os

from cripto_utils import encriptar_imagem
from decripto_utils import decriptar_imagem

class Encriptador:
    def __init__(self):
        self.janela = tb.Window(themename="darkly")
        self.janela.title('Secure7Stego - Encriptador de Texto em Imagem')
        self.janela.geometry("600x700")
        self.janela.resizable(False, False)

        padding = 10

        self.texto_label = tb.Label(self.janela, text='Texto a ser criptografado:', font=("Arial", 14, "bold"))
        self.texto_label.pack(pady=(padding, 0), padx=padding, anchor="w")

        self.texto_entry = tb.Text(self.janela, height=10, width=60)
        self.texto_entry.pack(pady=(0, padding), padx=padding)

        self.carregar_imagem_chave_button = tb.Button(
            self.janela, text='Carregar Imagem como Chave',
            bootstyle=SUCCESS, command=self.carregar_imagem_chave
        )
        self.carregar_imagem_chave_button.pack(pady=padding, padx=padding, fill=X)

        self.chave_label = tb.Label(self.janela, text='Chave:', font=("Arial", 12))
        self.chave_label.pack(pady=(padding, 0), padx=padding, anchor="w")
        self.chave_entry = tb.Entry(self.janela, width=60)
        self.chave_entry.pack(pady=(0, padding), padx=padding)

        self.carregar_imagem_saida_button = tb.Button(
            self.janela, text='Carregar Imagem de Saída',
            bootstyle=SUCCESS, command=self.carregar_imagem_saida
        )
        self.carregar_imagem_saida_button.pack(pady=padding, padx=padding, fill=X)

        self.imagem_saida_label = tb.Label(self.janela, text='Imagem de Saída:', font=("Arial", 12))
        self.imagem_saida_label.pack(pady=(padding, 0), padx=padding, anchor="w")
        self.imagem_saida_entry = tb.Entry(self.janela, width=60)
        self.imagem_saida_entry.pack(pady=(0, padding), padx=padding)

        self.encriptar_button = tb.Button(self.janela, text='Encriptar', bootstyle=PRIMARY, command=self.encriptar)
        self.encriptar_button.pack(pady=(padding, 5), padx=padding, fill=X)

        self.decriptar_button = tb.Button(self.janela, text='Decriptar', bootstyle=INFO, command=self.decriptar)
        self.decriptar_button.pack(pady=(0, padding), padx=padding, fill=X)

        self.carregar_texto_button = tb.Button(self.janela, text='Carregar Texto', bootstyle=SECONDARY, command=self.carregar_texto)
        self.carregar_texto_button.pack(pady=(0, padding), padx=padding, fill=X)

        self.resultado_label = tb.Label(self.janela, text='Resultado:', font=("Arial", 12, "bold"))
        self.resultado_label.pack(pady=(padding, 0), padx=padding, anchor="w")

        self.resultado_texto = tb.Label(self.janela, text='', wraplength=560, font=("Arial", 11))
        self.resultado_texto.pack(pady=(0, padding), padx=padding, fill=X)

    def run(self):
        self.janela.mainloop()

    def carregar_texto(self):
        texto_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if texto_path:
            try:
                with open(texto_path, 'r', encoding='utf-8') as arquivo:
                    texto = arquivo.read()
                    self.texto_entry.delete("1.0", "end")
                    self.texto_entry.insert("1.0", texto)
                    self.resultado_texto.config(text=f"Texto carregado de: {texto_path}")
            except Exception as e:
                self.resultado_texto.config(text=f"Erro ao carregar texto: {e}")

    def carregar_imagem_chave(self):
        imagem_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg"), ("Todos os arquivos", "*.*")]
        )
        if imagem_path and os.path.isfile(imagem_path):
            try:
                self.imagem_chave = Image.open(imagem_path)
                self.resultado_texto.config(text="Imagem chave carregada com sucesso.")
            except Exception as e:
                self.resultado_texto.config(text=f"Erro ao carregar imagem chave: {e}")
        else:
            self.resultado_texto.config(text="Nenhuma imagem selecionada.")

    def carregar_imagem_saida(self):
        imagem_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg"), ("Todos os arquivos", "*.*")]
        )
        if imagem_path and os.path.isfile(imagem_path):
            try:
                self.imagem_saida = Image.open(imagem_path)
                self.imagem_saida_entry.delete(0, "end")
                self.imagem_saida_entry.insert(0, imagem_path)
                self.resultado_texto.config(text="Imagem de saída carregada com sucesso.")
            except Exception as e:
                self.resultado_texto.config(text=f"Erro ao carregar imagem de saída: {e}")
        else:
            self.resultado_texto.config(text="Nenhuma imagem selecionada.")

    def encriptar(self):
        texto = self.texto_entry.get("1.0", "end").strip()
        imagem_chave_path = filedialog.askopenfilename(title="Selecione a imagem chave")
        imagem_saida_path = self.imagem_saida_entry.get()

        if not imagem_chave_path or not imagem_saida_path:
            self.resultado_texto.config(text="Por favor, selecione a imagem chave e a imagem de saída.")
            return

        resultado = encriptar_imagem(texto, imagem_chave_path, imagem_saida_path)
        self.resultado_texto.config(text=resultado)

    def decriptar(self):
        imagem_saida_path = self.imagem_saida_entry.get()
        imagem_chave_path = filedialog.askopenfilename(title="Selecione a imagem chave")

        if not imagem_chave_path or not imagem_saida_path:
            self.resultado_texto.config(text="Por favor, selecione a imagem de saída e a imagem chave.")
            return

        resultado = decriptar_imagem(imagem_saida_path, imagem_chave_path)
        self.resultado_texto.config(text=resultado)


if __name__ == "__main__":
    app = Encriptador()
    app.run()

"""
name='Secure7Stego',
    version='0.1',
    author='Nelsomar Barros',
    author_email='nelsom.one8@gmail.com',
"""