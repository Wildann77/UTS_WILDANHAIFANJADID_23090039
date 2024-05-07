
def operasi():
    while True: 
        main = int(input('Masukan Berat badan '))
        main2 = int(input('Masukan tinggi badan '))
        hasil = main/main2
        if hasil < 18.5:
         print(f'berat badan = {main}')
         print(f'tinggi badan = {main2}')
         print(f'nilai bmi  = {hasil}')
         print('berat badan kurang')
         break
        elif 18.5 <= hasil < 24.9:
          print(f'berat badan = {main}')
          print(f'tinggi badan = {main2}')
          print(f'nilai bmi  = {hasil}')
          print('berat badan normal')
          break
        elif 25 <= hasil < 29.9:
          print(f'berat badan = {main}')
          print(f'tinggi badan = {main2}')
          print(f'nilai bmi  = {hasil}')
          print('kelebihan berat badan')
          break
        elif  hasil >= 30:
          print(f'berat badan = {main}')
          print(f'tinggi badan = {main2}')
          print(f'nilai bmi  = {hasil}')
          print('obesitas')
          break


operasi()
    