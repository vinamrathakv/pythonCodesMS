# find longest common prefix between two stringStart

def prefix(s1, s2):
    p = ''
    for c in s1:
        p += c
        
        if s2.startswith(p):
            continue
        else:
            return p[0:len(p)-1]


def main():
    
    s1 = input("String 1 : ")
    s2 = input("string 2 : ")
    
    pre = prefix(s1,s2)
    print("Longest prefix is : ",pre)        
    
main()
        