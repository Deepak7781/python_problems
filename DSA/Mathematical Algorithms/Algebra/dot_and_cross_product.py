'''
There are two vector A and B and we have to find the dot product and cross product of two vector array. Dot product is also known as scalar product and cross product also known as vector product.
Dot Product – Let we have given two vector A = a1 * i + a2 * j + a3 * k and B = b1 * i + b2 * j + b3 * k. Where i, j and k are the unit vector along the x, y and z directions. Then dot product is calculated as dot product = a1 * b1 + a2 * b2 + a3 * b3
Example – 
 

A = 3 * i + 5 * j + 4 * k
B = 2 * i + 7 * j + 5 * k
dot product = 3 * 2 + 5 * 7 + 4 * 5
            = 6 + 35 + 20
            = 61


Cross Product – Let we have given two vector A = a1 * i + a2 * j + a3 * k and B = b1 * i + b2 * j + b3 * k. Then cross product is calculated as cross product = (a2 * b3 – a3 * b2) * i + (a3 * b1 – a1 * b3) * j + (a1 * b2 – a2 * b1) * k, where [(a2 * b3 – a3 * b2), (a3 * b1 – a1 * b3), (a1 * b2 – a2 * b1)] are the coefficient of unit vector along i, j and k directions.
Example – 
 

A = 3 * i + 5 * j + 4 * k
B = 2 * i + 7 * j + 5 * k
cross product 
= (5 * 5 - 4 * 7) * i 
      + (4 * 2 - 3 * 5) * j + (3 * 7 - 5 * 2) * k
= (-3)*i + (-7)*j + (11)*k


Example – 
 

Input: vect_A[] = {3, -5, 4}
        vect_B[] = {2, 6, 5}
Output: Dot product: -4
         Cross product = -49 -7 28



'''

def dotProduct(vectA,vectB):
    product = 0
    for i in range(len(vectA)):
        product += vectA[i]*vectB[i]

    return product

def crossProduct(vectA,vectB):
    cross = []
    cross.append(vectA[1] * vectB[2] - vectA[2] * vectB[1])
    cross.append(vectA[2] * vectB[0] - vectA[0] * vectB[2])
    cross.append(vectA[0] * vectB[1] - vectA[1] * vectB[0])

    return cross

vectA = [7, 2, 4]
vectB = [10, 2, 8]

print("Dot Product :")
print(dotProduct(vectA,vectB))
print("Cross Product:")
cross_p = crossProduct(vectA,vectB)
if cross_p[1]<0 and cross_p[2]<0:
    print(f"{cross_p[0]}i{cross_p[1]}j{cross_p[2]}k")
elif cross_p[1]<0:
    print(f"{cross_p[0]}i{cross_p[1]}j+{cross_p[2]}k")
elif cross_p[2]<0:
    print(f"{cross_p[0]}i+{cross_p[1]}j{cross_p[2]}k")
else:
    print(f"{cross_p[0]}i+{cross_p[1]}j+{cross_p[2]}k")

    