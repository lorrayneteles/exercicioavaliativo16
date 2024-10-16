#Preço com desconto

preco_produto = int(input("Digite o preço do produto:"))

valor_desconto = int(input("Digite o valor do desconto:"))

desconto = valor_desconto * 0.01 * preco_produto

preco_final = preco_produto - desconto

print(f"O valor do produto com o desconto é de:",preco_final)