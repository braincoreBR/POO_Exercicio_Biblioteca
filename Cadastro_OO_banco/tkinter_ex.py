import tkinter as tk

janela = tk.Tk()
janela.title("Teste")
janela.geometry("330x350")

label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0,column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela , width =35)
entry_nome.grid(row=0,column=1, padx=10, pady=10)

janela.mainloop()