fundamental = {
    'calculo': [],
    'ciências': [],
    'literatura': []
}

medio = {
    'matematica': [],
    'fisica': [],
    'quimica': [],
    'biologia': []
}

programacao = {
    'programação': []
}

infantil = {
    'Historia para crianças' : []
}

def livros(categoria):
    if categoria == 'literatura':
        return [
            "O Pequeno Príncipe", 
            "Meu Pé de Laranja Lima",
            "A Bolsa Amarela", 
            "A Menina que Roubava Livros", 
            "O Diário de Anne Frank", 
            "Alice no País das Maravilhas", 
            "Dom Quixote (adaptação)", 
            "As Crônicas de Nárnia", 
            "Viagem ao Centro da Terra", 
            "O Mistério do Cinco Estrelas", 
            "A Droga da Obediência", 
            "Harry Potter e a Pedra Filosofal", 
            "Os Contos de Grimm", 
            "O Gênio do Crime", 
            "Pinóquio", 
            "O Menino Maluquinho"
        ]
    elif categoria == 'calculo':
        return [
            "O Homem que Calculava",
            "Aventuras Matemáticas", 
            "Desafio Matemático", 
            "Problemas de Lógica Matemática", 
            "Matemática Divertida e Curiosa", 
            "Desafios Matemáticos", 
            "O Desafio do X", 
            "Brincando com a Matemática", 
            "Matemática Fácil e Divertida", 
            "Matemática Elementar – Vol. 1", 
            "Cálculos e Estimativas", 
            "Matemática – Coletânea de Exercícios", 
            "Jogos Matemáticos", 
            "Cálculo Rápido"
        ]
    elif categoria == 'ciências':
        return [
            "O Livro da Ciência para Crianças",
            "Tudo Sobre o Corpo Humano",
            "O Sistema Solar: O que há lá fora?",
            "O Pequeno Cientista: Experimentos Divertidos",
            "A Máquina Fantástica do Corpo Humano",
            "A Terra em que Vivemos",
            "O Universo: Estrelas, Planetas e Galáxias",
            "De onde vem a eletricidade?",
            "O Mundo dos Insetos",
            "Animais Fantásticos: Descubra a Natureza",
            "O que é DNA?",
            "Inventores e suas Grandes Ideias",
            "Como Surgiram as Coisas?",
            "Astronomia para Crianças",
            "Robôs: Como Funcionam?",
            "Pequenos Cientistas: A Natureza e os Animais",
            "Ciclo da Água: Uma Viagem em Cada Gota",
            "O Mundo dos Dinossauros",
            "Energia: Como Ela se Transforma?",
            "Física Divertida para Crianças"
        ]
    elif categoria == 'matematica':
        return [
            "Matemática: Ciência e Aplicações",
            "Geometria Plana e Espacial",
            "Álgebra Linear para Estudantes",
            "Cálculo Diferencial e Integral",
            "Trigonometria Essencial",
            "Estatística e Probabilidade",
            "Física-Matemática: Fundamentos e Aplicações",
            "Matemática Discreta"
        ]
    elif categoria == 'fisica':
        return [
            "Física Clássica para Estudantes",
            "Mecânica Clássica",
            "Eletromagnetismo: Fundamentos e Aplicações",
            "Ondas e Termodinâmica",
            "Óptica e Física Moderna",
            "Física Quântica e Relatividade",
            "Física Experimental para Estudantes",
            "Cinemática e Dinâmica"
        ]
    elif categoria == 'quimica':
        return [
            "Química Geral: Princípios e Aplicações",
            "Química Inorgânica",
            "Química Orgânica",
            "Termoquímica: Calor e Energia",
            "Estequiometria: Teoria e Exercícios",
            "Eletroquímica: Teoria e Prática",
            "Química Ambiental",
            "Laboratório de Química"
        ]
    elif categoria == 'biologia':
        return [
            "Biologia: Estrutura e Função",
            "Genética e Evolução",
            "Fisiologia Humana",
            "Ecologia e Meio Ambiente",
            "Botânica e Zoologia",
            "Biologia Celular e Molecular",
            "Microbiologia e Parasitologia",
            "Biotecnologia: Princípios e Aplicações"
        ]
    
    elif categoria == 'programação':
        return [
    "Python Crash Course por Eric Matthes",
    "Automate the Boring Stuff with Python por Al Sweigart",
    "Clean Code: A Handbook of Agile Software Craftsmanship por Robert C. Martin",
    "Introduction to the Theory of Computation por Michael Sipser",
    "The Pragmatic Programmer: Your Journey to Mastery por Andrew Hunt e David Thomas",
    "Design Patterns: Elements of Reusable Object-Oriented Software por Erich Gamma, Richard Helm, Ralph Johnson e John Vlissides",
    "JavaScript: The Good Parts por Douglas Crockford",
    "Eloquent JavaScript: A Modern Introduction to Programming por Marijn Haverbeke",
    "You Don't Know JS (série) por Kyle Simpson",
    "Effective Java por Joshua Bloch",
    "The Art of Computer Programming por Donald E. Knuth",
    "Programming Pearls por Jon Bentley",
    "Code: The Hidden Language of Computer Hardware and Software por Charles Petzold",
    "Structure and Interpretation of Computer Programs por Harold Abelson e Gerald Jay Sussman",
    "The Mythical Man-Month: Essays on Software Engineering por Frederick P. Brooks Jr."]


    elif categoria in ('histórias infantís'):
        return[
    "O Pequeno Príncipe ",
    "A Bolsa Amarela",
    "O Menino Maluquinho",
    "A Turma da Mônica",
    "Chapeuzinho Vermelho",
    "A Bela Adormecida",
    "Os Três Porquinhos",
    "João e o Pé de Feijão",
    "A Cinderella",
    "A Branca de Neve",
    "A Pequena Sereia",
    "A Rapunzel",
    "O Patinho Feio",
    "A Galinha dos Ovos de Ouro",
    "Os Sete Anões"
        ]


    else:
        print("Opção inválida")
        return []

