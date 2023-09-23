def linearSearchProduct(productList,targetproduct):
	indices=[]
	for index,product in enumerate(productList):
		if product==targetproduct:
			indices.append(index)
		return indices
products=["shoes","boot","loafer","boot","goki","hai","hai"]
target="shoes"
result=linearSearchProduct(products,target)
print(result)
