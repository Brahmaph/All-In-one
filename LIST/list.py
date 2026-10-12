servers = ["server1", "server2", "server3"]

#print list
print(servers)

#accessing List elements
print(servers[0])
print(servers[1])

#Adding a server
servers.append("Server4")
print(servers)

#Inserting a server
servers.insert(1,"BackupServer")
print(servers)

#Removing a server
servers.remove("server2")
print(servers)

#Updating s server name
servers[0] = "MainServer"
print(servers)

#Loop Through the list
for server in servers:
    print(server)

#Length of the List
print(len(servers))

#Reverse
servers.reverse()
print(servers)

#sort
a = [2,3,1,4,5,6]
a.sort()
print(a)

#example

ex = ["Web","Db","Mail"]

ex.append("DNS")
ex.remove("Mail")

print("Server List")
for i in ex:
    print(i)