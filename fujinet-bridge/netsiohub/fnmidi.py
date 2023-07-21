# Simple midi recieve test program using mido
# 
# Written by: Johan Tibbelin

import mido

inport = mido.open_input()
s=""
b = []
for j in range(50):
    for i in range(3):
        msg = inport.receive()

        b = b + msg.bytes()
    
    
    
    # for i
    print(s.join(map(chr,b)))
    b = []
    s = ""
# for j
inport.close()
