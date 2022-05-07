from cmath import pi
import numpy
import math
from random import randint

#scaled by lamda
lam = 100;
q = 2*16;
sigma = 1.0; #standard deviation
n= 3;

#normal (Gaussian) distribution
delta_error = numpy.int64(numpy.random.normal(0,sigma,n)) #center , width , size of matrix
numpy.vectorize(delta_error);

calc =((math.sqrt(2*pi)*sigma)/q)
if n*math.log(q,2) >= (0.63*lam - 0.21)*(math.log(calc,2)) :
    print("-------TRUE------\n")
else:
    print("------FALSE------\n")

def gen_privateKey() -> int:
    return randint(0, sigma)

# Generate the secret generakey as a row vector such that each element is sampled from the distribution N (0,sigma, 0 ). Return sk.
sk = numpy.random.randint(256, size=(n));

# Encryption
m = [1.2345, 2.2345, 3.2345];
m_scaled=[]
for i in range(0,n):
    m_scaled_i = int((m[i] *lam) %q);
    m_scaled.append(m_scaled_i)
m_scaled = numpy.array(m_scaled)

a = numpy.random.uniform(0,sigma,size=(n,n))
print("a: \n",a)
print("secrete negative: \n",numpy.negative(sk))
print("m scaled: \n",m_scaled)
print("delta error: \n", delta_error)

# b = −sk · a + m + ∆ mod q.
b_1 = numpy.dot(sk,a)
b_2 = -b_1 + m_scaled ;
b = (b_2 +delta_error) % q
print("Cyphertext:\n",b)

# Decryption
dec_1 = numpy.dot(sk,a) 
dec = ( b + dec_1 ) % q
print("dec: \n",dec )
