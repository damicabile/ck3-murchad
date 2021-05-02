# import os

## FAMILY TREE 
```
import os


dir_mds = 'C:\Users\diego\ck3aars\ck3-murchad\p'
  
for file_name in os.listdir(dir_mds):
    print(file_name)
    if ('md' in file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            title = lines[0]
            full_name = os.path.join(dir_mds, 'out', file_name)
            print(full_name)
            with open(full_name, 'w') as fw:
                fw.write('# {}\n'.format(title))
                fw.write('## FAMILY TREE \n')
                fw.write('```\n')
                fw.writelines(lines)
                fw.write('```\n')
                
```
