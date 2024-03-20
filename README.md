## Estágio Ribeirão Preto - 2024

#### 1) Observe o trecho de código abaixo:
````
int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça {
  K = K + 1;
  SOMA = SOMA + K;
}

imprimir(SOMA);

````

Ao final do processamento, qual será o valor da variável SOMA?

````
A soma dos números de 1 a 13 é uma progressão aritmética, e podemos calcular dessa forma:

soma = n*(1 + n)/2
soma = 13 *(1 + 13)/2 
soma = 91

````

### Usando código para resolver o problema:
[Pergunta 1: ](https://github.com/MurilodioPy/desafio/blob/main/pergunta_1.py)

````
indice = 13
soma = 0
k = 0

while k < indice:
  k += 1
  soma += k

print(soma) # 91

soma_2 = indice * (1 + indice)/2

print(soma_2) # 91

````
#### 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

[Pergunta 2: ](https://github.com/MurilodioPy/desafio/blob/main/pergunta_2.py)

````
def verifica_fibonacci(n):
  x = 0
  y = 1
  for i in range(n + 1):
    z = x + y
    if z == n:
      return "Número pertence a sequência de Fibonacci!"
    elif i == n:
      return "Número NÃO pertence a sequência de Fibonacci!"
    y = x
    x = z

print(verifica_fibonacci(4181)) # Número pertence a sequência de Fibonacci!

````

#### 3) Descubra a lógica e complete o próximo elemento:

````
a) 1, 3, 5, 7, 9, 11, 13 sendo n iniciado em 1 lógica (n + 2)

b) 2, 4, 8, 16, 32, 64, 128, 256 lógica (n * 2)

c) 0, 1, 4, 9, 16, 25, 36, 49, 64 lógica (n^2)

d) 4, 16, 36, 64, 100 sendo n um número par lógica ( n^2)

e) 1, 1, 2, 3, 5, 8, 13 Essa é a sequência de fibonacci lógica (f(n-1) + f(n-2))

f) 2, 10, 12, 16, 17, 18, 19, Essa sequéncia não apresenta uma lógica bem definida

````

#### 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

````
  Entendi que estou em uma sala com três interruptores e preciso descobrir qual interruptor é de cada lâmpada de outra sala com três lâmpadas.
  
  Posso resolver isso dessa forma: 
    1. Posso ligar o interruptor de duas lâmpadas e anotar.
    2. Ir até a sala anotar quais lâmpadas ligaram, o interruptor da lâmpada apagada eu já sei (check).
    3. Voltar até os interruptores desligar um dos interruptores que liguei
    4. Na segunda ida até a sala, observar qual das lâmpadas apagou.
    5. Com isso, consigo identificar qual interruptor controla as outras duas últimas lâmpadas (check e check).

````
     
#### 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

[Pergunta 5: ](https://github.com/MurilodioPy/desafio/blob/main/pergunta_5.py)

````
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

````
