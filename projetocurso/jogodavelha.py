
# importando a biblioteca
import tkinter

# criando a janela principal
janela = tkinter.Tk()

# alterando o título da janela
janela.title("Jogo da Velha")

# criando a interface gráfica
lb = tkinter.Label(janela, text="Jogo da Velha", font=("Arial", 20))
lb.grid(row=0, column=0, columnspan=3)

# criando os botões
bt1 = tkinter.Button(janela, width=10, height=5)
bt1.grid(row=1, column=0)

bt2 = tkinter.Button(janela, width=10, height=5)
bt2.grid(row=1, column=1)

bt3 = tkinter.Button(janela, width=10, height=5)
bt3.grid(row=1, column=2)

bt4 = tkinter.Button(janela, width=10, height=5)
bt4.grid(row=2, column=0)

bt5 = tkinter.Button(janela, width=10, height=5)
bt5.grid(row=2, column=1)

bt6 = tkinter.Button(janela, width=10, height=5)
bt6.grid(row=2, column=2)

bt7 = tkinter.Button(janela, width=10, height=5)
bt7.grid(row=3, column=0)

bt8 = tkinter.Button(janela, width=10, height=5)
bt8.grid(row=3, column=1)

bt9 = tkinter.Button(janela, width=10, height=5)
bt9.grid(row=3, column=2)

# executando o loop da janela
janela.mainloop()