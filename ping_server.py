import subprocess
#read the server names
hostfile = open('servername.txt','r')
#list for holding the servers
listofserver = []
for lines in hostfile:
    ph = lines.rstrip()
    #removes the new line character at the end
    listofserver.append(ph)
#append to myfile
myfile = open('newfile.txt',"a+")
n = len(listofserver)
timestamp = subprocess.Popen(["date"],stdout=subprocess.PIPE).communicate()[0]
myfile.writelines(timestamp)
for i in range(n):
    pingout = subprocess.Popen(["ping","-c","20", listofserver[i]], stdout= subprocess.PIPE).communicate()[0]
    traceroute = subprocess.Popen(["traceroute",listofserver[i]], stdout=subprocess.PIPE).communicate()[0]
    myfile.writelines(pingout)
    myfile.writelines(traceroute)
myfile.close()
hostfile.close()