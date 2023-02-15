from typing import Tuple
import sqlite3
import tkinter as tk
from datetime import date
from time import strftime
from tkinter import scrolledtext as tkst
import string
import random

from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

con = sqlite3.connect('banco_de_dados.db')
cursor = con.cursor()

co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

janela = Tk()
janela.title('Menu Login')
janela.geometry('310x350')
janela.configure(background=co1)
janela.resizable(width= TRUE, height= TRUE)

#JANELA LOGIN
frame_cima = Frame(janela, width= 310, height= 50, bg = co1, relief= 'flat')
frame_cima.grid(row = 0, column=0, pady = 1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width= 310, height= 250, bg = co1, relief= 'flat')
frame_baixo.grid(row = 1, column=0, pady = 1, padx=0, sticky=NSEW)

frame_baixo2= Frame(janela, width= 310, height= 450, bg = co1, relief= 'flat')
frame_baixo2.grid(row = 2, column=0, pady = 1, padx=0, sticky=NSEW)
 
l_nome = Label(frame_cima, text='LOGIN',anchor= NE, font='Ivy 25', bg = co1, fg= co4)
l_nome.place(x = 5, y=5)

l_linha = Label(frame_cima, text='',width=275, anchor= NW, font='Ivy 1', bg = co2, fg= co4)
l_linha.place(x = 10, y=45)


def buscar(userlogin, usersenha):
  userlogin = e_nome.get()
  usersenha = e_pass.get()
  logins_ = []
  try:
    with open("logins.txt", 'r+', encoding='Utf-8', newline='') as arquivo:
      for linha in arquivo:
    
        lista1 = linha.split()
        if len(lista1) != 0:
          logins_.append(lista1)
      for l in logins_:
          login = l[1]
          senha = l[3]
          if userlogin == login and usersenha == senha:
            return True
  except FileNotFoundError:
      return False

def fazerLogin():
    userlogin = e_nome.get()
    usersenha = e_pass.get()
    b = buscar(userlogin, usersenha)
    if (userlogin == "" or userlogin == " ") or (usersenha == "" or usersenha == " "):
                messagebox.showwarning("ERROR", "Por favor, preencha o espaço vazio.")
                return False
    if b == True:
        messagebox.showinfo('Login','Seja bem vindo(a) ' + str(userlogin))
        nova_janela()
    else:
        messagebox.showwarning('ERRO','Login ou senha incorretos!')
    return fazerLogin

global janela2

def indicate(lb,page):
    #hide_indicators()
    lb.config(bg='white')
    delete_pages()
    page()

def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()

