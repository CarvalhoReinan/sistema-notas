from InquirerPy import prompt
from time import sleep
import os

CANCELAR = "Ok ! Operacão encerrada."

def tentar_novamente():
    perguntas = [
        {
            'type' : "list",
            'message' : "Deseja tentar novamente?  ↓ - ↑     ",
            'choices' : ["Sim", "Não"],
            'name' : 'escolha'
        }
    ]
    resultado = prompt(perguntas)
        
    if resultado['escolha'] == 'Não':
        return False
    elif resultado["escolha"]== "Sim":
        return True
     
def quantidade_aluno():
    while True:
        try:
            return int(input('Digite a quantidade de aluno: '))
        except ValueError:
            print('Erro, por favor digite um valor inteiro!')
            if not tentar_novamente():
                print('Ok! Operação Cancelada.')
                return None
                
def nome_aluno():
    while True:
        try:
            nome = input('Nome do aluno(a): ')
            if not all (part.isalpha() for part in nome.split()):
                raise ValueError('Digite o nome do aluno, sem números!')
            return nome
        except ValueError as ve:
            print(f'Erro: {ve}')
            if not tentar_novamente():
                print(CANCELAR)
                return None
                
def pegar_notas():
    while True:
        try:
            notas = []
            for i in range(1, 4):
                nota = float(input(f'Nota {i} UND: '))
                if nota < 0 or nota > 10:
                    raise ValueError('Notas devem estar entre 0 e 10.')
                notas.append(nota)
            return notas
        except ValueError:
            print('Digite apenas números de 1 a 10!')
            if not tentar_novamente():
                print(CANCELAR)
                return None

def calcular_media(a, b, c):
    return round((a + b + c) / 3, 2)

def imprimir_alunos(aprovados, reprovados, recuperar):
    print('\nLista de aluno aprovados:')
    for aluno in aprovados:
        print(f'{aluno[0].capitalize()} - Média: {aluno[1]:.2f}')
    print('\nLista de alunos Reprovados:')
    for aluno in reprovados:
        print(f'{aluno[0].capitalize()} - Média: {aluno[1]:.2f}')
    print('\nLista de alunos em Recuperação:')
    for aluno in recuperar:
        print(f'{aluno[0].capitalize()} - Média: {aluno[1]:.2f}')
            
def planilha_nota():
    qtd_alunos = quantidade_aluno()
    if qtd_alunos is None:
        return
    
    total_aprovado = 0
    total_reprovado = 0
    total_recuperacao= 0
    aprovados = []
    reprovados = []
    recuperar = []

    for _ in range(qtd_alunos):
        aluno = nome_aluno()    
        if aluno is None:
            return

        notas = pegar_notas()
        if notas is None:
            return

        resultado = calcular_media(*notas)

        if resultado >= 5:
            print(f'{aluno.capitalize()}, passou! Média: {resultado:.2f}')
            total_aprovado += 1
            aprovados.append((aluno, resultado))
        elif resultado <= 4.9 and resultado >= 3:
            print(f'{aluno.capitalize()}, recuperação Média: {resultado:.2f}')
            total_recuperacao += 1
            recuperar.append((aluno, resultado))
        else:
            print(f'{aluno.capitalize()}, recuperação! Média: {resultado:.2f}')
            total_recuperacao += 1
            reprovados.append((aluno, resultado))
            
    total = qtd_alunos
    print("\nAguarde um momento..")
    sleep (3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('='*20)
    print(f'\nSEGUE A PLANILHA ABAIXO:')
    print('='*20)
    print (f'Total alunos: {total}')
    print(f'Quantidade de alunos aprovados: {total_aprovado}')
    print(f'Quantidade reprovado: {total_reprovado}')
    print(f'Quantidade recuperação: {total_recuperacao}')
    imprimir_alunos(aprovados, reprovados, recuperar)

    
if __name__ == "__main__":

    print('Bem-vindo ao sistema de notas!')
    planilha_nota()
    print('Obrigado por usar o sistema!')

