product = []
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	product. append([name, price])
print (product)