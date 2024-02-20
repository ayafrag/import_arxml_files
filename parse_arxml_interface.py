from abc import ABC, abstractmethod


class json_write(ABC):
    @abstractmethod
    def write_json_file(self,json_path,data):
        pass
class json_read(ABC):
    @abstractmethod
    def read_json_file(self,json_data):
        pass
class yaml_write(ABC):
    @abstractmethod
    def write_yaml_file(self,yaml_path,data):
        pass