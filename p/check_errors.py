import os
import re

zz_groups = []

dir_mds = 'C:\Users\diego\ck3aars\ck3-murchad'
ppl_file = 'C:\Users\diego\ck3aars\ck3-murchad\people.md'
history_dirs = 'C:\Users\diego\ck3aars\ck3-murchad\h'
with open(ppl_file, 'r') as fp:
    for line in fp.readlines():
        zm = re.search('\[([\w\s\-\+]+)\]\((.*?)\)\s+\(([0-9\-\s]+)\).*\*(.*)\*', line)
        if zm:
            zz_groups.append(zm.groups(1))
work_all = []
for zz_s in zz_groups:
    work_info = [] 
    full_file = os.path.join(dir_mds, zz_s[1])
    short_list = zz_s[1].split('/')[1].split('_')[:-1]
    word_list = set(short_list + [zz_s[2].strip()]+zz_s[3].replace(',',' ').lower().strip().split())
    #print(word_list)
    # print(short_list, zz_s[2], zz_s[3])
    work_info = [] 
    
    with open(full_file, 'r') as f:
        lines = []
        in_family_tree = False
        for i, line in enumerate(f.readlines()):
             if i == 0:
                  title_list = set(line[2:].replace(',',' ').replace('(',' ').replace(')',' ').strip().lower().split())
                  #print(title_list)
             if in_family_tree:
                  
                  if "```" in line:
                       in_family_tree = False
                       continue
                  else:
                       lines.append(line.rstrip())
             else:
                  if "```" in line:
                       in_family_tree = True
                       continue

        first_line = set(lines[0].lower().replace(',',' ').replace('(',' ').replace(')',' ').strip().split())
        #print(first_line)
        if not (first_line == title_list == word_list):
             print(word_list)
             print(title_list)
             print(first_line)
             
        print("============================")  

