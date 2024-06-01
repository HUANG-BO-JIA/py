num = int(input("請輸入整數:"))
for i in range(num+1):
    print(' '*(num-i)+'♣'*(2*i-1))