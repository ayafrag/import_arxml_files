# import_arxml_files
### This is the previous code 

import xmltodict
import json
import yaml
import argparse

class import_configuration_tool:
    def _init_(self):
            pass
            
    def __json_write(self,json_path,data):
         with open(json_path,'w', encoding='utf8') as fb:
            json_data= json.dumps(data, indent=4, ensure_ascii=False)
            fb.write(json_data)
            
    def __json_read(self,json_data):
        with open (json_data ,'r') as json_f:
                file_data=json.load(json_f)
        return file_data          
        
    def __yaml_write(self,yaml_path,data):
        with open(yaml_path,'w') as yf:
            yaml.dump(data, yf,default_flow_style=False)
            
    def extract_arxml_data_to_dict(self,arxml_path):
        xml_content = open(arxml_path).read()
        my_ordered_dict=xmltodict.parse(xml_content)
        return my_ordered_dict
        
    def convert_dict_to_json(self,json_path,data):
         self.__json_write(json_path,data)
         
    def convert_json_to_syml(self,json_data,yaml_path):
            file_data=self.__json_read(json_data)
            self.__yaml_write(yaml_path,file_data)
            
            
def main():

     parser=argparse.ArgumentParser(description="A script that imports data from arxml files and converts them to json files")
     parser.add_argument("arxml_path", type=str, help="The path to the arxml file")
     parser.add_argument("json_path", type=str, help="The path to the json file")
     parser.add_argument("yaml_path", type=str, help="The path to the yaml file")
     
     args=parser.parse_args()
     my_tool = import_configuration_tool()
     my_dict = my_tool.extract_arxml_data_to_dict(args.arxml_path)
     my_tool.convert_dict_to_json(args.json_path, my_dict)
     my_tool.convert_json_to_syml(args.json_path,args.yaml_path)
     
if __name__ == "__main__":
    main()
    
### in this code there were some problems about the code to be more flexible, scalable, maintainable, and reusable code.
### but I apply the SOLID Principles to get it more flexible , scalable , maintainable and reusable 
### I apply 
### 1- Single-responsibility principle (SRP) :
### This means that a class should have only one responsibility, as expressed through its methods. If a class takes care of more than one task, then you should separate those tasks into separate classes.
### A class should have only one reason to change.
### I made every class have a single repposabilty 
### 2- Open_Closed Principle : Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
### made my code open to be extended and closed for modification by writing every Method doing different reposability alone using 

 from abc import ABC, abstractmethod

class class_name(ABC):
    @abstractmethod
    def function_name(self,given_args):
        pass
        
### 3- Liskov Substitution Principle (LSP):
### • According to this principle, The objects of a superclass should be replaceable with objects of its subclasses which should not break the original program.
### • Derived classes should be able to be used in place of their base classes without causing any unexpected behavior or violating the expected contracts.
### • Ensures that polymorphism is correctly implemented and helps maintain the behavior and consistency of the code.

### 4- Dependency Inversion Principle (DIP):
### • High-level modules should not depend on low-level modules. Both should depend on abstractions.
### • Abstractions should not depend on details; details should depend on abstractions.
### • Encourages the use of dependency injection and inversion of control to reduce direct dependencies between modules and promote modular and testable code.
