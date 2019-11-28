import unicodedata
const = ['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ' 'ஔ','க','ங','ச','ஞ','ட', 'ண','த','ந','ப','ம','ய','ர','ல','வ','ழ','ள','ற' ,'ன','ஶ','ஜ', 'ஷ','ஸ','ஹ','க்ஷ' ]

file = open("muslim_splitted_names_unique_random_with_cases_ta.txt",'w')

with open("muslim_names_unique_random_with_cases_ta.txt") as f:
    file_content = f.readlines()
    for line in file_content:
        #if ' ' in line:
            #line = line.replace(' ', '\n')

        for c in const:
            if (c in line):
                line = line.replace(c, ' '+c)
            if ('\n' in line):
                line = line.replace('\n ', '\n')
        file.write(line.lstrip())
    file.close()

