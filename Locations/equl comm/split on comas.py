import linecache

file_si = open("split on commas_ta",'w')

file1 = "loc_with_equal_commas_ta.txt"

i=1

while i< 99647:
    line_si = linecache.getline(file1,i).strip()
    line = line_si.split(',')
    for word in line:
        if word != ',':
            x= word+'\n'
            file_si.write(x.lstrip())
            print (word)
      
    i+=1

file_si.close()

