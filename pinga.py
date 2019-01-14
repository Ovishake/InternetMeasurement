import subprocess
file_name = open("filename.dat","r")
for line in file_name:
    f = line.split(",")
#splitted lines
print(f[1])

test = subprocess.call(["ping","-c","20",f[1]],stdout=subprocess.PIPE);

print(test)