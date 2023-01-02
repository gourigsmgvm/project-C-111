import os
import shutil
from_dir= "E:/assets"
to_dir = "E:/test"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for filename in list_of_files:
   name, extension = os.path.splitext(filename)
   print(name , ",", extension)

   if extension in [".txt", ".doc", ".docx", ".pdf", ".pptx"]:
        src = "E:/assets/" +filename

        dest = "E:/test/" + filename 

        shutil.move(src,dest)

   
