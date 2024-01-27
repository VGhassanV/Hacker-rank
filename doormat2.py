inp=input()
inp_lst=inp.split()
N=int(inp_lst[0])
M=int(inp_lst[1])
r=(N-1)//2
d=".|."

for i in range(int(r)):
    print((d*(1+(2*i))).center(M,"-"))

print("PYTHON".center(M,"-"))

for i in range(r-1,-1,-1):
        
   print((d*(1+(2*i))).center(M,"-"))
    
    
#--------.|.---------
#-----.|..|..|.------
#--.|..|..|..|..|.---
#.|..|..|..|..|..|..|.
#-------PYTHON-------
#.|..|..|..|..|..|..|.
#--.|..|..|..|..|.---
#-----.|..|..|.------
#--------.|.---------