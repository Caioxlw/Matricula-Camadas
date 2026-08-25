from persistence.inicializadorbd import criar_tabelas, semear
from persistence.consultas import *
from business import *

def menu():
    criar_tabelas()
    semear()
    while True:
        print("\n1) Matricular  2) Listar  3) Cancelar expiradas  4) Sair")
        opcao = input("> ").strip()
        if opcao == "1":
            matricular(input("id do aluno, codigo da turma: "))
        elif opcao == "2":
            listarTurmasAluno(int(input("id do aluno: ")))
        elif opcao == "3":
            cancelar_expiradas()
        elif opcao == "4":
            break
        else:
            print("Opcao invalida")


if __name__ == "__main__":
    menu()