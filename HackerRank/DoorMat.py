# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N , M = map(int, input().split())
# M = 3*N  #because it will be done implicitly by hackerank, no need to ovrwrite

ro = math.floor(N/2)
for i in range(0 ,ro):
    print(('.|.'*(i*2+1)).center(M,'-'))
    
print('WELCOME'.center(M,'-'))

for i in range(ro-1,-1,-1):
    print(('.|.'*(i*2+1)).center(M,'-'))
