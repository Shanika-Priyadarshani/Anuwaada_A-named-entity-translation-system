import linecache

file_si = open("muslim_names_without_mistakes_si2.txt",'w')
file_ta = open("muslim_names_without_mistakes_ta2.txt",'w')

file_si_mis = open("muslim_names_with_mistakes_si2.txt",'w')
file_ta_mis = open("muslim_names_with_mistakes_ta2.txt",'w')

file1 = "muslim_names_with_mistakes_si.txt"
file2 = "muslim_names_with_mistakes_ta.txt"

i=1

while i< 99647:
    line_si = linecache.getline(file1,i).strip()
    line_ta = linecache.getline(file2,i).strip()
    if line_si.count(' ') != line_ta.count(' '):
        print(i, line_si.count(' ') , line_ta.count(' '))
        line_si = line_si+'\n'
        file_si_mis.write(line_si.lstrip())
        line_ta = line_ta+'\n'
        file_ta_mis.write(line_ta.lstrip())
    else:
        line_si = line_si+'\n'
        file_si.write(line_si.lstrip())
        line_ta = line_ta+'\n'
        file_ta.write(line_ta.lstrip())
    i+=1

file_si.close()
file_ta.close()
file_si_mis.close()
file_ta_mis.close()
