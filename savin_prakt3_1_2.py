# Перемножение транспонированных векторов
from random import randint

# Функция вывода на печать для наглядности
def print_prod(a,b,n):
    for i in range(n):
        if i!=2:
            print(a[i])
        else:
            print(a[i]," X  ",b)
            
    print("\nПроизведени:\n")
    for i in range(n):
        for j in range(n):
            print(a[i],"x",b[j],end="   ")
        print()


    print("\nИтоговая матрица:\n")
    for i in range(n):
        for j in range(n):
            print(a[i]*b[j],end="   ")
        print()

    
# формирование векторов
n=5
vect_a=[]
vect_b=[]
tmp_a=0
tmp_b=0


for i in range(n):
    tmp_a=randint(1,9)
    tmp_b=randint(1,9)
    vect_a.append(tmp_a)
    vect_b.append(tmp_b)
    

print("Вектор а: ",vect_a)
print("Вектор b: ",vect_b)
print()
print_prod(vect_a,vect_b,n)
                  

