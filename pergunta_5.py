texto = "Preciso muito de um estágio!!"
texto_invertido = ""
contador = 0

# contando a quantidade de caracteres
for letra in texto:
  contador += 1

# percorrendo a string do fim para o começo
while contador > 0:
  # print(texto[contador-1:contador])
  texto_invertido += texto[contador-1:contador]
  contador -= 1

print(texto_invertido) # !!oigátse mu ed otium osicerP