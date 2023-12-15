

import os   # module to list file [NB in <OS module  it has and in build module call <listdir> that is y we are using <OS>]

folders =  input("please provid list of folder names with space in between: ").split()  # herewe are aking the use to put in the fole name/path and we use < .split > so separate the folders

# Write our For Loop  for the forder we will recieve from the user
for folder in folders:
    try:                          # to perform exceptional handeling 
        files = os.listdir(folder)  # here we are listing the files in any given folder
    except FileNotFoundError:    # here  we are passing the kind of ERROR we want to Accept
        print("please provid a valid folder name, looks like this folde does not exist:" " " + folder ) # the meassage we want to pass if the folder input is not Found or it wrong and we name the folder
        break                                    # we cab stop the program here by using <break> statement
# Let say may the the user do not have permission to the folder ab=nd we want to still move ahead and send a message and the folder in question:
    except PermissionError:
        print("No access tio this folder - " + folder)

    print(" ===== listing  files for the folder - " + folder)  # this will print out the meassage and pointing with folder it refering to
    # Writing another loop that will put all the in order NOT putting them in the form of a list

    for file in files:
        print(file)

# Next we see how to d exceptional handeling of ERRORS ( so should in case the user input a wrong FOLDER or FOLDER that does not Exit ) the 
# The program should move over to other folder given by the users an d run it as without braking and it should give the use a propal ERROR message
# And  for theat we will be using < try > & <except > as seen abave .
    
