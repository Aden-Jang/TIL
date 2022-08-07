# 시험실행 - time limit exceeded
s = 'babad'
ans = []
for i in range(len(s)):
    for j in range(len(s)-1,i,-1):
        if s[i] == s[j]:
            for k in range(i,j+1):
                if (j-i)%2 == 0:
                    if k == j-k+i:
                        ans.append(s[i:j+1])
                        break
                    elif s[k] == s[j-k+i]:
                        continue
                    else:
                        break
                else:
                    if k+1 == j-k+i:
                        if s[k] == s[j-k+i]:
                            ans.append(s[i:j+1])
                            break
                        else:
                            continue
                    if s[k] == s[j-k+i]:
                        continue
                    else:
                        break
if ans !=[]:
    print(max(ans, key = len))
else:
    print(s[0])
