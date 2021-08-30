with open("template.txt","r") as template:
    sorce=template.readlines()
code=[]
for i in range(0 ,10):
    try:
        with open(f'output{i}.txt') as line:
            code.append(line.readline())
    except:
        code.append(' ')
print( sorce )
for i in range(1 ,10):
    sorce[i+50]=f"case '{i}': digitalWrite(LED_BUILTIN, HIGH); {code[i]}  digitalWrite(LED_BUILTIN, LOW); break; \n"
sorce[90]=f'digitalWrite(LED_BUILTIN, HIGH); {code[0]}digitalWrite(LED_BUILTIN, LOW); '

print( code )
with open("code_final.txt","w") as output:
    output.writelines(sorce)

