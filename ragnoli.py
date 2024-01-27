import string 
alp_list=list(string.ascii_lowercase)


n=int(input('enter a num '))

width=1+4*(n-1)

alp_n=alp_list[0:n] 
rev_alp=alp_n[::-1]


for l in rev_alp:
    index_l=rev_alp.index(l)+1

    des_l=rev_alp[0:index_l]

    acs_l=alp_n[alp_n.index(l)+1:]

    des_l+=acs_l

    o='-'.join(des_l)

    print(o.center(width,'-'))

for c in alp_n[1:n+1]:
    lst=alp_n[alp_n.index(c):]
    lst_2=rev_alp[0:rev_alp.index(c)]
    lst_2+=lst
    j_2="-".join(lst_2)         
    print(j_2.center(width,'-'))


#------------g------------
#----------g-f-g----------
#--------g-f-e-f-g--------
#------g-f-e-d-e-f-g------
#----g-f-e-d-c-d-e-f-g----
#--g-f-e-d-c-b-c-d-e-f-g--
#g-f-e-d-c-b-a-b-c-d-e-f-g
#--g-f-e-d-c-b-c-d-e-f-g--
#----g-f-e-d-c-d-e-f-g----
#------g-f-e-d-e-f-g------
#--------g-f-e-f-g--------
#----------g-f-g----------
#------------g------------