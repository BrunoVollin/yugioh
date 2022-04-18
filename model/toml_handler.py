import toml

class TomlHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_toml(self):
        with open(self.file_name, 'r', encoding="utf-8") as f:
            return toml.load(f)

    def write_toml(self, data):
        with open(self.file_name, 'w', encoding="utf-8") as f:
            toml.dump(data, f)

    def append_toml(self, data):
        with open(self.file_name, 'a', encoding="utf-8") as f:
            toml.dump(data, f)
            
    def append_toml_string(self, data):
        with open(self.file_name, 'a', encoding="utf-8") as f:
            f.write(data)
    
    def delete_toml(self):
        with open(self.file_name, 'w', encoding="utf-8") as f:
            f.truncate()
