#!/usr/bin/python
import csv
import sys

if len(sys.argv) < 4:
    print("Usage: ./genetate_training_csv.py synonyms original_csv output")

synonyms = sys.argv[1]

f = open(synonyms)

syn_set = set()
for line in f:
    line = line.strip()
    syn_set.add(line.decode("utf-8"))

f.close()


original_csv = sys.argv[2]
found_synonyms = 0
count = 0
syn_list = []
f = open(original_csv)
rd = csv.reader(f)
rd.next()
for line in rd:
    old_line = line
    line = line[1:3]
    h1 = line[0]
    h2 = line[1]
    mix1 = h1.decode("utf-8")+','+h2.decode("utf-8")
    mix2 = h2.decode("utf-8")+','+h1.decode("utf-8")
    #print(mix1)
    #print(mix)
    if mix1 in syn_set or mix2 in syn_set: 
        found_synonyms += 1
        print("Found a synonym : ) - Count: "+str(count))
        syn_list.append(old_line)
    count += 1

print("End - Count: "+str(count)+" - Found: "+str(found_synonyms))
f.close()


output_file = sys.argv[3]
f = open(output_file, "w")
wr = csv.writer(f)
for elm in syn_list:
    wr.writerow(elm[3:])

f.close()
print("Done!")
