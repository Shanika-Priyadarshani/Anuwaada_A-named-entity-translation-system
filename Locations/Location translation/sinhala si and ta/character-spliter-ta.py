import unicodedata
const = ['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ' 'ஔ','க','ங','ச','ஞ','ட', 'ண','த','ந','ப','ம','ய','ர','ல','வ','ழ','ள','ற' ,'ன','ஶ','ஜ', 'ஷ','ஸ','ஹ','க்ஷ' ]

file = open("SPLITTED_locations_sinhala_ta casemarkers.txt",'w')

with open("locations_sinhala_ta casemarkers.txt") as f:
    file_content = f.readlines()
    for line in file_content:
        line=line.strip()+'\n'
        
        for c in const:
            if (c in line):
                line = line.replace(c, ' '+c)
            if ('\n' in line):
                line = line.replace('\n ', '\n')
        file.write(line.lstrip())
        print(line)
    file.close()

