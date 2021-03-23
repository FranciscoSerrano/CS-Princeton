'''
“Modify useargument.py to compose a program usethree.py that 
takes three names and writes a proper sentence with the names 
in the reverse of the order they are given, so that, for example, 
python usethree.py Alice Bob Carol writes the string 
'Hi Carol, Bob, and Alice'.”
'''
import sys
name1 = sys.argv[1]
name2 = sys.argv[2]
name3 = sys.argv[3]
print(f"Hi, {name1}, {name2}, and {name3}" )