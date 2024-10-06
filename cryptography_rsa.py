import random
import time

def sieve_of_eratosthenes(limit):
    """Crivo de Eratóstenes para encontrar todos os números primos até o limite."""
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes

def pre_cod(poem):
    """Conversão das letras do poema em números (string de números) usando a tabela de conversão."""
    poem_pre_cod = ""
    pre_cod = []
    for char in poem:
        if char == ' ':
            pre_cod.append(36)
        elif char == '.':
            pre_cod.append(37)
        else:
            pre_cod.append(ord(char) - 55)
    for num in pre_cod:
        poem_pre_cod += str(num)
    return poem_pre_cod

def extended_euclides(a, b):
    if b == 0:
        return a, 1, 0
    mdc, x, y = extended_euclides(b, a % b)
    return mdc, y, x - (a // b) * y

def e_search(totient):
    while True:
        e = random.randrange(2, totient)
        mdc, _, _ = extended_euclides(e, totient)
        if mdc == 1:
            return e

def d_search(e, totient):
    _, alfa, _ = extended_euclides(e, totient)
    return alfa % totient

def quebra_poema(n, poema):
    l_n = len(str(n))
    l_block = l_n - 2 if l_n % 2 == 0 else l_n - 1
    n_blocos = len(poema) // l_block + 1
    blocks = []
    for i in range(n_blocos):
        aux = "".join(poema[j + i * l_block] for j in range(l_block) if j + i * l_block < len(poema))
        blocks.append(int(aux))
    return blocks

# Defina um limite grande para encontrar números primos suficientes
LIMIT = 10**6

# Encontra números primos até o limite usando o Crivo de Eratóstenes
start_time = time.time()
primes = sieve_of_eratosthenes(LIMIT)
end_time = time.time()
processing_time = end_time - start_time

# Seleciona aleatoriamente dois números primos grandes da lista de primos
p = random.choice(primes[-1000:])  # Seleciona um primo aleatório dos 1000 maiores
q = random.choice(primes[-1000:])  # Seleciona outro primo aleatório dos 1000 maiores

# Assegura que p e q são diferentes
while p == q:
    q = random.choice(primes[-1000:])

n = p * q
totient = (p - 1) * (q - 1)

print('Números primos encontrados:', p, q)
print("Tempo para achar os primos:", processing_time)

# Pré-codificação
poem = ("NO MEIO DO CAMINHO TINHA UMA PEDRA. TINHA UMA PEDRA NO MEIO DO "
        "CAMINHO. TINHA UMA PEDRA. NO MEIO DO CAMINHO TINHA UMA PEDRA. "
        "NUNCA ME ESQUECEREI DESSE ACONTECIMENTO NA VIDA DE MINHAS RETINAS "
        "TÃO FATIGADAS. NUNCA ME ESQUECEREI QUE NO MEIO DO CAMINHO TINHA "
        "UMA PEDRA. TINHA UMA PEDRA. TINHA UMA PEDRA NO MEIO DO CAMINHO. NO "
        "MEIO DO CAMINHO TINHA UMA PEDRA. POEMA DE CARLOS DRUMMOND DE ANDRADE.")
poem_pre_cod = pre_cod(poem)
print("Poema pré-codificado:", poem_pre_cod)

e = e_search(totient)
print("Chave da codificação:", n, e)

d = d_search(e, totient)
print("Chave da decodificação:", n, d)

blocks = quebra_poema(n, poem_pre_cod)
print('Blocos:', blocks)

# Codificação
blocks_cod = [pow(block, e, n) for block in blocks]
print("Blocos codificados:", blocks_cod)

# Decodificação correta
blocks_decod = [pow(block, d, n) for block in blocks_cod]
print("Blocos decodificados corretamente:", blocks_decod)

# Verificação da decodificação correta
decoded_poem = "".join(str(block) for block in blocks_decod)
print("Poema decodificado corretamente:", decoded_poem)

# Seleciona dois novos números primos diferentes
new_p = random.choice(primes[-1000:])
new_q = random.choice(primes[-1000:])

while new_p == new_q or new_p == p or new_q == q:
    new_p = random.choice(primes[-1000:])
    new_q = random.choice(primes[-1000:])

new_n = new_p * new_q
new_totient = (new_p - 1) * (new_q - 1)
new_d = d_search(e, new_totient)

# Decodificação incorreta
blocks_decod_incorreto = [pow(block, new_d, new_n) for block in blocks_cod]
print("Blocos decodificados incorretamente:", blocks_decod_incorreto)

# Verificação da decodificação incorreta
decoded_poem_incorreto = "".join(str(block) for block in blocks_decod_incorreto)
print("Poema decodificado incorretamente:", decoded_poem_incorreto)