while True:
    ver_livros = input("Deseja ver uma lista dos livros disponíveis para qual tipo de ensino (Fundamental, Médio, programação, histórias infantís): ").strip().lower()
    if ver_livros == 'fundamental':
        tipo_livros = input('Temos livros de literatura, cálculo e ciências para os alunos iniciantes, digite qual você deseja ver: ').lower()
        lista_livros = livros(tipo_livros)

        if lista_livros:
            for i, c in enumerate(lista_livros):
                print(f'{i+1} = {c}')

            escolha_livros = input('Com base na tabela selecione os itens que você deseja baixar (separados por vírgula): ')
            num_escolhidos = [int(num.strip()) for num in escolha_livros.split(',')]

            for c in num_escolhidos:
                if 1 <= c <= len(lista_livros):
                    livros_escolhido = lista_livros[c-1]

                    if tipo_livros in ('calculo', 'cálculo'):
                        fundamental["calculo"].append(livros_escolhido)
                    elif tipo_livros == 'literatura':
                        fundamental["literatura"].append(livros_escolhido)
                    elif tipo_livros in ('ciências', 'ciencias'):
                        fundamental["ciências"].append(livros_escolhido)
                else:
                    print(f'Número {c} inválido')

    elif ver_livros in ("médio","medio"):
        tipo_livros = input('Temos livros de Matemática, Física, Química e Biologia voltados para alunos do ensino médio, digite qual você deseja ver: ').lower()
        lista_livros = livros(tipo_livros)

        if lista_livros:
            for i, c in enumerate(lista_livros):
                print(f'{i+1} = {c}')

            escolha_livros = input('Com base na tabela selecione os itens que você deseja baixar (separados por vírgula): ')
            num_escolhidos = [int(num.strip()) for num in escolha_livros.split(',')]

            for c in num_escolhidos:
                if 1 <= c <= len(lista_livros):
                    livros_escolhido = lista_livros[c-1]

                    if tipo_livros == 'fisica':
                        medio["fisica"].append(livros_escolhido)
                    elif tipo_livros in ('matematica', 'matemática'):
                        medio['matematica'].append(livros_escolhido)
                    elif tipo_livros == 'quimica':
                        medio['quimica'].append(livros_escolhido)
                    elif tipo_livros == 'biologia':
                        medio["biologia"].append(livros_escolhido)
                else:
                    print(f'Número {c} inválido')
    
    elif ver_livros in ('programaçao','programação'):
        print('Temos livros diversos sobre programação para voçê iniciar sua jornada dev')
        lista_livros = livros('programação')

        if lista_livros:
            for i,c in enumerate(lista_livros):
                print(f'{i+1} = {c}')

            escolha_livros = input('Com base na tabela selecione os itens que você deseja baixar (separados por vírgula): ')
            num_escolhidos = [int(num.strip())for num in escolha_livros.split(',')]

            for c in num_escolhidos:
                if 1 <= c <= len(lista_livros):
                    livros_escolhido = lista_livros[c-1]
                    programacao["programação"].append(lista_livros)

                else:
                    print(f'Número {c} inválido')

    elif ver_livros in ('historias infantis', 'histórias infantís' ):
        print('Aqui está uma lista das recomendações de histórias infantís.')
        lista_livros = livros('histórias infantís')

        if lista_livros:
            for i,c in enumerate(lista_livros):
                print(f'{i+1} = {c}')

            escolha_livros = input('Com base na tabela selecione os itens que você deseja baixar (separados por vírgula): ')
            num_escolhidos = [int(num.strip())for num in escolha_livros.split(',')]

            for c in num_escolhidos:
                if 1 <= c <= len(lista_livros):
                    livros_escolhido = lista_livros[c-1]
                    infantil['Historia para crianças'].append(lista_livros)

                else:
                    print(f'Número {c} inválido')

    else:
        print("Opção inválida")

    adicionar = input('Deseja adicionar mais itens? [S/N]: ').upper()
    if adicionar != 'S':
        break




if any(len(lista) > 0 for lista in fundamental.values()):
 fundamental_lista = [livro for lista_livro in fundamental.values() if len(lista_livro)>0 for livro in lista_livro]
 print("Listas dos livros do fundamental escolhidos por voçê: ")
 for i, c in enumerate(fundamental_lista):
    print(f"{i+1} = {c}")


if any(len(lista) > 0 for lista in medio.values()):
    medio_lista = [livro for lista_livro in medio.values() if len(lista_livro)>0 for livro in lista_livro]
    print("Lista dos livros do ensino médio escolhidos por voçê: ")
    for i, c in enumerate(medio_lista):
        print(f"{i+1} = {c}")


if any(len(lista) > 0 for lista in programacao.values()):
    print("Lista dos livros de programação escolhidos por voçê: ")
    for i, c in programacao.values():
        print(f"{i+1} = {c}")


if any(len(lista) > 0 for lista in infantil.values()):
    print("Lista dos livros de história escolhidos por voçê: ")
    for i, c in infantil.values():
        print(f"{i+1} = {c}")
    

    

    