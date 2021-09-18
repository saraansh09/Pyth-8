import csv
import pandas as pd
import math

with open("class1.csv", newline="") as f:
    reader = csv.reader(f)
    a = list(reader)
    a.pop(0)
    ab = []
    for i in range(len(a)):
        abcd = a[i][0]
        ab.append(float(abcd))
    hello = len(ab)
    world = 0
    for e in ab:
        world += e
    mean = world/hello
    print("The mean is: " + str(mean))
vava = []
for d in abcd:
    jaba = int(d)-mean
    jaba = jaba*jaba
    vava.append(jaba)
nana = 0
for b in vava:
    nana+=b
baba = nana/(hello-1)
gaga = math.sqrt(baba)

print("Standard Deviation is: " + str(gaga))
df = pd.read_csv("class1.csv")