# TELA CADASTRO DE PRODUTO
def cadastroProduto_pag():

    cadpro_frame = tk.Frame(main_frame, background= "white")
    lb = tk.Label(cadpro_frame, text='Cadastro de produto', font = ('Bold', 25), bg = "#3fb5a3")
    lb.pack(side= TOP, fill = tk.X)
    lb_resp = Label(cadpro_frame, font = ('Arial',12), text='',bg = 'white', fg= 'red')
    lb_resp.place(x=600, y=400)
    
    cadpro_frame.place(width = 1000, height =600 )

    def Nome():
        nome = e_nome.get()
    
        if (len(nome) == 0):
            lb_resp.configure(text='Campo nome vazio.')
            return True

        elif not len(nome)>= 2:
   
            lb_resp.configure(text='Digite um nome com \npelo menos 2 caracteres.')
            return True
        temp = ''.join(nome.split(' '))
        for i in temp:
            if not i.isalpha(): #verifica se tem número
                lb_resp.configure(text='Digite um nome válido.')
                return False
          
        else:
            lb_resp.configure(text='')
            return nome.strip(' ')

    def Cnpj():
            cnpj = e_cnpj.get()
            if (len(cnpj) == 0):
                lb_resp.configure(text='Campo CNPJ vazio.')
                return True
        
            elif not cnpj.isnumeric():
                lb_resp.configure(text='Insira apenas \nnúmeros no campo CNPJ.')
                return False
          
            if not(len(cnpj) == 14):
                lb_resp.configure(text='Insira um CNPJ \ncom 14 caracteres.')
                return False
         
            else:
                lb_resp.configure(text='')
                return cnpj.strip(' ')

    def Preco_custo():
            preco_custo = e_precoCusto.get()
            if (len(preco_custo) == 0):
                lb_resp.configure(text='Campo preço de custo vazio.')
                return True
         
            if not preco_custo.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo preço de custo.')
                return False
           
            else:
                lb_resp.configure(text='')
                return preco_custo.strip(' ')

    def Preco_v():
            preco_v = e_precoV.get()
            if (len(preco_v)== 0):
                lb_resp.configure(text='Campo preço de venda vazio.')
                return True
           
            elif not preco_v.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo preço de venda.')
                return False
          
            else:
                lb_resp.configure(text='')
                return preco_v.strip(' ')

    def Codigo_p():
            codigo_p = e_codigoP.get()
            if (len(codigo_p) == 0):
                lb_resp.configure(text='Campo código vazio.')
                return True
        
            elif not codigo_p.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo código.')
                return False
           
            else:
                lb_resp.configure(text='')
                return codigo_p.strip('')

    def Nome_f():
            nome_f = e_nomeF.get()
            if (len(nome_f) == 0):
                lb_resp.configure(text='Campo fornecedor vazio.')
                return True
            
            elif not len(nome_f)>= 2:
                lb_resp.configure(text='Insira um fornecedor com \npelo menos 2 caracteres.')
                return False
       
            temp = ''.join(nome_f.split(' '))
            for i in temp:
                if not i.isalnum():
                    lb_resp.configure(text='Insira apenas letras \ne números no campo fornecedor.')
                    return False
       
            else:
                lb_resp.configure(text='')
                return nome_f.strip(' ')

    def Fabricante():
            fabricante = e_fabricante.get()
            if (len(fabricante) == 0):
                lb_resp.configure(text='Campo fabricante vazio.')
                return True
  
            elif not len(fabricante)>= 2:
                lb_resp.configure(text='Insira um fabricante \ncom pelo menos 2 caracteres.')
                return False
              
            temp = ''.join(fabricante.split(' '))
            for i in temp:
                if not i.isalnum():
                    lb_resp.configure(text='Insira apenas letras \ne números no campo fabricante.')
                    return False
                   
            else:
                lb_resp.configure(text='')
                return fabricante.strip(' ')

    def Margem_lucro():
            margem_lucro = e_margemLucro.get()
            if (len(margem_lucro) == 0):
                lb_resp.configure(text='Campo margem de lucro vazio.')
                return True
               
            elif not margem_lucro.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo margem de lucro.')
                return False
        
            else:
                lb_resp.configure(text='')
                return margem_lucro.strip(' ')

    def Quantidade():
            quant_estoque = e_quantEsto.get()
            if (len(quant_estoque) == 0):
                lb_resp.configure(text='Campo quantidade \nno estoque vazio.')
                return True
      
            elif not quant_estoque.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo quant. no estoque.')
                return False
       
            else:
                lb_resp.configure(text='')
                return quant_estoque.strip(' ')

    def dataCadastro():
            data_atual = date.today()
            data_cadastro = data_atual.strftime('%d/%m/%Y')
            return data_cadastro


    lb_nome = Label(cadpro_frame, text='Nome do produto',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_nome.place(x = 20, y=70)
    e_nome = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Nome)
    e_nome.place(x=190,y=75)

    lb_cnpj = Label(cadpro_frame, text='CNPJ do produto',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_cnpj.place(x = 20, y=130)
    e_cnpj = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Cnpj)
    e_cnpj.place(x=190,y=135)

    v = tk.StringVar()
    lb_precoCusto = Label(cadpro_frame, text='Preço de custo',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_precoCusto.place(x = 20, y=195)
    e_precoCusto = Entry(cadpro_frame, textvariable= v ,width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Preco_custo)
    e_precoCusto.place(x=190,y=195)

    lb_precoV = Label(cadpro_frame, text='Preço de venda',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_precoV.place(x = 20, y=250)
    e_precoV= Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Preco_v)
    e_precoV.place(x=190,y=255)

    lb_codigoP = Label(cadpro_frame, text='Código do produto',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_codigoP.place(x = 20, y=310)
    e_codigoP = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Codigo_p)
    e_codigoP.place(x=190,y=310)

    lb_nomeF = Label(cadpro_frame, text='Nome do fornecedor',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_nomeF.place(x = 400, y=70)
    e_nomeF = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Nome_f)
    e_nomeF.place(x=600,y=75)

    lb_fabricante= Label(cadpro_frame, text='Fabricante',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_fabricante.place(x = 400, y=130)
    e_fabricante = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Fabricante)
    e_fabricante.place(x=600,y=135)

    lb_margemLucro = Label(cadpro_frame, text='Margem de lucro',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_margemLucro.place(x = 400, y=190)
    e_margemLucro = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Margem_lucro)
    e_margemLucro.place(x=600,y=195)

    lb_quantEsto = Label(cadpro_frame, text='Quantidade em \nestoque ',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_quantEsto.place(x = 400, y=250)
    e_quantEsto = Entry(cadpro_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Quantidade)
    e_quantEsto.place(x=600,y=255)


    #verificação
    

    def checkCOD(codigo_p):

        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"""SELECT codigo_p FROM produtos WHERE codigo_p == '{codigo_p}'""")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False

    def buscar(cnpj):
        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT cnpj FROM produtos WHERE cnpj == {cnpj}")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False

    def verificacaoP():
        nome_p = e_nome.get() 
        cnpj = e_cnpj.get()
        preco_custo = e_precoCusto.get()
        preco_v = e_precoV.get()
        codigo_p = e_codigoP.get()
        nome_f = e_nomeF.get()
        fabricante = e_fabricante.get()
        margem_lucro = e_margemLucro.get()
        quant_estoque = e_quantEsto.get()
        data_cadastro = dataCadastro()
    
    


        if (nome_p == "" or nome_p == " ") or (cnpj == "" or cnpj == " ") or (preco_custo == "" or preco_custo == " ") or (preco_v == "" or preco_v == " ") or (codigo_p == "" or codigo_p == " ") or (nome_f == "" or nome_f == " ") or (fabricante == "" or fabricante == " ") or (margem_lucro == "" or margem_lucro == " ") or (quant_estoque == "" or quant_estoque == " ") or (data_cadastro == "" or data_cadastro == " "):
                messagebox.showwarning("ERROR", "Por favor, preencha o espaço vazio.")
                return False

        elif(Nome() == False ) or (Cnpj() == False ) or (Preco_custo() ==False ) or (Preco_v() == False) or (Codigo_p()== False) or (Nome_f() == False ) or (Fabricante()== False ) or (Margem_lucro() == False) or (Quantidade() == False ) or (dataCadastro() == False ):
                messagebox.showwarning("ERROR", "Valor(es) inválido(s).")
                return False

        elif(buscar(cnpj)== True):
            messagebox.showwarning("ERROR", "CNPJ já existe.")
            return False


        

        if not checkCOD(codigo_p):
            bd = open("banco_de_dados.db", 'a')
            bd.write(f'Nome: {nome_p} -CNPJ: {cnpj} -Preço de custo: {preco_custo} -Preço de venda: {preco_v} -Código do produto: {codigo_p} -Fornecedor: {nome_f} -Fabricante: {fabricante} -Margem de Lucro: {margem_lucro} -Quantidade em estoque: {quant_estoque} -Data de cadastro: {data_cadastro}\n')
           
            cursor.execute(f"INSERT INTO produtos(nome_p, cnpj, preco_c, preco_v, codigo_p, nome_f, fabricante, margem_lucro, quant_estoque, data_cadastro) VALUES(?,?,?,?,?,?,?,?,?,?)", (nome_p, cnpj, preco_custo, preco_v, codigo_p, nome_f, fabricante, margem_lucro, quant_estoque, data_cadastro))
            con.commit() 
            messagebox.showinfo('SUCESSO','Produto cadastrado com sucesso!')

            bd.close()
         
            return 
        else: 
            messagebox.showwarning('ERRO','Já existe um produto com esse código.')
            return 


    criarFunc_btn = tk.Button(cadpro_frame, text='Cadastrar Produto',width=20, height=1, font='Ivy 12 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=verificacaoP)
    criarFunc_btn.place( x=370, y=400)
    
# TELA CADASTRO DE FUNCIONARIO
def cadastroFuncionario_pag():

    cadfun_frame = tk.Frame(main_frame, background= "white")
    lb = tk.Label(cadfun_frame, text='Cadastro de funcionário', font = ('Bold', 25), bg = "#3fb5a3")
    lb.pack(side= TOP, fill = tk.X)
    lb_resp = Label(cadfun_frame, font = ('Arial',12),text='',bg = 'white', fg= 'red')
    lb_resp.place(x=400, y=450)
    
    cadfun_frame.place(width = 1000, height =600 )

    def Nome():
        nome = e_nome.get()
        if (len(nome) == 0 ):
            lb_resp.configure(text='Campo nome vazio.')
            return True

        elif not len(nome)>= 2:
       
            lb_resp.configure(text='Digite um nome com pelo menos 2 caracteres.')
            return True
        temp = ''.join(nome.split(' '))
        for i in temp:
            if not i.isalpha(): #verifica se tem número
                lb_resp.configure(text='Digite um nome válido.')
                return False
                    
        else:
            lb_resp.configure(text='')
            return nome.strip(' ')
    
    def Tele():
            telefone = e_telefone.get()
            if (len(telefone) == 0):
                lb_resp.configure(text='Campo telefone vazio.')
                return True
   
            elif not telefone.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo telefone.')
                return False
        
            else:
                if 9 <= len(telefone) <= 11:
                    lb_resp.configure(text='')
                    return telefone.strip(' ')

                else:
                    lb_resp.configure(text='O número deve ter entre 9-11 caracteres.')
                    return False
             
    def Salario():
        salariof = e_salario.get()
        if (len(salariof) == 0):
            lb_resp.configure(text='Campo salário vazio.')
            return True
         
        elif not salariof.isdigit():
            lb_resp.configure(text='Insira apenas números no campo salário.')
            return False
     
        else:
            lb_resp.configure(text='')
            return salariof.strip(' ')
            
    def Data():
        data = e_dtNasci.get()
        if (len(data) == 0):
            lb_resp.configure(text='Campo data de nascimento vazio.')
            return True
    
        temp = ''.join(data.split('/')) #retorna uma string de valores sem '/'
        if not temp.isnumeric(): #analisa se a string tem caracteres
            lb_resp.configure(text='Insira uma data de nascimento válida.')
            return False
   
        if data.count('/') == 2 and data != '//':
            dia, mes, ano = map(int, data.split('/')) #cada valor dividido é jogado nas variaveis em sequencia
            if mes < 1 or mes > 12 or ano <= 0 or ano > 2022:
                lb_resp.configure(text='Insira uma data válida.')
                return False
           
            elif mes in (1, 3, 5, 7, 8, 10, 12):
                ult_dia = 31
            elif mes == 2:
                if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
            	    ult_dia = 29
                else:
                    ult_dia = 28
            else:
                ult_dia = 30
            
            if dia < 1 or dia > ult_dia:
                lb_resp.configure(text='Data inválida.')
                return False
         
            else:
                lb_resp.configure(text='')
                return data.strip(' ')

        else:
            lb_resp.configure(text='A data deve seguir o padrão dd/mm/aaaa.')
            return False
       
    def Rua():
        rua = e_rua.get()
        if (len(rua) == 0):
            lb_resp.configure(text='Campo rua vazio')
            return True

        temp1 = ''.join(rua.split(' '))
        for i in temp1:
            if not i.isalpha(): 
                lb_resp.configure(text='Insira apenas letras no campo rua.')
                return False
          
        else:
            lb_resp.configure(text='')
            return rua.strip(' ')    

    def NumeroCasa():
        numero = e_numero.get()
        if (len(numero) == 0):
            lb_resp.configure(text='Campo número da casa vazio.')
            return True 
        elif not numero.isnumeric():
            lb_resp.configure(text='Insira apenas dígitos no campo número.')
            return False 
   
        else:
            lb_resp.configure(text='')
            return numero.strip(' ')

    def Complemento():
        complemento = e_complemento.get()
        if (len(complemento) == 0):
            lb_resp.configure(text='Campo complemento vazio.')
            return True
 
        temp1 = ''.join(complemento.split(' '))
        for i in temp1:
            if not i.isalnum(): 
                lb_resp.configure(text='Insira apenas letras e números no campo complemento.')
                return False 
     
        else:
            lb_resp.configure(text='')
            return complemento.strip(' ')
   
    def Bairro():
        bairro = e_bairro.get()
        if (len(bairro) == 0):
        
            lb_resp.configure(text='Campo bairro vazio.')
            return True 
        temp1 = ''.join(bairro.split(' '))
        for i in temp1:
            if not i.isalnum():
                lb_resp.configure(text='Insira apenas letras e números no campo bairro.')
                return False 
                 
        else:
            lb_resp.configure(text='')
            return bairro.strip(' ')

    def Cep():
        cep = e_cep.get()
        if (len(cep) == 0):
            lb_resp.configure(text='Campo CEP vazio.')
            return True
    
        elif not cep.isnumeric():
            lb_resp.configure(text='Insira apenas números no campo CEP.')
            return False
        
        elif len(cep)!=8 :
            lb_resp.configure(text='Insira 8 caracteres no campo CEP.')
            return False
  
        else:
            lb_resp.configure(text='')
            return cep.strip(' ')

    def Cidade():
        cidade = e_cidade.get()
        if (len(cidade)== 0):
            lb_resp.configure(text='Campo cidade vazio')
            return True
          
        temp2 = ''.join(cidade.split(' '))
        for i in temp2:
            if not i.isalpha(): 
                lb_resp.configure(text='Insira apenas letras no campo cidade.')
                return False
     
        else:
            lb_resp.configure(text='')
            return cidade.strip(' ')

    def Email():

        email = e_email.get()
        if (len(email) == 0):
           lb_resp.configure(text='Campo email vazio.')
           return True
        elif not len(email)>= 6:
            lb_resp.configure(text='Insira um email com pelo menos 6 caracteres.')
            return False
        elif not '@' in email:
            lb_resp.configure(text='Insira um email que contenha o caractere "@".')
            return False
        elif '@' in email:
            lb_resp.configure(text='')
            return email.strip(' ')
    
    def dataCadastro():
            data_atual = date.today()
            data_cadastro = data_atual.strftime('%d/%m/%Y')
            return data_cadastro

    def id_F():
            id_fun= e_idFun.get()
            if (len(id_fun) == 0):
                lb_resp.configure(text='Campo ID vazio.')
                return True
        
            elif not id_fun.isnumeric():
                lb_resp.configure(text='Insira apenas números \nno campo ID.')
                return False
           
            else:
                lb_resp.configure(text='')
                return id_fun.strip(' ')
        

    lb_nome = Label(cadfun_frame, text='Nome do Funcionário',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_nome.place(x = 20, y=70)
    e_nome = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Nome)
    e_nome.place(x=240,y=75)

    lb_idFun = Label(cadfun_frame, text='ID do Funcionário',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_idFun.place(x = 20, y=130)
    e_idFun = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = id_F)
    e_idFun.place(x=240,y=135)

    lb_telefone = Label(cadfun_frame, text='Telefone do Funcionário',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_telefone.place(x = 20, y=190)
    e_telefone = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Tele)
    e_telefone.place(x=240,y=195)

    lb_salario = Label(cadfun_frame, text='Salário do Funcionário',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_salario.place(x = 20, y=250)
    e_salario = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Salario)
    e_salario.place(x=240,y=255)

    lb_dtNasci = Label(cadfun_frame, text='Data de Nascimento',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_dtNasci.place(x = 20, y=310)
    e_dtNasci= Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Data)
    e_dtNasci.place(x=240,y=315)

    lb_email = Label(cadfun_frame, text='Email do Funcionário',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_email.place(x = 20, y=370)
    e_email = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Email)
    e_email.place(x=240,y=375)

    #endereço
    lb_rua = Label(cadfun_frame, text='Rua ',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_rua.place(x = 450, y=70)
    e_rua = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Rua)
    e_rua.place(x=580,y=75)

    lb_numero = Label(cadfun_frame, text='Número ',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_numero.place(x = 450, y=130)
    e_numero = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = NumeroCasa)
    e_numero.place(x=580,y=135)

    lb_complemento = Label(cadfun_frame, text='Complemento',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_complemento.place(x = 450, y=190)
    e_complemento = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Complemento)
    e_complemento.place(x=580,y=195)

    lb_bairro = Label(cadfun_frame, text='Bairro',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_bairro.place(x = 450, y=250)
    e_bairro = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Bairro)
    e_bairro.place(x=580,y=255)

    lb_cep = Label(cadfun_frame, text='CEP',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_cep.place(x =450 , y=310)
    e_cep = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Cep)
    e_cep.place(x=580,y=315)

    lb_cidade = Label(cadfun_frame, text='Cidade',anchor= NW, font='Ivy 15', bg = 'white', fg= co4)
    lb_cidade.place(x = 450, y=370)
    e_cidade = Entry(cadfun_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Cidade)
    e_cidade.place(x=580,y=375)


    def checkID(id_f):

        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT id FROM funcionarios WHERE id == {id_f}")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False

    def check_collect():
            nome = e_nome.get()
            id_f = e_idFun.get()
            email = e_email.get()
            data = e_dtNasci.get()
            tele = e_telefone.get()
            salariof = e_salario.get()
            data_cadas = dataCadastro()
            rua = e_rua.get()
            numero = e_numero.get()
            complemento = e_complemento.get()
            bairro = e_bairro.get()
            cep = e_cep.get()
            cidade = e_cidade.get()

            if (nome == "" or nome== " ") or (id_f == "" or id_f == " ") or (email == "" or email == " ") or (data == "" or data == " ") or (tele == "" or tele == " ") or (salariof == "" or salariof == " ") or (data_cadas== "" or data_cadas == " ") or (rua == "" or rua == " ") or (numero == "" or numero == " ") or (complemento == "" or complemento == " ")or (cep == "" or cep == " ")or (cidade == "" or cidade == " "):
                messagebox.showwarning("ERROR", "Por favor, preencha o espaço vazio.")
                return False

            elif(Nome()== False) or (Tele()== False) or (Salario()==False) or (Data()==False) or (Rua()==False) or (NumeroCasa() == False) or (Complemento()== False) or (Bairro() == False) or (Cep() == False) or (Cidade()== False) or (Email() == False) or (id_F() == False):
                messagebox.showwarning("ERROR", "Valor(es) inválido(s).")
                return False 
        

            if not checkID(id_f):
                bd = open("banco_de_dados.db", 'a')
                bd.write(f'Nome: {nome} -ID: {id_f} -Email: {email} -Data de nascimento: {data} -Número de celular: {tele} -Data de cadastro do funcionário: {data_cadas} -Salário: ${salariof} -Rua: {rua} -Número da casa: {numero} -Complemento: {complemento} -Bairro: {bairro} -CEP: {cep} -Cidade: {cidade} \n')
                f = open("funcionarios.txt", 'a')
                f.write(f'Nome: {nome} -ID: {id_f} -Email: {email} -Data de nascimento: {data} -Número de celular: {tele} -Data de cadastro do funcionário: {data_cadas} -Salário: ${salariof} -Rua: {rua} -Número da casa: {numero} -Complemento: {complemento} -Bairro: {bairro} -CEP: {cep} -Cidade: {cidade} \n')
               
                cursor.execute(f"INSERT INTO funcionarios (nome, id, email, data, tele, salariof, data_cadastro, rua, numero, complemento, bairro, cep, cidade) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (nome, id_f, email, data, tele, salariof, data_cadas,rua, numero, complemento, bairro, cep, cidade))
                con.commit() 
               
                messagebox.showinfo('SUCESSO','Funcionário cadastrado com sucesso!')

                bd.close()
                f.close()

            
                return 
            else: 
                messagebox.showwarning('ERROR', 'ID já existe')

    criarFunc_btn = tk.Button(cadfun_frame, text='Cadastrar Funcionário',width=20, height=1, font='Ivy 12 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=check_collect)
    criarFunc_btn.place( x=150, y=450)
        
# TELA ATUALIZACAO DE PRODUTO
def entrada_pag():

    con = sqlite3.connect('banco_de_dados.db')
    cursor = con.cursor()

    ent_frame = tk.Frame(main_frame, background= "white")
    
    lb = tk.Label(ent_frame, text='Entrada de produtos', font = ('Bold', 25), bg = "#3fb5a3")
    lb.pack(side= TOP, fill = tk.X)
    lb_resp = Label(ent_frame, text='',bg = 'white', fg= 'red')
    lb_resp.place(x = 300, y = 270)
    ent_frame.place(width = 1000, height = 600) 

    def dataCadastro():

            data_atual = date.today()
            data_cadastro = data_atual.strftime('%d/%m/%Y')
            return data_cadastro

    def Nome():
        nome = e_nome.get()
        if (len(nome) == 0):
            lb_resp.configure(text='Campo nome vazio.')
            return True

        elif not len(nome)>= 2:
            lb_resp.configure(text='Digite um nome com pelo menos 2 caracteres.')
            return True
        temp = ''.join(nome.split(' '))
        for i in temp:
            if not i.isalpha(): #verifica se tem número
                lb_resp.configure(text='Digite um nome válido.')
                return False
        else:
            lb_resp.configure(text='')
            return nome.strip(' ')

    def Cnpj():
            cnpj = e_cnpj.get()
            if (len(cnpj) == 0):
                lb_resp.configure(text='Campo CNPJ vazio.')
                return True
             
            elif not cnpj.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo CNPJ.')
                return False
             
            if not(len(cnpj) == 14):
                lb_resp.configure(text='Insira um CNPJ com 14 caracteres.')
                return False
             
            else:
                lb_resp.configure(text='')
                return cnpj.strip(' ')

    def Preco_custo():
            preco_custo = e_preco_custo.get()
            if (len(preco_custo) == 0):
                lb_resp.configure(text='Campo preço de custo vazio.')
                return True
        
            elif not preco_custo.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo preço de custo.')
                return False
             
            else:
                lb_resp.configure(text='')
                return preco_custo.strip(' ')

    def Preco_v():
            preco_v = e_precoV.get()
            if (len(preco_v)== 0):
                lb_resp.configure(text='Campo preço de venda vazio.')
                return True
              
            elif not preco_v.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo preço de venda.')
                return False
             
            else:
                lb_resp.configure(text='')
                return preco_v.strip(' ')

    def Codigo_p():
            codigo_p = e_codigoP.get()
            if (len(codigo_p) == 0):
                lb_resp.configure(text='Campo código vazio.')
                return True
            
            elif not codigo_p.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo código.')
                return False
         
            else:
                lb_resp.configure(text='')
                return codigo_p.strip('')

    def Nome_f():
            nome_f = e_nomeF.get()
            if (len(nome_f) == 0):
                lb_resp.configure(text='Campo fornecedor vazio.')
                return True
               
            elif not len(nome_f)>= 2:
                lb_resp.configure(text='Insira um fornecedor com pelo menos 2 caracteres.')
                return False
                
            temp = ''.join(nome_f.split(' '))
            for i in temp:
                if not i.isalnum():
                    lb_resp.configure(text='Insira apenas letras e números no campo fornecedor.')
                    return False
                
            else:
                lb_resp.configure(text='')
                return nome_f.strip(' ')

    def Fabricante():
            fabricante = e_fabricante.get()
            if (len(fabricante) == 0):
                lb_resp.configure(text='Campo fabricante vazio.')
                return True
              
            elif not len(fabricante)>= 2:
                lb_resp.configure(text='Insira um fabricante com pelo menos 2 caracteres.')
                return False
               
            temp = ''.join(fabricante.split(' '))
            for i in temp:
                if not i.isalnum():
                    lb_resp.configure(text='Insira apenas letras e números no campo fabricante.')
                    return False
                   
            else:
                lb_resp.configure(text='')
                return fabricante.strip(' ')

    def Margem_lucro():
            margem_lucro = e_margemLucro.get()
            if (len(margem_lucro) == 0):
                lb_resp.configure(text='Campo margem de lucro vazio.')
                return True
              
            elif not margem_lucro.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo margem de lucro.')
                return False
               
            else:
                lb_resp.configure(text='')
                return margem_lucro.strip(' ')

    def Quantidade():
            quant_estoque = e_quantEsto.get()
            if (len(quant_estoque) == 0):
                lb_resp.configure(text='Campo quantidade no estoque vazio.')
                return True
              
            elif not quant_estoque.isnumeric():
                lb_resp.configure(text='Insira apenas números no campo quant. no estoque.')
                return False
         
            else:
                lb_resp.configure(text='')
                return quant_estoque.strip(' ')

    lb_nome = Label(ent_frame, text='Nome',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_nome.place(x = 10, y=60)
    e_nome = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Nome)
    e_nome.place(x=115,y=60)

    lb_cnpj = Label(ent_frame, text='CNPJ',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_cnpj.place(x = 10, y=100)
    e_cnpj = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Cnpj)
    e_cnpj.place(x=115,y=100)

    lb_preco_custo = Label(ent_frame, text='Preço de custo',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_preco_custo.place(x = 10, y=140)
    e_preco_custo = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Preco_custo)
    e_preco_custo.place(x=115,y=140)

    lb_precoV = Label(ent_frame, text='Preço de venda',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_precoV.place(x = 10, y=180)
    e_precoV= Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Preco_v)
    e_precoV.place(x=115,y=180)

    lb_codigoP = Label(ent_frame, text='Código do \nproduto',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_codigoP.place(x = 10, y=220)
    e_codigoP = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Codigo_p )
    e_codigoP.place(x=115,y=230)

    lb_nomeF = Label(ent_frame, text='Nome do \nfornecedor',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_nomeF.place(x = 310, y=60)
    e_nomeF = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Nome_f)
    e_nomeF.place(x=400,y=70)

    lb_fabricante= Label(ent_frame, text='Fabricante',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_fabricante.place(x = 310, y=100)
    e_fabricante = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Fabricante)
    e_fabricante.place(x=400,y=105)

    lb_margemLucro = Label(ent_frame, text='Margem \nde lucro',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_margemLucro.place(x = 310, y=140)
    e_margemLucro = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout", validatecommand = Margem_lucro)
    e_margemLucro.place(x=400,y=150)

    lb_quantEsto = Label(ent_frame, text='Quantidade \nem estoque ',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_quantEsto.place(x = 310, y=180)
    e_quantEsto = Entry(ent_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid',validate = "focusout",validatecommand = Quantidade)
    e_quantEsto.place(x=400,y=190)


    nome_p = e_nome.get() 
    cnpj = e_cnpj.get()
    preco_c = e_preco_custo.get()
    preco_v = e_precoV.get()
    codigo_p = e_codigoP.get()
    nome_f = e_nomeF.get()
    fabricante = e_fabricante.get()
    margem_lucro = e_margemLucro.get()
    quant_estoque = e_quantEsto.get()
    data_cadastro = dataCadastro()


    def GetValue(event):
        nome_p.delete(0, END)
        cnpj.delete(0, END)
        preco_c.delete(0, END)
        preco_v.delete(0, END)
        codigo_p.delete(0, END)
        nome_f.delete(0, END)
        fabricante.delete(0, END)
        margem_lucro.delete(0, END)
        quant_estoque.delete(0, END)
        data_cadastro.delete(0, END)
        row_codigo = listBox.selection()[0]
        select = listBox.set(row_codigo)
        nome_p.insert(0, select['nome_p'])
        cnpj.insert(0, select['cnpj'])
        preco_c.insert(0, select['preco_c'])
        preco_v.insert(0, select['preco_v'])
        codigo_p.insert(0, select['codigo_p.'])
        nome_f.insert(0, select['nome_f'])
        fabricante.insert(0, select['fabricante'])
        margem_lucro.insert(0, select['margem_lucro'])
        quant_estoque.insert(0, select['quant_estoque'])
        data_cadastro.insert(0, select['data_cadastro'])

    def buscar_(codigo_p):
        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT codigo_p FROM produtos WHERE codigo_p == {codigo_p}")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False
    
    def confirme():

            nome_p = e_nome.get() 
            cnpj = e_cnpj.get()
            preco_c = e_preco_custo.get()
            preco_v = e_precoV.get()
            codigo_p = e_codigoP.get()
            nome_f = e_nomeF.get()
            fabricante = e_fabricante.get()
            margem_lucro = e_margemLucro.get()
            quant_estoque = e_quantEsto.get()
            data_cadastro = dataCadastro()

            try:


                if (nome_p == "" or nome_p == " ") or (cnpj == "" or cnpj == " ") or (preco_c == "" or preco_c == " ") or (preco_v == "" or preco_v == " ") or (codigo_p == "" or codigo_p == " ") or (nome_f == "" or nome_f == " ") or (fabricante == "" or fabricante == " ") or (margem_lucro == "" or margem_lucro == " ") or (quant_estoque == "" or quant_estoque == " ") or (data_cadastro == "" or data_cadastro == " "):
                        messagebox.showwarning("ERROR", "Por favor, preencha o espaço vazio.")
                        return False

                elif(Nome()== False ) or (Cnpj() == False) or (Preco_custo() == False) or (Preco_v() == False) or (Codigo_p() == False ) or (Nome_f() == False ) or (Fabricante() == False ) or (Margem_lucro() == False) or (Quantidade()== False):
                        messagebox.showwarning("ERROR","Valor(es) inválido(s)")
                        return False

                elif buscar_(codigo_p) == False:
                        messagebox.showwarning("ERROR","Produto não existe no banco de dados")
                        return False

                else:
                    cursor.execute(f"UPDATE produtos SET nome_p = '{nome_p}', cnpj= {cnpj}, preco_c = '{preco_c}', preco_v = '{preco_v}', codigo_p = '{codigo_p}', nome_f = '{nome_f}', fabricante = '{fabricante}', margem_lucro = '{margem_lucro}', quant_estoque = '{quant_estoque}', data_cadastro = '{data_cadastro}' WHERE codigo_p = '{codigo_p}'")
                    con.commit()
                    messagebox.showinfo("SUCESSO", "Entrada alterada com sucesso!")

                e_nome.delete(0, END)
                e_cnpj.delete(0, END)
                e_preco_custo.delete(0, END)
                e_precoV.delete(0, END)
                e_codigoP.delete(0, END)
                e_nomeF.delete(0, END)
                e_fabricante.delete(0, END)
                e_margemLucro.delete(0, END)
                e_quantEsto.delete(0, END)
                e_codigoP.focus_set()

                show()
        
            except Exception as e:
                print(e)
                con.rollback()
                
    def update():
        try:
            con = sqlite3.connect('banco_de_dados.db')
            cursor = con.cursor()   


            treev_dados = listBox.focus()
            treev_dicionario = listBox.item(treev_dados)
            tree_lista = treev_dicionario['values']

            nome_p = tree_lista[0]
            cnpj = tree_lista[1]
            preco_c =tree_lista[2]
            preco_v =tree_lista[3]
            codigo_p = tree_lista[4]
            nome_f = tree_lista[5]
            fabricante = tree_lista[6]
            margem_lucro = tree_lista[7]
            quant_estoque = tree_lista[8]
       
            e_nome.delete(0, END)
            e_cnpj.delete(0, END)
            e_preco_custo.delete(0, END)
            e_precoV.delete(0, END)
            e_codigoP.delete(0, END)
            e_nomeF.delete(0, END)
            e_fabricante.delete(0, END)
            e_margemLucro.delete(0, END)
            e_quantEsto.delete(0, END)
            e_codigoP.focus_set()
            
            e_nome.insert(0, nome_p)
            e_cnpj.insert(0, cnpj)
            e_preco_custo.insert(0, preco_c)
            e_precoV.insert(0, preco_v)
            e_codigoP.insert(0, codigo_p)
            e_nomeF.insert(0, nome_f)
            e_fabricante.insert(0, fabricante)
            e_margemLucro.insert(0, margem_lucro)
            e_quantEsto.insert(0, quant_estoque)
             
        except Exception as e:
            print(e)
            
    lb_confirmeBT = Button(ent_frame, text='Confirmar', font='Ivy 10 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=confirme) #comando update
    lb_confirmeBT.place(x = 480, y=230)
    lb_procurarBT = Button(ent_frame, text='Atualizar', font='Ivy 10 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=update) #seleciona entry
    lb_procurarBT.place(x = 340, y=230)
        
    def show():
        cursor.execute("SELECT nome_p, cnpj, preco_c, preco_v, codigo_p, nome_f, fabricante, margem_lucro, quant_estoque, data_cadastro FROM produtos")
        records = cursor.fetchall()
     

        
        for i, (nome_p, cnpj, preco_c, preco_v, codigo_p, nome_f, fabricante, margem_lucro, quant_estoque, data_cadastro) in enumerate(records, start=1):
            listBox.insert("", "end", values=(nome_p, cnpj, preco_c, preco_v, codigo_p, nome_f, fabricante, margem_lucro, quant_estoque, data_cadastro))
        
    cols = ['nome_p', 'cnpj', 'preco_c', 'preco_v', 'codigo_p', 'nome_f', 'fabricante', 'margem_lucro', 'quant_estoque', 'data_cadastro']
    
    Y = ttk.Scrollbar(ent_frame,orient='vertical')
    X = ttk.Scrollbar(ent_frame,orient='horizontal')
    listBox = ttk.Treeview(ent_frame, columns=cols, show='headings', yscrollcommand=Y.set, xscrollcommand= X.set) # TODO linkar a barra com a listagem (listbox)
    
    Y.place(x= 550,y=300)
    X.place(x= 300 ,y=300)

    for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=10, y=300)

    show()
  
    listBox.heading(0,text = 'Nome', anchor = NW)
    listBox.heading(1,text = 'CNPJ', anchor = NW)
    listBox.heading(2,text = 'Preço de custo', anchor = NW)
    listBox.heading(3,text = 'Preço de venda', anchor = NW)
    listBox.heading(4,text = 'Código', anchor = NW)
    listBox.heading(5,text = 'Fornecedor', anchor = NW)
    listBox.heading(6,text = 'Fabricante', anchor = NW)
    listBox.heading(7,text = 'Margem de lucro', anchor = NW)
    listBox.heading(8,text = 'Estoque', anchor = NW)
    listBox.heading(9,text = 'Data de cadastro', anchor = NW)

    listBox.column(0, width=80, anchor = 'nw')
    listBox.column(1, width=120, anchor = 'nw')
    listBox.column(2, width=85, anchor = 'nw')
    listBox.column(3, width=120, anchor = 'nw')
    listBox.column(4, width=80, anchor = 'nw')
    listBox.column(5, width=90, anchor = 'nw')
    listBox.column(6, width=80, anchor = 'nw')
    listBox.column(7, width=100, anchor = 'nw')
    listBox.column(8, width=80, anchor = 'nw')
    listBox.column(9, width=100, anchor = 'nw')

# TELA BUSCA DE FUNCIONARIO
def buscaFuncionario_pag():

    bs_frame = tk.Frame(main_frame, background='white')
    bs_frame.place(width = 1000, height = 600)

   
    lb = tk.Label(bs_frame, text='Busca de funcionário', font = ('Bold', 25), bg = "#3fb5a3")
    lb.pack(side= TOP, fill = tk.X)
    lb_resp = Label(bs_frame, text='',bg = 'white', fg= 'red')
    lb_resp.place(x = 350 , y=240)



    def id_Num():
            numero = e_id.get()
            if (len(numero) == 0):
                lb_resp.configure(text='Entrada vazia.')
                return True
             
            elif not numero.isnumeric():
                lb_resp.configure(text='Insira apenas números.')
                return False
            
            else:
                lb_resp.configure(text='')
                return numero.strip(' ')

    def voltar():
        listBox.delete(*listBox.get_children())
        a = cursor.execute(f"SELECT * FROM funcionarios")
        for i in a:
            listBox.insert("","end",values=i)


    lb_id = Label(bs_frame, text='ID',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_id.place(x =350, y=130)
    e_id = Entry(bs_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand= id_Num)
    e_id.place(x=370,y=130)
    

    def mostraDados():
        id_funcionario = e_id.get()
        b = buscar_F(id_funcionario)
        
        if id_Num() == True:
            messagebox.showwarning('ERRO','ID vazio!')
            return False 
        if id_Num() == False:
            messagebox.showwarning('ERRO','Valor inválido!')
            return False
        elif b == False:
            messagebox.showwarning('ERRO','Funcionário não se encontra na base de dados!')
            return False

        else:
            listBox.delete(*listBox.get_children())
            a = cursor.execute(f"SELECT nome, id, email, data,tele ,salariof, data_cadastro, rua, numero, complemento, bairro, cep, cidade FROM funcionarios WHERE id = '{id_funcionario}'")
            for i in a:
                listBox.insert("","end",values=i)

    lb_voltarBT = Button(bs_frame, text='Voltar', font='Ivy 10 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=voltar) #comando update
    lb_voltarBT.place(x = 530, y=180)               
        

  

    def buscar_F(id_f):
        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT id FROM funcionarios WHERE id == '{id_f}'")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False



    
    criarFunc_btn = tk.Button(bs_frame, text='Buscar Funcionário',width=20, height=1, font='Ivy 10 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE, command=mostraDados)
    criarFunc_btn.place( x=350, y=180)

    cols = ['Nome','ID', 'Email','Data','Telefone','Salário','Data de cadastro','Rua','Numero','Complemento', 'Bairro','CEP', 'Cidade']
    
   
    listBox = ttk.Treeview(bs_frame, columns=cols, show='headings') # TODO linkar a barra com a listagem (listbox)


    for col in cols:
        listBox.heading(col, text=col)
        listBox.place(x=10, y=300) 

    def show():
        cursor.execute("SELECT nome, id, email, data,tele ,salariof, data_cadastro, rua, numero, complemento, bairro, cep, cidade FROM funcionarios")
        records = cursor.fetchall()
    

        
        for i, (nome, id, email, data, tele, salariof, data_cadastro, rua, numero, complemento, bairro, cep, cidade) in enumerate(records, start=1):
            listBox.insert("", "end", values=(nome,id, email, data, tele, salariof, data_cadastro, rua, numero, complemento, bairro, cep, cidade))
        

    for col in cols:
        listBox.heading(col, text=col)
   
        listBox.place(x=10, y=300)

    show()
    #listBox.bind('<Double-Button-1>',GetValue)

    listBox.heading(0,text = 'Nome', anchor = NW)
    listBox.heading(1,text = 'ID', anchor = NW)
    listBox.heading(2,text = 'Email', anchor = NW)
    listBox.heading(3,text = 'Data', anchor = NW)
    listBox.heading(4,text = 'Telefone', anchor = NW)
    listBox.heading(5,text = 'Salario', anchor = NW)
    listBox.heading(6,text = 'Data de cadastro', anchor = NW)
    listBox.heading(7,text = 'Rua', anchor = NW)
    listBox.heading(8,text = 'Número', anchor = NW)
    listBox.heading(9,text = 'Complemento', anchor = NW)
    listBox.heading(10,text = 'Bairro', anchor = NW)
    listBox.heading(11,text = 'CEP', anchor = NW)
    listBox.heading(12,text = 'Cidade', anchor = NW)

    listBox.column(0, width=80, anchor = 'nw')
    listBox.column(1, width=50, anchor = 'nw')
    listBox.column(2, width=90, anchor = 'nw')
    listBox.column(3, width=70, anchor = 'nw')
    listBox.column(4, width=80, anchor = 'nw')
    listBox.column(5, width=70, anchor = 'nw')
    listBox.column(6, width=80, anchor = 'nw')
    listBox.column(7, width=60, anchor = 'nw')
    listBox.column(8, width=80, anchor = 'nw')
    listBox.column(9, width=100, anchor = 'nw')
    listBox.column(10, width=80, anchor = 'nw')
    listBox.column(11, width=80, anchor = 'nw')
    listBox.column(12, width=100, anchor = 'nw')
    
# TELA CADASTRO DE LOGIN
def cadLogin():
    log_frame = tk.Frame(janela, background= "white")
    lb = tk.Label(log_frame, text='Cadastro de Login', font = ('Bold', 12), bg = "#3fb5a3", anchor = NW)
    lb.pack(side= TOP, fill = tk.X)
    lb_resp = Label(log_frame, text='',bg = 'white', fg= 'red')
    lb_resp.place(x = 90 , y=220)
    log_frame.place(width = 700, height =600 )

    def Nome():
        nome = e_user.get()
        if (len(nome) == 0):
            lb_resp.configure(text='Campo User vazio.')
            return True

        elif not len(nome)>= 2:
            lb_resp.configure(text='Digite um User com \npelo menos 2 caracteres.')
            return True
        temp = ''.join(nome.split(' '))

        for i in temp:
            if not i.isalpha(): #verifica se tem número
                lb_resp.configure(text='Digite um User válido.')
                return False
        else:
            lb_resp.configure(text='')
            return nome.strip(' ')

    def Email():
        email = e_email.get()
        if (len(email) == 0):
            lb_resp.configure(text='Erro! Entrada email vazia.')
            return True
        elif not len(email)>= 6:
            lb_resp.configure(text='Insira um email com \npelo menos 5 caracteres.')
            return False
        elif '@' in email:
            lb_resp.configure(text='')
            return email.strip(' ')  
        else:
            lb_resp.configure(text='Email inválido! \nDeve conter "@"')
            return False
          
    def Senha():
        senha = e_senha.get()
        if (len(senha) == 0):
            lb_resp.configure(text='Erro! Entrada senha vazia.')
            return True

        if not 4 <= len(senha) <= 8:
            lb_resp.configure(text='Digite uma senha \nentre 4 e 8 caracteres.')
            return False

        else:
            lb_resp.configure(text='')
            return senha.strip(' ')

    def checkLogin(login):

        connection = sqlite3.connect('banco_de_dados.db')
        cursor = connection.cursor()

        cursor.execute(f"""SELECT login FROM logins WHERE login == '{login}'""")
            
        connection.commit()
        response = cursor.fetchall()
        connection.close()

        if response:
            return True 
        else: 
            return False

    def verificacaoL():
        login = e_user.get() 
        senha = e_senha.get()
        email = e_email.get()
        
        if (login == "" or login == " ") or (senha == "" or senha == " ") or (email == "" or email == " "):
                messagebox.showwarning("ERROR", "Por favor, preencha o espaço vazio.")
                return False

        elif(Nome()== False ) or (Email() == False) or (Senha() == False):
                        messagebox.showwarning("ERROR","Valor(es) inválido(s)")
                        return False

        if not checkLogin(login):
            bd = open("banco_de_dados.db", 'a')
            bd.write(f'User: {login} -Senha: {senha} -Email: {email}\n')
            f = open("logins.txt", 'a')
            f.write(f'User: {login} -Senha: {senha} -Email: {email}\n')

            
            cursor.execute(f"INSERT INTO logins (login, senha, email) VALUES(?,?,?)", (login, senha, email))
            con.commit() 
            messagebox.showinfo('SUCESSO','Login criado com sucesso!')

            bd.close()
            f.close()
            return 
        else: 
                messagebox.showwarning('ERRO','Esse login já existe.')
                return 

    lb_user = Label(log_frame, text='User',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_user.place(x = 10, y=60)
    e_user = Entry(log_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Nome)
    e_user.place(x=90,y=60)

    lb_senha = Label(log_frame, text='Senha',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_senha.place(x = 10, y=100)
    e_senha = Entry(log_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Senha)
    e_senha.place(x=90,y=100)

    lb_email = Label(log_frame, text='E-mail',anchor= NW, font='Ivy 10', bg = 'white', fg= co4)
    lb_email.place(x = 10, y=140)
    e_email = Entry(log_frame, width=25, justify= 'left', font=("",10), highlightthickness=1, relief='solid', validate = "focusout", validatecommand = Email)
    e_email.place(x=90,y=140)

    b_botcad = Button(log_frame, text='Cadastrar Login', font='Ivy 10 bold', overrelief= RIDGE, bg = "#3fb5a3", fg= 'white', command = verificacaoL)
    b_botcad.place(x = 90, y=180)

global venda_j
global a

def Venda_pg():
    global venda_j
    global a
    venda_j = tk.Toplevel()
    a = Venda(venda_j)
    venda_j.title('VENDA')
    venda_j.mainloop()

NomeCliente = StringVar()
IdCli = StringVar()
Quant = StringVar()
Data= StringVar()



class item:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class carrinho:
    def __init__(self):
        self.itens = []
        self.dicionario = {}

    def adicionarItem(self,item):
        self.itens.append(item)

    def removerItem(self):
        self.itens.pop()
    
    def removerItens(self):
        self.itens.clear()
    
    def Total(self):
        total = 0.0
        for i in self.itens:
            total += i.preco * i.quantidade
        return total 
    
    def vazio(self):
        if len(self.itens) == 0:
            return True 

    def carrinhoCheio(self):
        for i in self.itens:
            if i.nome in self.dicionario:
                self.dicionario[i.nome] += i.quantidade
            else:
                self.dicionario.update({i.nome:i.quantidade})



   
class Venda:
    def __init__(self,top = None):
        global venda_j
        top.geometry('1000x650')
        top.resizable(0,0)
        top.title('VENDA')
        top.configure(bg = 'white smoke')


        def Nome():
            nome = self.e_nomeCliente.get()
            if (len(nome) == 0):
                return True

            elif not len(nome)>= 2:
                return True
            temp = ''.join(nome.split(' '))

            for i in temp:
                if not i.isalpha():
                    return False
            else:
                return nome.strip(' ')

        def Quantidade():
            quant_estoque = self.e_quant.get()
            if (len(quant_estoque) == 0):
                return True
              
            elif not quant_estoque.isnumeric():
                return False
         
            else:
                return quant_estoque.strip(' ')
        
        


        
      
        self.lb_nomeCliente = Label(venda_j, text='Nome do cliente',anchor= NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_nomeCliente.place(x = 20, y=50)


        self.lb_idCli = Label(venda_j, text='Id do cliente',anchor= NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_idCli.place(x = 480, y=50)

        self.lb_info = Label(venda_j, text='INFORMAÇÕES DO PRODUTO', anchor=NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_info.place(x = 100, y=130)

        self.lb_nome_p = Label(venda_j, text='Produto',anchor= NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_nome_p.place(x = 20, y=200)

        self.lb_preco = Label(venda_j, text='Preço',anchor= NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_preco.place(x = 20, y=300)

        self.lb_quant = Label(venda_j, text='Quant.',anchor= NW, font = "-family {Poppins} -size 12", bg = 'white smoke', fg= 'black')
        self.lb_quant.place(x = 20, y=400)

        self.lb_pro_scroll = Label(venda_j, text='PRODUTO',anchor= NW, font = "bold", bg = 'white smoke', fg= 'black')
        self.lb_pro_scroll.place(x = 480, y=120)

        self.lb_quant_scroll = Label(venda_j, text='QUANTIDADE',anchor= NW, font = "bold", bg = 'white smoke', fg= 'black')
        self.lb_quant_scroll.place(x = 610, y=120)

        self.lb_preco_scroll = Label(venda_j, text='PREÇO',anchor= NW, font = "bold", bg = 'white smoke', fg= 'black')
        self.lb_preco_scroll.place(x = 800, y=120)

        self.e_nomeCliente = Entry(venda_j, validatecommand= Nome) 
        self.e_nomeCliente.place(x = 160, y =50, width=240, height= 30)
        self.e_nomeCliente.configure(textvariable= NomeCliente, font = "-family {Poppins} -size 12" )

        self.tx_idCli = Text(venda_j) 
        self.tx_idCli.place(x = 590, y = 50, width=240, height= 30)
        self.tx_idCli.configure( font = "-family {Poppins} -size 12", bg='white smoke', borderwidth=0 )



        self.e_quant = ttk.Entry(venda_j,validatecommand=Quantidade)
        self.e_quant.place(x=100, y=400, width=300, height=30)
        self.e_quant.configure(textvariable= Quant, font="-family {Poppins} -size 8", state="disabled")

        self.adicionar_btn = Button(venda_j)
        self.adicionar_btn.place(x = 50 , y =570, width=120, height= 26)
        self.adicionar_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Adicionar', command= self.add_to_cart)

        self.removerItem_btn = Button(venda_j)
        self.removerItem_btn.place(x = 200 , y =570, width=120, height= 26 )
        self.removerItem_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Remover Produto', command= self.remove_product)

        self.removerItens_btn = Button(venda_j)
        self.removerItens_btn.place(x = 350 , y =570, width=120, height= 26 )
        self.removerItens_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Limpar Conta', command= self.clear_bill)

        self.limparInformacao_btn = Button(venda_j)
        self.limparInformacao_btn.place(x = 500 , y =570, width=120, height= 26 )
        self.limparInformacao_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Limpar Produto', command= self.clear_selection)

        self.Total_btn = Button(venda_j)
        self.Total_btn.place(x = 650 , y =570, width=120, height= 26)
        self.Total_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Total', command= self.total_bill)

        self.confirmar_btn = Button(venda_j)
        self.confirmar_btn.place(x = 800 , y =570, width=120, height= 26)
        self.confirmar_btn.configure(cursor='hand2', fg= '#ffffff', bg= co2, font = "-family {Poppins SemiBold} -size 12", borderwidth= '0', text= 'Confirmar', command= self.confirmar)

        self.produtoScroll = tkst.ScrolledText(top)
        self.produtoScroll.place(x=480 , y=140 , width=430, height= 380)
        self.produtoScroll.configure(font = "-family {Podkova} -size 10", borderwidth= 0, state = 'disabled' )

       
      

        text_font = ("Poppins", "10")
        self.nome = ttk.Combobox(venda_j)
        self.nome.place(x=100, y=200, width=300, height=30)
        self.preco = ttk.Combobox(venda_j)
        self.preco.place(x=100, y=300, width=300, height=30)

        find_category = "SELECT nome_p FROM produtos"
        cursor.execute(find_category)
        result1 = cursor.fetchall()
        cat = []
        for i in range(len(result1)):
            if(result1[i][0] not in cat):
                cat.append(result1[i][0])


        self.nome.configure(values=cat)
        self.nome.configure(state="readonly")
        self.nome.configure(font="-family {Poppins} -size 8")
        self.nome.option_add("*TCombobox*Listbox.font", text_font)
        self.nome.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")
        self.nome.bind('<<ComboboxSelected>>', self.Preco)

        self.preco.configure(values=cat)
        self.preco.configure(state="disabled")
        self.preco.configure(font="-family {Poppins} -size 8")
        self.preco.option_add("*TCombobox*Listbox.font", text_font)
        self.preco.option_add("*TCombobox*Listbox.selectBackground", "#D2463E")
    



    def Preco(self, event):
        self.preco.configure(state="readonly")
        n = self.nome.get()
        a = cursor.execute(f"SELECT preco_v FROM produtos WHERE nome_p = ?", [n])
        l = []
        b = a.fetchall()
        for i in range(len(b)):
            l.append(b[i][0])
        self.preco.configure(values=l)
        self.preco.bind("<<ComboboxSelected>>", self.quant)

    def quant(self, event):
        self.e_quant.configure(state="normal")
        self.qty_label = Label(venda_j)
        self.qty_label.place(x= 100, y=430, width=100, height=26)
        self.qty_label.configure(font="-family {Poppins} -size 8")
        self.qty_label.configure(anchor="w")
        product_name = self.nome.get()
        find_qty = "SELECT quant_estoque FROM produtos WHERE nome_p = ?"
        cursor.execute(find_qty, [product_name])
        results = cursor.fetchone()
        self.qty_label.configure(text="Em estoque: {}".format(results[0]))
        self.qty_label.configure(background="white smoke")
        self.qty_label.configure(foreground="#333333")

        
    cart = carrinho()
    def add_to_cart(self):
            self.produtoScroll.configure(state="normal")
            strr = self.produtoScroll.get('1.0', END)
            if strr.find('Total')==-1:
                product_name = self.nome.get()
                if(product_name!=""):
                    product_qty = self.e_quant.get()
                    find_preco = "SELECT preco_v, quant_estoque FROM produtos WHERE nome_p = ?"
                    cursor.execute(find_preco, [product_name])
                    results = cursor.fetchall()
                    stock = results[0][1]
                    preco = results[0][0]
                    if product_qty.isdigit()==True:
                        if (stock-int(product_qty))>=0:
                            sp = preco*int(product_qty)
                            item_ = item(product_name, preco, int(product_qty))
                            self.cart.adicionarItem(item_)
                            self.produtoScroll.configure(state="normal")
                            bill_text = "{}\t\t\t{}\t\t\t   {}\n".format(product_name, product_qty, sp)
                            self.produtoScroll.insert('insert', bill_text)
                            self.produtoScroll.configure(state="disabled")
                            
                        else:
                            messagebox.showerror("ERRO!", "Acabou o estoque.", parent= venda_j)
                    else:
                        messagebox.showerror("ERRO!", "Quantidade inválida.", parent=venda_j)
                else:
                    messagebox.showerror("ERRO!", "Escolha o produto.", parent=venda_j)
            else:
                self.produtoScroll.delete('1.0', END)
                new_li = []
                li = strr.split("\n")
                for i in range(len(li)):
                    if len(li[i])!=0:
                        if li[i].find('Total')==-1:
                            new_li.append(li[i])
                        else:
                            break
                for j in range(len(new_li)-1):
                    self.produtoScroll.insert('insert', new_li[j])
                    self.produtoScroll.insert('insert','\n')
                product_name = self.nome.get()
                if(product_name!=""):
                    product_qty = self.e_quant.get()
                    find_preco = "SELECT preco_v, quant_estoque, codigo_p FROM produtos WHERE nome_p = ?"
                    cursor.execute(find_preco, [product_name])
                    results = cursor.fetchall()
                    stock = results[0][1]
                    preco = results[0][0]
                    if product_qty.isdigit()==True:
                        if (stock-int(product_qty))>=0:
                            sp = results[0][0]*int(product_qty)
                            item_ = item(product_name, preco, int(product_qty))
                            self.cart.adicionarItem(item_)
                            self.produtoScroll.configure(state="normal")
                            bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                            self.produtoScroll.insert('insert', bill_text)
                            self.produtoScroll.configure(state="disabled")
                        else:
                            messagebox.showerror("ERRO!", "Acabou o estoque.", parent=venda_j)
                    else:
                        messagebox.showerror("ERRO!", "Quantidade inválida.", parent=venda_j)
                else:
                    messagebox.showerror("ERRO!", "Escolha o produto", parent=venda_j)

    def remove_product(self):
            if(self.cart.vazio()!=True):
                self.produtoScroll.configure(state="normal")
                strr = self.produtoScroll.get('1.0', END)
                if strr.find('Total')==-1:
                    try:
                        self.cart.removerItem()
                    except IndexError:
                        messagebox.showerror("ERRO!", "Carrinho está vazio", parent=venda_j)
                    else:
                        self.produtoScroll.configure(state="normal")
                        get_all_bill = (self.produtoScroll.get('1.0', END).split("\n"))
                        new_string = get_all_bill[:len(get_all_bill)-3]
                        self.produtoScroll.delete('1.0', END)
                        for i in range(len(new_string)):
                            self.produtoScroll.insert('insert', new_string[i])
                            self.produtoScroll.insert('insert','\n')
                        
                        self.produtoScroll.configure(state="disabled")
                else:
                    try:
                        self.cart.removerItem()
                    except IndexError:
                        messagebox.showerror("ERRO!", "Carrinho está vazio", parent=venda_j)
                    else:
                        self.produtoScroll.delete('1.0', END)
                        new_li = []
                        li = strr.split("\n")
                        for i in range(len(li)):
                            if len(li[i])!=0:
                                if li[i].find('Total')==-1:
                                    new_li.append(li[i])
                                else:
                                    break
                        new_li.pop()
                        for j in range(len(new_li)-1):
                            self.produtoScroll.insert('insert', new_li[j])
                            self.produtoScroll.insert('insert','\n')
                        self.produtoScroll.configure(state="disabled")

            else:
                messagebox.showerror("ERRO!", "Adicione um produto.", parent=venda_j)
    
    def total_bill(self):
        if self.cart.vazio():
            messagebox.showerror("ERRO!", "Adicione um produto.", parent=venda_j)
        else:
            self.produtoScroll.configure(state="normal")
            strr = self.produtoScroll.get('1.0', END)
            if strr.find('Total')==-1:
                self.produtoScroll.configure(state="normal")
                divider = "\n\n\n"+("─"*45)
                self.produtoScroll.insert('insert', divider)
                total = "\nTotal\t\t\t\t\t\tR$. {}".format(self.cart.Total())
                self.produtoScroll.insert('insert', total)
                divider2 = "\n"+("─"*45)
                self.produtoScroll.insert('insert', divider2)
                self.produtoScroll.configure(state="disabled")
            else:
                return

    state = 1
    def confirmar(self):
        def Nome():
            nome = self.e_nomeCliente.get()
            if (len(nome) == 0):
                return True

            elif not len(nome)>= 2:
                return True
            temp = ''.join(nome.split(' '))

            for i in temp:
                if not i.isalpha():
                    return False
            else:
                return nome.strip(' ')

        def Quantidade():
            quant_estoque = self.e_quant.get()
            if (len(quant_estoque) == 0):
                return True
              
            elif not quant_estoque.isnumeric():
                return False
         
            else:
                return quant_estoque.strip(' ')

        def id_C(stringLength):
            lettersAndDigits = string.ascii_letters.upper() + string.digits
            strr=''.join(random.choice(lettersAndDigits) for i in range(stringLength-2))
            return ('BB'+strr)
        


        if self.state == 1:
            strr = self.produtoScroll.get('1.0', END)
            if(NomeCliente.get()=="" or NomeCliente.get()==" "):
                messagebox.showerror("ERRO!", "Campo nome vazio.", parent=venda_j)

            elif(self.cart.vazio()):
                messagebox.showerror("ERRO!", "Carrinho está vazio.", parent=venda_j)

            elif(Nome()== False ) or (Quantidade() == False):
                        messagebox.showwarning("ERROR","Valor(es) inválido(s)")
                        return False

            else: 
                if strr.find('Total')==-1:
                    self.total_bill()
                    self.confirmar()
                else:    
                    IdCli.set(id_C(8))
                    self.tx_idCli.insert(END,IdCli.get())
                    self.tx_idCli.configure(state='disabled')
                    Data.set(str(date.today()))
                    cursor = con.cursor()
                    insert = (
                        "INSERT INTO Venda(id_c, nome_c, produtosL, data_compra) VALUES(?,?,?,?)"
                    )
                    cursor.execute(insert, [IdCli.get(), NomeCliente.get(),self.produtoScroll.get('1.0', END), Data.get()])
                    con.commit() 
                   
                  
                    update_qty = "UPDATE produtos SET quant_estoque = quant_estoque - ? WHERE nome_p = ?"
                    cursor.execute(update_qty, [self.e_quant.get(), self.nome.get()])
                    con.commit() 
                    messagebox.showinfo("SUCESSO!", "Venda gerada", parent=venda_j)
                    self.e_nomeCliente.configure(state="disabled", disabledbackground="#ffffff", disabledforeground="#000000")
                    self.state = 0
        else:
            return
                    
    def clear_bill(self):
        self.e_nomeCliente.configure(state="normal")
        self.e_nomeCliente.delete(0, END)
        self.produtoScroll.configure(state="normal")
        self.produtoScroll.delete(1.0, END)
        self.produtoScroll.configure(state="disabled")
        self.cart.removerItens()
        self.state = 1

    def clear_selection(self):
        self.e_quant.delete(0, END)
        self.nome.configure(state="normal")
        self.preco.configure(state="normal")
        self.nome.delete(0, END)
        self.preco.delete(0, END)
        self.preco.configure(state="disabled")
        self.e_quant.configure(state="disabled")
        try:
            self.qty_label.configure(foreground="#ffffff")
        except AttributeError:
            pass

    

       
            
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)
    
        

# MENU PRINCIPAL
def nova_janela():
    janela2 = tk.Toplevel()
    janela2.title('Menu principal')
    options_frame = tk.Frame(janela2, bg = '#3fb5a3')

    cadasP_btn = tk.Button(options_frame, text='CADASTRO DE \nPRODUTO', font = ('Ivy 10 bold'), fg= 'white', bd = 0,bg = '#3fb5a3', command = lambda: indicate(cadasP_indicate,cadastroProduto_pag))
    cadasP_btn.place(x=10, y=50)

    cadasP_indicate = tk.Label(options_frame, text = '', bg = 'white')
    cadasP_indicate.place(x=3, y =50, width = 5, height = 40)

    cadasF_btn = tk.Button(options_frame, text='CADASTRO DE \nFUNCIONÁRIO', font = ('Ivy 10 bold'), fg= 'white', bd = 0,bg = '#3fb5a3', command = lambda: indicate(cadasF_indicate,cadastroFuncionario_pag))
    cadasF_btn.place( x=10, y=150)

    cadasF_indicate = tk.Label(options_frame, text = '', bg = 'white')
    cadasF_indicate.place(x=3, y =150, width = 5, height = 40)

    Entrada_btn = tk.Button(options_frame, text='ENTRADA DE \nPRODUTO', font = ('Ivy 10 bold'), fg= 'white', bd = 0,bg = '#3fb5a3', command = lambda: indicate(Entrada_indicate,entrada_pag))
    Entrada_btn.place( x=10, y=250)

    Entrada_indicate = tk.Label(options_frame, text = '', bg = 'white')
    Entrada_indicate.place(x=3, y =250, width = 5, height = 40)

    busca_btn = tk.Button(options_frame, text='BUSCA DE \nFUNCIONÁRIO', font = ('Ivy 10 bold '), fg= 'white', bd = 0,bg = '#3fb5a3', command = lambda: indicate(busca_indicate,buscaFuncionario_pag))
    busca_btn.place( x=10, y=350)

    busca_indicate = tk.Label(options_frame, text = '', bg = 'white')
    busca_indicate.place(x=3, y =350, width = 5, height = 40)

    venda_btn = tk.Button(options_frame, text='VENDA', font = ('Ivy 10 bold'), fg= 'white', bd = 0,bg = '#3fb5a3', command = lambda: indicate(venda_indicate,Venda_pg))
    venda_btn.place( x=10, y=450)

    venda_indicate = tk.Label(options_frame, text = '', bg = 'white')
    venda_indicate.place(x=3, y =450, width = 5, height = 40)



    
    
    
    global main_frame

    options_frame.pack(side = tk.LEFT)
    options_frame.pack_propagate(False)
    options_frame.configure(width = 150, height = 600)


    main_frame = tk.Frame(janela2, highlightbackground= 'black', highlightthickness=2,bg = 'white')
    main_frame.pack(side = tk.LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(height= 600, width=1000)

    l_LOGO = Label(main_frame, text='PROJETO MULTI UTILIDADES',anchor= NW, font='Tahoma 30', bg = 'white', fg= '#3fb5a3', borderwidth= 20)
    l_LOGO.grid( column=0 , row= 2, padx= 200, pady=100)
    l_LOGO.place(x = 240, y=200)
    l_mini = Label(main_frame, text='AA Tech',anchor= NW, font='Ubuntu 20', bg = 'white', fg= '#3fb5a3')
    l_mini.place(x = 440, y=300)

# LOGIN
l_nome = Label(frame_baixo, text='User',anchor= NW, font='Ivy 10', bg = co1, fg= co4)
l_nome.place(x = 10, y=20)
e_nome = Entry(frame_baixo, width=25, justify= 'left', font=("",15), highlightthickness=1, relief='solid')
e_nome.place(x=14,y=50)

l_pass = Label(frame_baixo, text='Senha',anchor= NW, font='Ivy 10', bg = co1, fg= co4)
l_pass.place(x = 10, y=95)
e_pass = Entry(frame_baixo, width=25, justify= 'left', show='*',font=("",15), highlightthickness=1, relief='solid')
e_pass.place(x=14,y=130)

l_botcad = Label(frame_baixo2, text='Não tem Login?',anchor= NW, font='Ivy 10', bg = co1, fg= co4, )
l_botcad.place(x = 100 , y=10)
b_botcad = Button(frame_baixo2, text='Criar Login', font='Ivy 10 bold', overrelief= RIDGE, bg = 'white', fg= co2, command = cadLogin)
b_botcad.place(x = 210, y=10)

b_confirmar = Button(frame_baixo,command= fazerLogin, text='Entrar',width=34, height=2, font='Ivy 10 bold', bg = co2, fg= co1, relief= RAISED, overrelief= RIDGE)
b_confirmar.place(x = 15, y=180)



janela.mainloop()

