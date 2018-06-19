from os.path import exists

index_stamp = 3
max_index = 999
title = '/home/staff/asukeshkall/Downloads/Test/run_calc'
#ext = 'txt'

while index_stamp <= max_index:
    unique_filename = '%s-%03d' % (title, index_stamp)
    if exists(unique_filename):
       index_stamp += 1
       continue
    f = open(unique_filename, 'wt')
    f.write("Data")
    f.close()
    break

if index_stamp > max_index:
   print("Could not create a unique filename")
else:
   print("Created a unique file:",unique_filename)
