# -*- coding: UTF-8 -*-

import random
import math
import base64

def make_big_prime(a, b):
    num = random.randint(a,b)
    while(check(num) == False) :
        num = random.randint(a,b)
    return num

def check(num):
    if num < 2:
        return False

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    if num in small_primes:
        return True

    for prime in small_primes:
        if num % prime == 0:
            return False
    return miller_rabbin(num)

def miller_rabbin(num):
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def gcd(a, b):
    if a%b != 0:
        return gcd(b, a%b)
    else:
        return b

def get_(a, b):
    if b == 0:
        return 1, 0
    k = a//b
    remainder = a%b
    x1, y1 = get_(b, remainder)
    x, y = y1, x1-k*y1
    return x, y

if __name__ == "__main__":
    p = make_big_prime(1000000000000000000000,10000000000000000000000000000000000)
    q = make_big_prime(2000000000000000000000,20000000000000000000000000000000000)
    euler = (p-1)*(q-1)
    e = make_big_prime(100000000, 20000000000)
    while gcd(e,euler) != 1:
        e = make_big_prime(100000000, 20000000000)
    
    x, _ = get_(e, euler)
    d = x%euler

    print(f'p = {p}\nq = {q}')
    print(f'e = {e}\nd = {d}')
    s = input("明文:")
    s = base64.b16encode(s.encode('utf-8'))
    c = pow(int(s, 16), e, p*q)
    print("密文："+str(c))
    ans = pow(c, d, p*q)
    ans = "".join((list(hex(ans))[2:])).upper()
    ans = base64.b16decode(ans)
    print("解密："+str(ans, 'utf-8'))