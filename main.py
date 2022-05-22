#22.05.2022
def matrisYazdir(m):
    for i in range(len(m)): #satir
        for j in range(len(m[i])): #sütun
            print(m[i][j], end='\t')
        print()


def detHesapla2boyut(m):
    sol=(m[0][0])*(m[1][1])
    sag=(m[0][1])*(m[1][0])
    sonuc=sol-sag
    print("Determinant sonucu: ", sonuc)
    if sonuc==0:
        print("Bu matris terslenemez.")
    else:
        print("Bu matris terslenbilir.")
    return sonuc

def detHesapla3boyut(m):
    sol = (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1])
    sag = (m[2][0] * m[1][1] * m[0][2] + m[2][1] * m[1][2] * m[0][0] + m[2][2] * m[1][0] * m[0][2])
    sonuc=sol-sag
    print("det sonucu: ", sonuc)
    if sonuc==0:
        print("Bu matris terslenemez.")
    else:
        print("Bu matris terslenbilir.")
    return sonuc


#parametreleştirilmiş hali 2x2 ve 3x3lük boyut için tek fonk.
def Determinant(m, n):
    if n<4 and n>1:
        if n==2:
            detHesapla2boyut(m)
            print("2x2 lik determinant sonucu bulundu.")
        elif n==3:
            detHesapla3boyut(m)
            print("3x3 lük determinant sonucu bulundu.")
    else:
        print("Bu boyut hesaplanamaz")



#Ana Program
print("--A matrisinin determinant--")
A=[[2,5,1],[3,7,0],[4,8,9]]
Determinant(A,3)
print()
print("--B matrisinin determinant--")
B=[[4,7],[1,5]]
Determinant(B,2)
print()
print("--C matrisinin determinant--")
C=[[4,12,0],[8,6,3],[2,7,5]]
Determinant(C,3)

