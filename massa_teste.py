import random


def gere_nome():
    nomes = ('Aline', 'Ana', 'Beatriz', 'Bernardo', 'Bruno', 'Camila', 'Carlos', 'Cecília',
             'Davi', 'Eduardo', 'Felipe', 'Francisco', 'Gabriel', 'Gérson', 'Heitor', 'Henrique',
             'Ingrid', 'Isabela', 'Júlia', 'Larissa', 'Laura', 'Leonardo', 'Lorena', 'Marcelo',
             'Márcia', 'Marcos', 'Mariana', 'Milena', 'Patrícia', 'Pedro', 'Priscila', 'Renato',
             'Ricardo', 'Rodrigo', 'Ronaldo', 'Samuel', 'Sérgio', 'Sofia', 'Tiago', 'Vinícius')
    sobrenomes = ('Abreu', 'Albuquerque', 'Almeida', 'Alencar', 'Alves', 'Amaral', 'Amorim',
                  'Andrade', 'Antunes', 'Arantes', 'Araújo', 'Arruda', 'Azevedo', 'Barros',
                  'Bastos', 'Batista', 'Bezerra', 'Brandão', 'Brito', 'Cabral', 'Campos',
                  'Cardoso', 'Carneiro', 'Carvalho', 'Castro', 'Cavalcante', 'Chagas', 'Chaves',
                  'Correia', 'Costa', 'Cruz', 'Dantas', 'Diniz', 'Duarte', 'Esteves', 'Fagundes',
                  'Fernandes', 'Ferraz', 'Ferreira', 'Figueiredo', 'Fonseca', 'Franco', 'Freire',
                  'Freitas', 'Furtado', 'Gomes', 'Gonçalves', 'Guedes', 'Guerra', 'Guimarães',
                  'Liberato', 'Marinho', 'Marques', 'Martins', 'Medeiros', 'Melo', 'Menezes',
                  'Monteiro', 'Montenegro', 'Moraes', 'Moreira', 'Moura', 'Nogueira', 'Noronha',
                  'Novaes', 'Oliveira', 'Pereira', 'Pinto', 'Resende', 'Ribeiro', 'Rios',
                  'Sampaio', 'Santana', 'Santos', 'Torres', 'Trindade', 'Vasconcelos', 'Vargas')

    nome = random.choice(nomes) + " "
    ps = random.choice(sobrenomes)
    ss = random.choice(sobrenomes)
    while ps == ss:
        ss = random.choice(sobrenomes)
    return nome + ps + " " + ss

def gere_data():
    return [random.randint(1990, 2000), random.randint(1, 12),
            random.randint(1, 28)]

def gere_aluno(cod):
    ap1 = random.randint(50, 100) / 10
    ap2 = random.randint(50, 100) / 10
    return [cod, gere_nome(), gere_data(), ap1, ap2]


def gere_lista_de_alunos(nal):
    la = []
    for i in range(nal):
        la.append(gere_aluno(i+1))
    return la
