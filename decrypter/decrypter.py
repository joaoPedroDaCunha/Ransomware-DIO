import os
import pyaes

## abrir o arquivo criptografado

file_name = 'test.txt.ransomwaret'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomware'
aes = pyaes.AesModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar um novo arquivo descriptogarfado 

new_file = 'test.txt'
new_file = open(f'{new_file}',)
new_file.write(decrypt_data)
new_file.close()