tahun = int(input("masukan tahun "))
def kabisat(tahun):
    if(tahun % 4 == 0 and tahun % 100 != 0 or tahun % 400 == 0):
        print(f'{tahun} adalah tahun kabisat')
    else :
       print(f'{tahun} adalah bukan tahun kabisat') 

kabisat(tahun)
