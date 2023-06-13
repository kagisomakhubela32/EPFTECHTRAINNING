maxnum = 999
palindrome = 0
productChar = 0
productRv = 0
product = 0

for x in range(100,maxnum):
    for y in range(100,maxnum):
        product = x * y
        productChar = str(product)
        productRv = str(product)[::-1]

        if (productChar == productRv and product > palindrome):
            palindrome = product
print(palindrome)
           