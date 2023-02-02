import subprocess
with open("output.txt","w") as f:
    subprocess.check_call(["desktop","76_file.py"],stdout=f)            
