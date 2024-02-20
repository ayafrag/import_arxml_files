import parse_arxml_implementation
import argparse


def arg_parse():
     parser=argparse.ArgumentParser(description="A script that imports data from arxml files and converts them to json files")
     parser.add_argument("arxml_path", type=str, help="The path to the arxml file")
     parser.add_argument("json_path", type=str, help="The path to the json file")
     parser.add_argument("yaml_path", type=str, help="The path to the yaml file")

     args=parser.parse_args()
     return args



     

def main():
     
     arg_ret =arg_parse()
     arxml_file=parse_arxml_implementation.Parsing_Arxml_files()
     json_file =parse_arxml_implementation.get_json_file()
     yaml_file =parse_arxml_implementation.get_yaml()

     my_arxml_file=arxml_file.extract_arxml_data_to_dict(arg_ret.arxml_path)
     json_file.write_json_file(arg_ret.json_path, my_arxml_file)
     yaml_file.yaml_output(arg_ret.json_path,arg_ret.yaml_path)
    



if __name__ == "__main__":

    main()
