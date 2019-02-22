import os
import subprocess
import numpy as np

proc = subprocess.Popen('ls ../../ECEN403/library', shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err = proc.communicate()

pdf_names = out.decode("utf-8").split('.pdf\n')[0:-1]
#print(pdf_names)

file_path = os.path.dirname(__file__)
if file_path != "":
  os.chdir(file_path) 
print(os.getcwd())   

np.savetxt("file_names.csv", pdf_names, delimiter=",", fmt='%s')
np.savetxt(os.getcwd()+"/expertfinder/file_names.csv", pdf_names, delimiter=",", fmt='%s')


'''
import csv

your_list = []
with open('file_names.csv', 'r') as f:
    reader = csv.reader(f)
    for stuff in reader:
      your_list.append(stuff[0])

print(your_list)

'''