import configparser
 
class ConfigReader:
    def __init__(self, config_file_path='src/configurations/config.ini'):
        self.path= config_file_path
        self.config_value= configparser.ConfigParser()
        self.config_value.optionxform = str
        self.config_value.read(config_file_path)
        self.list_sections  = self.config_value.sections()


    def get(self, section):
        try:
            if section not in self.list_sections:
                return(False,"section not found")
            # else:
                # print("found section in config file.")
            #  create dictionary of all the values and parse it to the code
            dict_new = {}
            for key_config in self.config_value[section]:
                dict_new[key_config] = self.config_value[section][key_config]
            #  return fetched values in the code
            return(True, dict_new)
        except Exception as e:
            return (False,"Reason : {}".format(str(e)))
        
