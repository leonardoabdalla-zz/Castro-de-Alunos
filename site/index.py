print('Cadastro de Alunos')
cadastro = input('Deseja cadastrar um aluno?(S/N)')
cadastro = cadastro.upper()
cadastro = cadastro.strip()
listaAlunos = []
while(cadastro == 'S'):
    aluno = []
    nome = input('Qual nome do aluno? ')
    nome = nome.capitalize()
    nome = nome.strip()
    aluno.append(nome)
    matricula = int(input('qual seu código de matricula? '))
    aluno.append(matricula)
    nota1 = float(input('Nota do primeiro bimestre: '))
    nota2 = float(input('Nota do segundo bimestre: '))
    nota3 = float(input('Nota do terceiro bimestre: '))
    nota4 = float(input('Nota do quarto bimestre: '))
    mediaNotas = (nota1 + nota2 + nota3 + nota4) / 4
    aluno.append(mediaNotas)
    if (mediaNotas >= 7.0):
        aluno.append('Aprovado')
    elif (mediaNotas < 7 and mediaNotas > 3):
        aluno.append('Recuperação')
    else:
        aluno.append('Reprovado')
    print('Aluno = {}\nMatrícula = {} '.format(aluno[0], aluno[1]))
    print(' Nota do primeiro bimestre = {} \n Nota do segundo bimestre = {} \n Nota do terceiro bimestre = {} \n '
          'Nota do quarto bimestre = {}'.format(nota1, nota2, nota3, nota4))
    print(' Sua média final foi ', mediaNotas)
    print('status: ', aluno[3])
    listaAlunos.append(aluno)
    cadastro = input('Deseja cadastrar um novo aluno?(S/N) ').upper().capitalize()
print(listaAlunos)









