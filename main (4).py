from tkinter import *


master = Tk()
master.title("Ursos 100 curso")
img_Fundo = PhotoImage(file="Imagens//fundo.png")
fundo = Label(master, image=img_Fundo)
fundo.place(x=0, y=0)
master.tk.call('wm', 'iconphoto', master._w, PhotoImage(file='Imagens//icone.png'))
master.geometry("700x400")
master.minsize(700, 400) 
master.maxsize(700, 400)
 
#carregar imagens 
img_lindinha = PhotoImage(file="Imagens//lindinha.png")
img_florzinha = PhotoImage(file="Imagens//florzinha.png")
img_docinho = PhotoImage(file="Imagens//docinho.png")
img_nulo = PhotoImage(file="Imagens//nulo.png")
img_vencedor = PhotoImage(file="Imagens//vencedor.png")
img_resultado = PhotoImage(file="Imagens//resultado.png")

#variaveis globais
florzinha = 0
lindinha = 0
docinho = 0
nulo = 0

#contagem de pontos
def florz():
    global florzinha
    florzinha = florzinha + 1

def lind():
    global lindinha
    lindinha = lindinha + 1


def docin():
    global docinho
    docinho = docinho + 1

def nulos():
    global nulo
    nulo = nulo + 1


#cslculando o vencedor
def venc():
    
    if lindinha > florzinha and lindinha> docinho and lindinha > nulo:
        resultado = Label(master, text="A vencedora foi a Lindinha!", background='White', foreground='Black')
        resultado.place(width=229, height=13, x=237, y=48)
        resultado.configure(font=("Courier", 10, "italic"))
    
    elif florzinha > lindinha and florzinha > docinho and florzinha > nulo:
        resultado = Label(master, text="A vencedora foi a Florzinha!", background='White', foreground='Black')
        resultado.place(width=229, height=13, x=237, y=48)
        resultado.configure(font=("Courier", 10, "italic"))
    
    elif docinho > lindinha and docinho > florzinha and docinho > nulo:
        resultado = Label(master, text="A vencedora foi a Docinho!", background='White', foreground='Black')
        resultado.place(width=229, height=13, x=237, y=48)
        resultado.configure(font=("Courier", 10, "italic"))
    
    elif nulo > lindinha and nulo > florzinha and nulo > docinho:
        resultado = Label(master, text="Não foi possivel determinar!", background='White', foreground='Black')
        resultado.place(width=229, height=13, x=237, y=48)
        resultado.configure(font=("Courier", 10, "italic"))

def result():
    
    label2.configure(text=f'Lindinha recebeu {lindinha} votos')
    label1.configure(text=f'Florzinha recebeu {florzinha} votos')
    label3.configure(text=f'Docinho recebeu {docinho} votos')
    label4.configure(text=f'Nulo recebeu {nulo} votos')

#botoes
botao_1 = Button(master,  image=img_lindinha, command=lind)
botao_1.place(width=80, height=30, x=160, y=280)

botao_2 = Button(master, image=img_florzinha, command=florz)
botao_2.place(width=80, height=30, x=260, y=280)
  
botao_3 = Button(master, image=img_docinho, command=docin)
botao_3.place(width=80, height=30, x=360, y=280)

botao_4 = Button(master, image=img_nulo, command=nulos)
botao_4.place(width=80, height=30, x=460, y=280)

botao_5 = Button(master, image=img_vencedor, command=venc)
botao_5.place(width=100, height=30, x=200, y=335)

botao_5 = Button(master, image=img_resultado, command=result)
botao_5.place(width=100, height=30, x=400, y=335)

#labels
label1 = Label(master, background='White', foreground='Black')
label1.place(width=210, height=20, x=245, y=75)
label1.configure(font=("Courier", 10, "italic"))

label2 = Label(master, background='White', foreground='Black')
label2.place(width=210, height=20, x=245, y=90)
label2.configure(font=("Courier", 10, "italic"))

label3 = Label(master, background='White', foreground='Black')
label3.place(width=210, height=20, x=245, y=105)
label3.configure(font=("Courier", 10, "italic"))

label4 = Label(master, background='White', foreground='Black')
label4.place(width=210, height=20, x=245, y=120)
label4.configure(font=("Courier", 10, "italic"))

master.mainloop()