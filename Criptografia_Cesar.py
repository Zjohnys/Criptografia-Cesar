#Criptografia de Cesar

MODE_ENCRYPT = 1
MODE_DECRYPT = 0


#Funcao 
def cesar(data, key, mode):
#Declarando o alfaberto
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
#Fazendo um loop
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
#Operacao para achar a posicao do caractere de acordo com a chave
            new_index = index + key if mode == MODE_ENCRYPT else index - key
            new_index = new_index % len(alphabet)
            new_data += alphabet[new_index:new_index+1]
#fim do loop       
    return new_data
#progama
Palavra = input('Digite a mensagem a ser Encriptada e Decriptada: ')
key = int(input('Entre com o valor da chave (deslocamento): '))
ciphered = cesar(Palavra, key, MODE_ENCRYPT)
print('Encriptada:', ciphered)
plain = cesar(ciphered, key, MODE_DECRYPT)
print('Decriptada:', plain)

print('Obrigado por usar nosso programa.')