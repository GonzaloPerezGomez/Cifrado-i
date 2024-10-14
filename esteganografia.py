import subprocess, sys

i = 1
target_hash = "e5ed313192776744b9b93b1320b5e268"

while i <= 46:
    subprocess.run(f"md5sum imagen/imagen{i}.jpg | grep {target_hash}", shell=True)
    i+=1


subprocess.run("stegosuite extract -d -k  imagen/imagen22.jpg", shell=True)