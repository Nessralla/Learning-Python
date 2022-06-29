# Similiar ao 1096 porém o J faz 7,6,5; depois 9,8,7; depois 11,10,9 até 15,14,13 e i=9
start=7
end=4

for i in range(1,10,2):
    for j in range(start,end,-1):
        print(f"I={i} J={j}")
    start +=2
    end +=2