'''Armstrong number adalah, jika masing-masing angka n diexponen dengan digit yang dimiliki memiliki jumlah yang sama dengan angka n.
Misal : n = 371, pada n ada 3 digit jadi n^digit

Test 371, 3³ + 7³ + 1³ = 27 + 343 + 1 = 371 '''

def armstrong():
	a = 371
	cv_a = [3,7,1]
	c = 0
	for i in range(3) :
		b = cv_a[i]**3
		c += b
	return c

print(armstrong())