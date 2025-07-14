#digital clock
#ex 12:17:01
#ex 12:17:02
#for sleep import time
#import sys  for system

import time
import sys
h=12
m=58
s=0
while True:
    sys.stdout.write(f"\r{h:02d} : {m:02d} : {s:02d}") #write for printing 2digit number it is available in stdout
    sys.stdout.flush()  #flush is to delete or vanish
    time.sleep(1)
    s=s+1
    if(s==60):
        m=m+1
        s=0
    if(m==60):
        h=h+1
        s=0
    if(h==13) and m==0 and s==0:
        print("\n12 hours format reached") #after 12 hours 13:00:00  it will give message and exit
        break
