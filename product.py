import os
product = []

# 检查
if os.path.isfile('products.csv'):
	print ('file exist')

	with open ('products.csv', 'r') as f:
		for line in f:
			if '商品,价格' in line:
				continue
			name, price = line.strip().split(',')
			product. append([name, price])
		
	print (product)
else:
	Print('file does not exist')


# 写入
while True:
	name = input('请输入商品名称：')
	if name == 'q':
		break
	price = input('请输入商品价格：')
	product. append([name, price])

print ('name','price')
for p in product:
	print (p[0], p[1])

# 更新

with open ('products.csv', 'w') as f:
	f.write('商品,价格\n')
	for p in product:
		f.write (p[0] + ','+ p[1]+ '\n')