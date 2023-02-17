def isIsomorphic(s: str, t: str): # Учитывая две строки s и t, определите, являются ли они изоморфными.
    ind = True
    if len(s) != len(t):
        return False
    else:
        d = {}
        for i in range(len(s)):
            if d.get(s[i]) == None and not(t[i] in d.values()):
                d[s[i]]=t[i]
            else:
                if d.get(s[i]) == None or d[s[i]] != t[i]:
                    ind = False
        return ind
    

def isSubsequence(s: str, t: str): # Даны две строки s и t, возвращает true если s является 
    # подпоследовательностью t, или false в противном случае
    count = -1 
    ind = 0
    for i in range(len(s)):
        for j in range(count+1,len(t)):
            if s[i]==t[j]:
                count = j
                ind +=1
                break
        if ind < i+1:
            break                
    if ind == len(s):
        return True
    else:
        return False
