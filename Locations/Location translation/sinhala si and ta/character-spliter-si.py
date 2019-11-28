import unicodedata
const = ['අ','ආ','ඇ','ඈ','ඉ','ඊ','උ','ඌ','ඍ','ඎ','ඏ','ඐ','එ','ඒ','ඓ','ඔ','ඕ','ඖ','ං',
              'ක','ඛ','ග','ඝ','ඞ','ඟ',
              'ච','ඡ','ජ','ඣ','ඤ','ඥ',
              'ඦ','ට','ඨ','ඩ','ඪ','ණ','ඬ',
              'ත','ථ','ද','ධ','න','ඳ',
              'ප','ඵ','බ','භ','ම','ඹ',
              'ය','ර','ල','ව','ශ','ෂ','ස','හ','ළ','ෆ']

file = open("SPLITTED_locations_sinhala_si casemarkers.txt",'w')

with open("locations_sinhala_si casemarkers.txt") as f:
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

