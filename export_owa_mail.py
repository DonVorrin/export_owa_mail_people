import re

print('Example: \nInput file: text.txt\nOutput file: output.txt\n ---------------------------\n\n')

read_file = input('Enter input file: ')
write_file = input('Enter output file: ')
with open(read_file, 'r') as f:
	text = str(set(f.readlines()))

result = re.findall(r'([a-zA-Z0-9_\.]{2,}@[a-zA-Z]*\.[a-zA-Z]*)', text)  # mails
for i in result:
       with open(write_file, 'a') as f:
               f.write(i)
               f.write('\r\n')
