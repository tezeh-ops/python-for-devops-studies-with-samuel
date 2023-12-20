
# Making use of Dictionary

student_info = {
    "name": "samuel",
    "age" :  "25",
    "class": "DevOps"
}



# let try to see if we can do waht we just did above using List:

# student_info = ["abi", "13", "11"]     # we can see thtat wit list is not clera if what blomgs to what But with Dictionary with Key:value pair it make it clear to understand


print(student_info["name"])


#==========================================

# Example 2  Let see how we can store or write a dictionary  in a LIST

ec2_instance_info = [                # declaring our list
    {                              # Declaring our Dictionary with {}
        "id": "instnce-001",         # And we most separate each line with a <, >      
        "type": "t2.micro"
    },

    {
        "id": "instnce-002",
        "type": "t2.medium"
    },

    {
        "id": "instnce-003",
        "type": "t2.xlarge"
    }
]

# let say some ask you to give him the 2 instance type:

print(ec2_instance_info[1]["type"])   # so here we are callint the Second Ec2 instance type == < t2.medium > 

