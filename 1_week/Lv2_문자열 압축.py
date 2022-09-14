def solution(s):

    count=0
    mini=len(s)

    for i in range(1,int(len(s)/2+1)):

        temp=list(s[0:i])
        temp2=list(s[0:i])
        
        count=0

        for j in range(i,len(s)+1,i):
            if(temp==list(s[j:j+i])):

                del temp2[j:j+i]
                if(count==0):
                    temp2.append(count+1)
                else:
                    temp2.pop()
                    temp2.append(count+1)
                    
                count+=1

            else:

                temp=list(s[j:j+i])
                temp2=temp2+list(s[j:j+i])
                count=0
                
#            print(i,temp2,end="")
#        print()
        if(len(temp2)<mini):
            mini=len(temp2)
#            print(temp2)
                
            for k in temp2 :
                if isinstance(k,int):
                    mini-=1
                    mini+=len(str(k+1))
                
    
    return mini

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("xxxxxxxxxxyyy"))

#print(solution("abcabcdede"))
#print(solution("abcabcabcabcdededededede"))
#print(solution("xababcdcdababcdcd"))
    
