def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
           for i in range(2, sayi):
               if(sayi % i == 0):
                  break
           else:
                print(sayi)
                
sayi1 = int(input('sayi 1 : '))
sayi2 = int(input('sayi 2 : '))

def Fak(sayi3,a):
	for i in range(2,sayi3+1)
		a=a*i
	print a

sayi3=input("sayi giriniz:")
a=1
Fak(sayi3,a)
asalSayilariBul(sayi1, sayi2)
