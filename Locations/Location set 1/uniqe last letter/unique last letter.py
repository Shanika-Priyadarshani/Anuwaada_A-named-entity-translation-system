import linecache

file1 = "SPLITTED_parallel_loc_si-ta_si.txt"
file2 = "SPLITTED_parallel_loc_si-ta_ta.txt"

file_si = open("LOC names_for_casemarker_list_si.txt",'w')
file_ta = open("LOC names_for_casemarker_list_ta.txt",'w')

i=1
last_letter_list = []

while i< 76015:
    line_si = linecache.getline(file1,i).strip()
    line_ta = linecache.getline(file2,i).strip()
    line = line_si.split(" ")
    last_letter = line[len(line)-2]+line[len(line)-1]
    if last_letter in last_letter_list:
        y = 1
    else:
        print(last_letter ,",", line_si,",", line_ta)
        last_letter_list.append(last_letter)
        line_si = line_si+'\n'
        file_si.write(line_si.lstrip())
        line_ta = line_ta+'\n'
        file_ta.write(line_ta.lstrip())
    i+=1

file_si.close()
file_ta.close()
