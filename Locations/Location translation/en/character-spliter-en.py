import unicodedata
const = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','ං',
              's','t','u','v','w','x',
              'y','z']

file = open("SPLITTED_parallel_loc_ta-en_en.txt",'w')

with open("cleaned en_ta.en") as f:
    file_content = f.readlines()
    for line in file_content:
        line=line.strip()+'\n'
        
        for c in const:
            if (c in line):
                line = line.replace(c, ' '+c)
            if ('\n' in line):
                line = line.replace('\n ', '\n')
        file.write(line.lstrip())
        print (line)
    file.close()

