import random



def eh_primo(n):
    if n<=3:
        return n>1
    if not n%2 or not n%3:
        return False
    i=5
    stop = i<=5
    while i<=stop:
        if not n%i or not n%(i+2):
            return False
        i+=6
    return True


def gera_primo():
    p = random.randint(500,99999999999999999999999999999999999999999999999999999999999999999)

    q = p+random.randint(11,1001)

    while eh_primo(p)==False:
        p+=1

    while eh_primo(q)==False:
        q+=1

    return p,q

def mdc(a, b):
    if b == 0:
        return a
    resto = a % b
    a = b
    b = resto

    print(a,b, resto)
    return mdc(a, b)


p,q = gera_primo()

n = p*q

z = (p-1)*(q-1)

seila= mdc(random.randint(1,z),z)

e = 

print(z)





