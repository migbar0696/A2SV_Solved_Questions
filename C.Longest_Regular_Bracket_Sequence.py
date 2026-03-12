s = input()
stack = []

scnt = 0
maxl = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        sumn = 0
        j = len(stack) - 1
        while j >= 0 and stack[j].isdigit():
            num = stack.pop()
            sumn += int(num)
            
            # print(num)
            j -= 1
        
        if stack:
            if stack[-1] == "(":
                stack.pop()
                sumn += 1
                stack.append(str(sumn))
            else:
                if sumn > 0 :
                    stack.append(str(sumn)) 
        else:
            if sumn != 0:
                stack.append(str(sumn))
                
    stack.append(s[i])
        # print(stack)


sumn = 0
stack2 = []

j = 0
while j < len(stack):
    while j < len(stack) and stack[j].isdigit():
        sumn += int(stack[j])
        j += 1
    if sumn != 0:
        stack2.append(str(sumn))
        sumn = 0
    if j < len(stack) and  not stack[j].isdigit():
        stack2.append(str(stack[j]))
    j += 1

# print(stack2)
        
for i in range(len(stack2)):
    if stack2[i].isdigit():

        maxl = max(maxl, int(stack2[i]))
scnt = stack2.count(f"{maxl}")
print(maxl * 2, scnt) if maxl != 0 else print(0, 1)
