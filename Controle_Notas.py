import time
import massa_teste
import pickle

def menu_principal():
    print("\n"+66*"=")
    print("Controle de Notas".center(66))
    print(66*"="+"\n")
    print("  1 - Listar alunos")
    print("  2 - Matricular aluno")
    print("  3 - Buscar Aluno")  # .......................................<< New change in console'text interface (Adding "3 - Buscar Aluno" option)
    print("  0 - Sair do Aplicativo\n")
    return input("  Escolha uma opção: ")


def menu_listagem():
    print("\n"+66*"=")
    print("Mostra lista de alunos".center(66))
    print(66*"="+"\n")
    print("  1 - Ordenada pelo código")
    print("  2 - Ordenada pelo nome")
    print("  3 - Ordenada pelo idade")  # .......................................<< New change in console'text interface (Adding "3 - Ordenada pelo idade" option)
    print("  0 - Voltar ao menu principal\n")
    return input("  Escolha uma opção: ")


def media(ap1, ap2):
    a, b = ap1, ap2
    if ap1 > 10.5:
        a = 0
    if ap2 > 10:
        b = 0
    return (2 * a + 3 * b) // 5

def mostre_lista_de_alunos(la):
    print(66*"-")
    print("Código {:30s} Nascimento   AP1   AP2 Média".format("Nome"))
    print("------", 30*"-", 10*'-', 5*"-", 5*"-", 5*"-")
    for alu in la:
        print("{:06d} {:30s}".format(alu[0],alu[1]), end=' ')
        print("{:02d}/{:02d}/{:d}".format(alu[2][2],alu[2][1],alu[2][0]), end=' ')
        if alu[3] > 10.5:
            print("     ", end=' ')
        else:
            print("{:5.1f}".format(alu[3]), end=' ')
        if alu[4] > 10.5:
            print(5*" ", end=' ')
        else:
            print("{:5.1f}".format(alu[4]), end=' ')
        print("{:5.1f}".format(media(alu[3],alu[4])))

def busca_aluno(lis):
    nome = input("  Digite as primeiras letras do nome: ")
    print("  ----------------------------------------------")
    while True:
        for alu in sorted(lis, key = lambda x : x[1]):
            if alu[1].find(nome) == 0:
                print("  {:30s}  Código: {:06d}".format(alu[1], alu[0]))
        print("  ----------------------------------------------")  # .......................................<< New change in console'text interface
        c = input("  Complemente o nome ou <ENTER> para sair: "+nome)
        print("  ----------------------------------------------")  # .......................................<< New change in console'text interface
        if c == "":
            break
        nome = nome + c

def e_bissexto(ano):
    return ano%4 == 0 and (ano%100 != 0 or ano%400 == 0)

def e_valida(dia, mes,ano):
    ndm = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if e_bissexto(ano):
        ndm[2] = 29
    if ano < 1900:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > ndm[mes]:
        return False
    return True

def matricula(lis, cod):
    nome = input("  Nome: ")
    dia, mes, ano = map(int, input("  Data de nascimento (dd/mm/aaaa): ").split(sep='/'))
    lis.append([cod, nome, [ano, mes, dia], 11.0, 11.0])

def principal():
    #lis_alu = massa_teste.gere_lista_de_alunos(20)
    alterado = False
    file = open("alunos.gue", "rb")
    ult_cod = pickle.load(file)
    lis_alu = pickle.load(file)
    file.close()
    #ult_cod = 20
    while True:
        op = menu_principal()
        if op == '0':
            if alterado:
                salva = input("  Arquivo alterado. Deseja salvá-lo? (S/N)")
                while salva != 'S' and salva != 's' and salva != 'N' and salva != 'n':
                    salva = input("  Responda S ou N")
                if salva == 'S' or salva == 's':
                    file = open("alunos.gue", "wb")
                    pickle.dump(ult_cod, file)
                    pickle.dump(lis_alu, file)
                    file.close()
                    print("  Arquivo salvo")
            break
        elif op == '1':
            while True:
                op2 = menu_listagem()
                if op2 == '0':
                    break
                elif op2 == '1':
                    print(66*"-")  # .........................................................<< New change in console'text interface
                    print("{:s}".format("LISTA DE ALUNOS ORDENADOS PELO CÓDIGO".center(66)))
                    mostre_lista_de_alunos(lis_alu)
                elif op2 == '2':
                    print(66*"-")  # .........................................................<< New change in console'text interface
                    print("{:s}".format("LISTA DE ALUNOS ORDENADOS PELO NOME".center(66)))
                    mostre_lista_de_alunos(sorted(lis_alu, key=lambda nome : nome[1]))
                elif op2 == '3': # .........................................................<< New change in console'text interface (Adding "3 - Ordenada pelo idade" option)
                    print(66*"-")
                    print("{:s}".format("LISTA DE ALUNOS ORDENADOS PELA IDADE".center(66)))
                else:
                    print("\n  * ENTRADA INVÁLIDA *\n")  # .........<< New change in console'text interface
        elif op == '2':
            print(66*"-")  # .......................................<< New change in console'text interface
            print("{:s}".format("MATRICULAR ALUNO".center(66)))
            print(66*"-")  # .......................................<< New change in console'text interface
            matricula(lis_alu, ult_cod + 1)
            ult_cod += 1
            alterado = True
        elif op == '3':
            print(66*"-") #  ........................................<< New change in console'text interface
            print("{:s}".format("BUSCAR ALUNO PELO NOME".center(66)))
            print(66*"-") #   .......................................<< New change in console'text interface
            busca_aluno(lis_alu)
        else:
            print("\n  * ENTRADA INVÁLIDA *\n") #  ..................<< New change in console'text interface

principal()
