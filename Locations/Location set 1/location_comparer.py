import linecache


file_si = open("parallel_loc_si-ta_si.txt",'w')
file_ta = open("parallel_loc_si-ta_ta.txt",'w')

file1 = "locations-set 1.si"
file2 = "locations-set 1.ta"

i=1

while i< 56179:
    line_si = linecache.getline(file1,i).strip()
    line_ta = linecache.getline(file2,i).strip()

    if str(line_si) != '' and str(line_ta) != '':
        print (line_si, " --- ", line_ta)
        line_si = line_si+'\n'
        file_si.write(line_si.lstrip())
        line_ta = line_ta+'\n'
        file_ta.write(line_ta.lstrip())
    i+=1

file_si.close()
file_ta.close()
