import pandas as pd 

# lower ,upper , replace ,spilt  ,contain : 

data = pd.DataFrame({
    "email" :[
        "ram@gmail.com",
        "ABC@yahoo.com",
        "xyz@gmail.com",
        "Jayshah345@gmail.com",
    ] 
        
})

# print(data)

data["lower_email"] = data['email'].str.lower()
# print(data)

data["upper_email"] = data['email'].str.upper()
# print(data)

print(data['email'].str.contains("@yahoo.com"))

# spilt  : username , domain 

data[['username','domain']] =data['email'].str.split("@",expand=True)
# print(data)  

# replace : 
data["replace_yahoo"]=data['email'].str.replace('@yahoo.com','@gmail.com')
print(data)

# datetime  : 


