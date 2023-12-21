
#TASK ( demo )
#> Update sever.conf file  when  < maximum connection = 200  Thjen write a python script to update the server.conf file and update the < max connection from 200 to 500 



# OUTLINE

#>1  Read the file
#>2  Store all the line in the file in a var/list
#3 open the file in <write> mode
#4 Then update the maximun connection line

#=====================================>>





def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()

    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)

update_server_config("server.conf", "MAX_CONNECTIONS", "500")
