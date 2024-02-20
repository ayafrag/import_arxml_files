import parse_arxml_interface
import xmltodict
import json
import yaml

class Parsing_Arxml_files:
    def extract_arxml_data_to_dict(self,arxml_path):
        xml_content = open(arxml_path).read()
        my_ordered_dict=xmltodict.parse(xml_content)
        return my_ordered_dict
    
class get_json_file(parse_arxml_interface.json_write):
     def write_json_file(self,json_path,data):
         with open(json_path,'w', encoding='utf8') as fb:
            json_data= json.dumps(data, indent=4, ensure_ascii=False)
            fb.write(json_data)

class get_yaml(parse_arxml_interface.json_read,parse_arxml_interface.yaml_write):
    def read_json_file(self,json_data):
        with open (json_data ,'r') as json_f:
                file_data=json.load(json_f)
        return file_data
    def write_yaml_file(self ,yaml_path,data):
        with open(yaml_path,'w') as yf:
            yaml.dump(data, yf,default_flow_style=False)

    def yaml_output(self,json_data,yaml_path):
         file_data=self.read_json_file(json_data)
         self.write_yaml_file(yaml_path,file_data)