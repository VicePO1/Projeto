import tkinter as tk
from tkinter import messagebox
import requests
import sys
import random
import html.parser as html
from random import randint

nt=[]

url="https://opentdb.com/api.php?amount=50&category=9&difficulty=medium&type=multiple"
api=requests.get(url)
info= api.json()

class AppUI():
    n_de_questoes=0
    dinheiro=0
    respostas_corretas=0
    respostas_corretas_seguidas=0
    nome="test"
    numbersR=random.sample(range(1, 50), 12)
    number=0
    order=0

    
    def __init__(self,root):
        self.root = root
        self.root.title("Quem quer ser Milíonario")
        self.root.geometry("500x600")
        self.root.resizable(height=False,width=False)
        self.root.config(background="beige")

        self.Label=tk.Label(font=("Arial","18"),text="Bem-vindo ao 'Show Me The Money - O Quiz'",background="beige",wraplength=300)
        self.Label.place(x=30,y=30)

        self.Button1=tk.Button(text="Começar",width=25,height=5,command=self.criar_questão,wraplength=80,background="light grey")
        self.Button1.place(x=30,y=200)

        self.Button2=tk.Button(text="Historico",width=25,height=5,command=self.historico_ver,wraplength=80,background="light grey")
        self.Button2.place(x=270,y=200)

        self.Button3=tk.Button(text="Limpar Histórico",width=25,height=5,command=self.limpar_historico,wraplength=80,background="light grey")
        self.Button3.place(x=30,y=350)

        self.Button4=tk.Button(text="Fechar\n(eu não quero ser um milionário)",width=25,height=5,command=self.fechar,wraplength=80,background="light grey")
        self.Button4.place(x=270,y=350)

        self.label2=tk.Label(text="",font=("Arial",15),background="beige")
        self.label2.place(y=470,x=10)

        self.label3=tk.Label(text="",font=("Arial",15),background="beige")
        self.label3.place(y=470,x=330)

        self.entry=tk.Entry(root,width=50)

        self.Button5=tk.Button(width=25,height=5,command=self.registar,text="Confirmar")

        self.Button6=tk.Button(text="Fechar",width=25,height=5,command=self.fechar)
        

    def fechar(self):
        sys.exit()
    
            
    def criar_questão(self):
        if self.n_de_questoes==12:
            self.endquiz()
        
        else:
            self.label3.config(text=f"Dinheiro:\n{self.dinheiro} ")
            self.label2.config(text=f"Respostas corretas:\n{self.respostas_corretas} ")
        
            n=self.numbersR[self.order]
            self.order=self.order+1
            self.titulo_coded=info["results"][n]["question"]
            self.titulo=f"{self.n_de_questoes+1}. {html.unescape(self.titulo_coded)}"
            self.Label.config(text=self.titulo)

            rc=html.unescape(info["results"][n]["correct_answer"])
            ri=html.unescape(info["results"][n]["incorrect_answers"])

            qc=randint(1,4)
            match qc:
                case 1:
                    self.Button1.config(text=rc,command=self.Corr_A)
                    self.Button2.config(text=html.unescape(ri[0]),command=self.Wro_A)
                    self.Button3.config(text=html.unescape(ri[1]),command=self.Wro_A)
                    self.Button4.config(text=html.unescape(ri[2]),command=self.Wro_A)
                case 2:
                    self.Button1.config(text=html.unescape(ri[0]),command=self.Wro_A)
                    self.Button2.config(text=rc,command=self.Corr_A)
                    self.Button3.config(text=html.unescape(ri[1]),command=self.Wro_A)
                    self.Button4.config(text=html.unescape(ri[2]),command=self.Wro_A)
                case 3:
                    self.Button1.config(text=html.unescape(ri[0]),command=self.Wro_A)
                    self.Button2.config(text=html.unescape(ri[1]),command=self.Wro_A)
                    self.Button3.config(text=rc,command=self.Corr_A)
                    self.Button4.config(text=html.unescape(ri[2]),command=self.Wro_A)
                case 4:
                    self.Button1.config(text=html.unescape(ri[0]),command=self.Wro_A)
                    self.Button2.config(text=html.unescape(ri[1]),command=self.Wro_A)
                    self.Button3.config(text=html.unescape(ri[2]),command=self.Wro_A)
                    self.Button4.config(text=rc,command=self.Corr_A)

    def Corr_A(self):
        self.Button1.config(background="green")
        self.Button2.config(background="green")
        self.Button3.config(background="green")
        self.Button4.config(background="green")
        
        self.n_de_questoes=self.n_de_questoes+1
        self.respostas_corretas=self.respostas_corretas+1
        self.respostas_corretas_seguidas=self.respostas_corretas_seguidas+1
        self.dinheiro=self.dinheiro+(100*self.respostas_corretas_seguidas)
        messagebox.showinfo("A resposta está...",f"Correta! +{100*self.respostas_corretas_seguidas}")

        self.Button1.config(background="light grey")
        self.Button2.config(background="light grey")
        self.Button3.config(background="light grey")
        self.Button4.config(background="light grey")
        
        self.criar_questão()
        

    def Wro_A(self):
        self.Button1.config(background="red")
        self.Button2.config(background="red")
        self.Button3.config(background="red")
        self.Button4.config(background="red")
        
        messagebox.showerror("A resposta está...",f"Errada!")
        self.n_de_questoes=self.n_de_questoes+1
        self.respostas_corretas_seguidas=0
        
        self.Button1.config(background="light grey")
        self.Button2.config(background="light grey")
        self.Button3.config(background="light grey")
        self.Button4.config(background="light grey")
        
        self.criar_questão()

    def endquiz(self):
        self.Button1.place_forget()
        self.Button2.place_forget()
        self.Button3.place_forget()
        self.Button4.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()

        self.entry.place(x=30,y=200)
        self.Button5.place(x=30,y=275)
        self.Label.config(text=f"Fim do Quiz. Conseguiste {self.dinheiro} euros. Escreve o teu nome.")
    
    def registar(self):
        self.nome=self.entry.get()

        with open("historico_quiz.txt","a") as file:
            file.write(f"{self.nome} -- {self.dinheiro}\n")
        
        self.fechar()

    def historico_ver(self):
        with open("historico_quiz.txt","r")as fileH:
            self.historico=fileH.read()

        if self.historico=="":
            self.historico="Sem historico"
        
        self.Button1.place_forget()
        self.Button2.place_forget()
        self.Button3.place_forget()
        self.Button4.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()

        self.Label.config(text=self.historico)
        
        self.Button6.place(x=270,y=350)


    def limpar_historico(self):
        with open("historico_quiz.txt","w")as fileD:
            fileD.truncate()
        messagebox.showinfo("Quem quer ser milionário","O Historico está agora Limpo")

        
     
def main():
    root= tk.Tk()
    app = AppUI(root)
    root.mainloop()

if __name__ =="__main__":
    main()