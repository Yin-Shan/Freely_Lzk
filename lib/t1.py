import configparser
import os
project_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
cfgpath = os.path.join(project_path,"conf","account.ini")

for file in os.listdir(project_path):
    print(file)
#print(os.listdir(project_path))
