'''Deret Fibonacci adalah himpunan bilangan yang dimulai dengan angka satu atau nol, 
kemudian diikuti oleh satu,
dan angka selanjutnya merupakan jumlah dari dua angka sebelumnya. 
Seperti misalnya: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55.'''

#tentukan jumlah deret fibonacci
Angka = 3

#tentukan angka pertama
n = 0
#tentukan angka kedua
n1 = 1
#jumlah angka yang dihitung
count = 2

#periksa angka
if Angka <= 0:
	print("Angka harus diatas 0")
elif Angka == 1:
	print("Deret fibonacci : ",Angka,":")
	print(n)
else:
	print("Deret fibonacci : ",Angka,":")
	print(n)
	print(n1)
	while count < Angka:
		nth = n+n1
		print(nth)
		#tukar nilai untuk mendapatkan 2 index terakhir
		n=n1
		n1=nth
		count+=1