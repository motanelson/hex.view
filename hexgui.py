
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def load_file():
    """Carrega um arquivo binário e exibe o conteúdo formatado em hexadecimal na área de texto."""
    file_path = filedialog.askopenfilename(title="Selecione um arquivo")
    if not file_path:
        return

    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()
        
        hex_output = []
        for offset in range(0, len(binary_data), 16):
            line_data = binary_data[offset:offset + 16]
            hex_values = " ".join(f"{byte:02X}" for byte in line_data)
            ascii_values = "".join(chr(byte) if 32 <= byte <= 127 else "." for byte in line_data)
            hex_output.append(f"{hex_values:<48} ; {offset:08X} {ascii_values}")

        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "\n".join(hex_output))
        global current_file_content
        current_file_content = "\n".join(hex_output)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

def save_file():
    """Salva o conteúdo da área de texto em um arquivo com extensão .hex."""
    file_path = filedialog.asksaveasfilename(defaultextension=".hex", filetypes=[("Arquivos HEX", "*.hex")])
    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END).strip())
        messagebox.showinfo("Sucesso", f"Arquivo salvo como: {file_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Configuração da janela principal
root = tk.Tk()
root.title("Visualizador de Arquivo Binário")
root.geometry("800x600")

# Botões para carregar e salvar arquivos
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, padx=10, pady=5)

load_button = tk.Button(button_frame, text="Carregar Arquivo", command=load_file)
load_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Salvar como .hex", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)

# Área de texto para exibir e editar o conteúdo
text_area = tk.Text(root, wrap=tk.NONE, font=("Courier", 10), bg="black", fg="white", insertbackground="white")
text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Barra de rolagem para a área de texto
scrollbar = tk.Scrollbar(text_area, command=text_area.yview)
text_area.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Variável global para armazenar o conteúdo atual
current_file_content = ""

# Inicia a aplicação
root.mainloop()
