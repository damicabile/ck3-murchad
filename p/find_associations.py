import os
import re

dir_mds = 'C:\Users\diego\ck3aars\ck3-murchad\p'
ppl_file = 'C:\Users\diego\ck3aars\ck3-murchad\people.md'
history_dirs = 'C:\Users\diego\ck3aars\ck3-murchad\h'
history_ffs = ['1227.md']

file_names = []  
for file_name in os.listdir(dir_mds):
    if ('.md' in file_name):
       file_names.append(file_name)

zz_groups = []
    
with open(ppl_file, 'r') as fp:
    for line in fp.readlines():
        zm = re.search('\[([\w\s\-\+]+)\]\((.*?)\)', line)
        if zm:
            zz_groups.append(zm.groups(1)[1])
            

zz_all = zz_groups[:len(file_names)]

zz_st = zip(file_names, zz_all)

for zz_s in zz_st:
    print(zz_s)
