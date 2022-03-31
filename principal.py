from automatico import envia_email
import time


lista_email = ['contateste314159@gmail.com', 
               'mabuddaj@gmail.com', 
               'engenheiroloterico@gmail.com',
               'sara.diene.abreu@gmail.com',
               'gabo.otto303@gmail.com']

while True:

    hora = time.localtime().tm_hour
    minuto = time.localtime().tm_min
    
    if hora == 10 and minuto == 46:
         for email in lista_email:
              envia_email(email)
    time.sleep(60)

'''
    A ideia do projeto integrador é criar um sistema de controle de estoque:
    O sistema deve permitir inserir produtos ou itens no estoque: 
    Todo produto pertence a uma categoria. 
    
    As informações
    de produto necessárias são nome do produto, valor, quantidade e 
    Unidade de Medida: KG, Litro, Unidade, também é necessário 
    inserir uma data de entrada desse item no estoque.
    
    O sistema deve permitir visualizar os itens do estoque.
    
    O sistema deve permitir retirar itens do estoque e atualizar o 
    estoque de acordo com a retirada. A retirada não pode ser maior
    que a quantidade em estoque.
    

    1- Separar as funcionalidades do sistema. (descreva as ações que
    o sistema faz).
    
    2- Atividade Prototipar as telas do sistema. (Desenhar como elas
    seriam)


'''





















