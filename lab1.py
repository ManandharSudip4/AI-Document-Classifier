import os 
import shutil 
# os.mkdir('AI')
# os.mkdir('WEB')
for file in os.listdir(os.getcwd()):
    if file.endswith("_AI.pdf"):
        shutil.copy(file,'AI/'+file)
    elif file.endswith('_WEB.pdf'):
        shutil.copy(file,'WEB/'+file)

for file in os.listdir(os.getcwd()):
    if file.endswith(".pdf"):
        os.remove(file)