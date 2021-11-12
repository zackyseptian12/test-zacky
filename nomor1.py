def deret():
    print('Un =  a + (n-1)b')
    a =int(input('masukan angka a :'))
    b =int(input('masukan angka b :'))
    print(f'Un =  (a-b)+(b)n')
    Un=[]
    while True:
        n=int(input('Input n (Batas barisan yang ingin dik) :'))
        for n in range(1,n+1,1):
            Un.append((a-b)+(b*n))
        print(Un)
deret()