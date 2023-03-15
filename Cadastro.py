import re

lista = []

class Usuario():
    def __init__(self, nome, senha, email, identity):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.identity = identity
        self.usuario = None

    def cadastrar(self):
        print("Insira as informações para cadastro...")

        nome = str(input("Digite o nome: "))

        senha = str(input("Digite a senha: "))

        while not (re.search('[a-z]', senha) and re.search('[A-Z]', senha) and re.search('[0-9]', senha)):
            print("A senha deve conter pelo menos uma letra maiúscula e um número.")
            senha = input("Digite a senha: ")

        email = str(input("Digite o email: "))

        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("O email digitado não é válido.")
            email = input("Digite o email: ")

        identity = str(input("Digite o identidade. Ex(1,2,3...): "))

        self.usuario = Usuario(nome, senha, email, identity)

        lista.append(self.usuario)


        def salvar_usuario(lista):
        #abre o arquivo
            with open("usuarios.txt", 'a') as arquivo:

                for usuario in lista:
                    arquivo.write(f"{usuario.nome},{usuario.senha},{usuario.email},{usuario.identity}\n")

        print("Usuário salvo com sucesso...")


        salvar_usuario(lista)
        print("Cadastrado com sucesso...")


    def listar(self):

        print("Listando usuários...")

        for i in range(len(lista)):

            print(f"Nome: {lista[i].nome}")
            print(f"Senha: {lista[i].senha}")
            print(f"Email: {lista[i].email}")
            print(f"Identidade: {lista[i].identity}")

    def alterar(self, item):

        print("Alterando usuário...")

        for usuario in lista:
            if usuario.identity == item:
                lista.remove(usuario)
                print(f"O {item} foi excluido da lista...")
                break

        else:
            print(f"Usuario não encontrado...")





user = Usuario('','','','')




print("Bem vindo!")

dec = int(input("""O que deseja fazer?
1 - Cadastrar
2 - Alterar/Excluir
3 - Listar
"""))

if dec == 1:
    user.cadastrar()


elif dec == 2:
    item = str(input("Digite a identidade do usuário que deseja alterar/excluir: "))
    user.alterar(item)

elif dec == 3:
    user.listar()

else:
    print("Opção inválida...")


while True:
    escolha = input("Deseja continuar? [S/N]")
    if escolha.lower() == 's':
        dec = int(input("""O que deseja fazer?
        1 - Cadastrar
        2 - Alterar/Excluir
        3 - Listar
        """))

        if dec == 1:
            user.cadastrar()

        elif dec == 2:
            item = str(input("Digite a identidade do usuário que deseja alterar/excluir: "))
            user.alterar(item)

        elif dec == 3:
            user.listar()

        else:
            print("Opção inválida...")

    elif escolha.lower() == 'n':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Digite 'S' para continuar ou 'N' para encerrar o programa.") 
