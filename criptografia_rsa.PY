import random
import time
import math



def pre_cod(poem):
   """
    Conversão das letras do poema em números(string de números) usando a tabela de conversão 
    """
   poem_pre_cod = ""
   pre_cod = []
   for char in poem:
      if char == ' ':
         pre_cod.append(36)
      elif char == '.':
        pre_cod.append(37)
      else:
        pre_cod.append(ord(char) - 55)
   for i in range(len(pre_cod)):
       poem_pre_cod += str(pre_cod[i])
   return poem_pre_cod




def mod(a,b): # mod function
    if(a<b):
        return a
    else:
        c=a%b
        return c

def extended_euclides(a, b):
    if b == 0:
        return a, 1, 0

    mdc, x, y = extended_euclides(b, a % b)
    x, y = y, x - (a // b) * y
    return mdc, x, y


def e_search(totient):
    while True:
        e = random.randrange(2,100)
        mdc, _, _ = extended_euclides(e, totient)
        if(mdc == 1):
         return e
     
def d_search(e, totient):
    _ , alfa , _ = extended_euclides(e, totient)
    d = alfa % totient
    return d
    

def is_prime(n):
    """
    Verifica se um número é primo utilizando o teste de Miller-Rabin.
    Retorna True se for provavelmente primo, False caso contrário.
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    def miller_rabin(n, a):
        """
        Teste de Miller-Rabin para uma base a específica.
        Retorna True se n é provavelmente primo, False caso contrário.
        """
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for k in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    # Executa o teste de Miller-Rabin para as 10 primeiras bases
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if not miller_rabin(n, a):
            return False

    return True

def generate_large_prime():
    """
    Gera um número primo grande entre 6 e 9 algarismos, utilizando o método descrito.
    """
    while True:
        n = random.randint(10**5, 10**6 - 1) * 10 + random.choice([1, 3, 7, 9])
        if is_prime(n):
            return n

def quebra_poema(n, poema):
    """
    Quebra o poema pré codificado em uma lista de números menores que n.
    """
    l_n = len(str(n))
    l_poema = len(poema)

    if(l_n%2==0):
        l_block = l_n - 2
    else:
        l_block = l_n - 1

    n_blocos = l_poema//l_block + 1

    blocks = []
    for i in range(n_blocos):
        aux = ""
        for j in range(l_block):
            ind = j + i*l_block
            if(ind<l_poema):
                aux += poema[ind]
        blocks.append(int(aux))    
    return blocks

########### Encontra dois números primos grandes
start_time = time.time()
p = generate_large_prime()
q = generate_large_prime()
end_time = time.time()
processing_time = end_time - start_time
n = p*q
totient = (p-1)*(q-1)
#########Números primos encontrados
print('Números primos encontrados: ',p ,q)
print("Tempo para achar os primos: ", processing_time)

########Pré-codificação

poem = "NAO SOU NADA. NUNCA SEREI NADA. NAO POSSO QUERER SER NADA. A PARTE ISSO TENHO EM MIM TODOS OS SONHOS DO MUNDO. ESTOU HOJE VENCIDO COMO SE SOUBESSE A VERDADE. ESTOU HOJE PERPLEXO COMO QUEM PENSOU E ACHOU E ESQUECEU."
poem_pre_cod = pre_cod(poem)
print(poem_pre_cod)
e = e_search(totient)
print("Chave da codificacao: ", n, e)

##Achando o d
d = d_search(e, totient)
print("Chave da decodificacao: ", n, d)



blocks = quebra_poema(n, poem_pre_cod)

print('Blocos: ')
print(blocks)

########Codificação

blocks_cod = []
for block in blocks:
    C_b = block**e % n
    blocks_cod.append(C_b)

print("Blocos codificados: ", blocks_cod)

##########Decodificação

blocks_decod = []
for block in blocks_cod:
    D_a = block**d % n
    blocks_decod.append(D_a)

print("Blocos decodificado: ", blocks_decod)

