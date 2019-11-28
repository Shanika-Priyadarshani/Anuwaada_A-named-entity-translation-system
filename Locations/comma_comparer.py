import linecache

file_si = open("loc_with_no_equal_commas_si.txt",'w')
file_ta = open("loc_with_no_equal_commas_ta.txt",'w')

file1 = "address.tok.si-ta.si"
file2 = "address.tok.si-ta.ta"

i=1

while i< 99647:
    line_si = linecache.getline(file1,i).strip()
    line_ta = linecache.getline(file2,i).strip()
    if line_si.count(',') == line_ta.count(','):
        print(i, line_si.count(',') , line_ta.count(','))
    else:
        line_si = line_si+'\n'
        file_si.write(line_si.lstrip())
        line_ta = line_ta+'\n'
        file_ta.write(line_ta.lstrip())
    i+=1

file_si.close()
file_ta.close()
