def print_rangoli(size):
    # your code goes here
    p = 96 + size
    a = ( size - 1 ) * 2 + 1
    w = ( size - 1 ) * 4 + 1
    
    for i in range(a):
        ptrn = ""
        
        if i < size:
            itr = i
            v = p - i
        else:
            itr = a - i - 1
            v = p + i + 1 - a
        
        for j in range(itr):
            ptrn += chr(v-j+itr) + "-"
        
        ptrn += chr(v) + ptrn[::-1]
        print(ptrn.center(w,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)