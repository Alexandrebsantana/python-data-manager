import csv

def ler_csv():
    with open("produtos.csv") as arquivo:
        dados = csv.DictReader(arquivo)

        produtos = list(dados)

        for produto  in produtos:
            produto["preco"] = int(produto["preco"])
            produto["quantidade"] = int(produto["quantidade"])
        return produtos
      
def listar_produtos():
    produtos = ler_csv()

    for produto in produtos:
        print(f"Nome: {produto['nome']}")
        print(f"categoria: {produto['categoria']}")
        print(f"preço: {produto['preco']}")
        print(f"quantidade: {produto['quantidade']}")
        print()

def buscar_produto(nome):
    produtos = ler_csv()

    encontrado = False
    for produto in produtos:
        if produto["nome"] == nome:
            encontrado = True

            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"preço: {produto['preco']}")
            print(f"quantidade: {produto['quantidade']}")
            return
    if not encontrado:
        print("Produto não encontrado")
        return
    
def adicionar_produto(nome, categoria, preco, quantidade):

    produtos = ler_csv()

    for produto in produtos:
        if produto["nome"] == nome:
            print("produto ja existe")
            return
    
    novo_produto = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(novo_produto)

    salvar_produtos(produtos)

    print("Produto adicionado com sucesso")

def salvar_produtos(produtos):

    with open("produtos.csv", "w", newline="") as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow([
            "nome",
            "categoria",
            "preco",
            "quantidade"
        ])

        for produto in produtos:

            writer.writerow([
                produto["nome"],
                produto["categoria"],
                produto["preco"],
                produto["quantidade"]
            ])

def atualizar_quantidade(nome, nova_quantidade):
    produtos = ler_csv()

    encontrado = False
    for produto in produtos:
        if produto["nome"] == nome:
            produto["quantidade"] = nova_quantidade
            encontrado = True

    if not encontrado:
        print("produto não encontrado")
        return
    salvar_produtos(produtos)
    print("quantidade atualizada com suceesso")

def remover_produto(nome):
    produtos = ler_csv()

    encontrado = False

    for produto in produtos:
        if produto["nome"] == nome:
            encontrado = True

    if not encontrado:
        print("produto não encontrado")
        return

    produtos_filtrados = [
        produto
        for produto in produtos
        if produto["nome"] != nome
    ]
    
    salvar_produtos(produtos_filtrados)
    print("produto removido com sucesso")        

def valor_total_estoque(produtos):
    return sum(
        produto["preco"] * produto["quantidade"]
        for produto in produtos
    )

def relatorio():
    produtos = ler_csv()

    total = valor_total_estoque(produtos)

    print(f"valor total do estoque: {total}")


def menu():

    while True:

        print("\n === SISTEMA DE ESTOQUE ===")
        print("1 - Listar produtos")
        print("2 - Buscar produto")
        print("3 - Adicionar produto")
        print("4 - Atualizar quantidade")
        print("5 - Remover produto")
        print("6 - Relatorio")
        print("0 - sair")

        opcao = input("escolha uma opção: ")

        if opcao == "0":
          print("encerrando sistema...")
          break

        elif opcao == "1":
           listar_produtos()
           
        elif opcao == "2":
            nome = input("digite o nome do produto: ")
            buscar_produto(nome)
            
        elif opcao == "3":
            nome = input("Nome:")
            categoria = input("categoria: ")
            preco = int(input("preço: "))
            quantidade = int(input("quantidade: "))
           
            adicionar_produto(     
                nome, 
                categoria,
                preco,
                quantidade
            )
            
        elif opcao == "4":
            nome = input("Nome do produto:")
            quantidade = int(input("Nova quantidade: "))
            
            atualizar_quantidade(
                nome, 
                quantidade
            )
        
        elif opcao == "5":
           nome = input("Nome do produto : ")
           
           remover_produto(nome)
            
        elif opcao =="6":
            relatorio()
       
        else:
            print("Opção inválida")

menu()