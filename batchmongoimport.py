#!/anaconda3/bin/python
# based on https://abstar.readthedocs.io/en/latest/api_examples.html


import os
from abstar.utils  import mongoimport

project = input("Project name: ")
project_dir = input("Directory to upload: ")

abstar_output = os.path.join(project_dir,'output') if project_dir != None else exit("Please supply a directory")
logs = os.path.join(project_dir, 'log/mongo.log')
mongo_args = mongoimport.Args(db=project, input=abstar_output, delim1='.', log=logs)

# import into MongoDB
mongoimport.run(ip=mongo_args.ip,
                port=mongo_args.port,
                user=mongo_args.user,
                password=mongo_args.password,
                input=mongo_args.input,
                log=mongo_args.log,
                db=mongo_args.db,
                delim1=mongo_args.delim1,
                delim2=mongo_args.delim2)