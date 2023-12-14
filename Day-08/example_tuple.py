
total_servers = ("serve-1", "server-2",  "server-3")
print(len(total_servers))

# how to create a  new TUPLE from the above tuple  

new_server_list = total_servers[0:1]  # this we create a new server tuple of  <server-1> only because the upper element is not always included in the count
print(new_server_list)

print(total_servers)