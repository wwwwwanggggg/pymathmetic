def v_p_norm(v,p,n=None):   
    if n is None:
        n = len(v)-1
    
    res = 0
    for i in range(1,n+1):  
        res += abs(v[i]) ** p
    
    return res ** (1/p)


def v_infty_norm(v,n=None): 
    if n is None:
        n = len(v)-1
    
    tv = [abs(v[i]) for i in range(1,n+1)]
    
    return max(tv)


def mat_1norm(mat,n=None):
    if n is None:
        n = len(mat)-1
    
    res = -1
    for i in range(1,n+1):
        temp = v_p_norm(mat[i],1,n)
        res = max(res,temp)

    return res






