""" importing package """
import os
import configparser

env = os.environ["active-profile"]


def get_config(section):
    """Reading config file and return based on section"""
    # create a parser
    parser = configparser.ConfigParser()
    config_file_name = "config/config-" + env + ".conf"
    print(f"Active : {env}")
    # read config file
    parser.read(config_file_name)
    # get section
    config_param = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_param[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} not found in the {1} file".format(section, config_file_name)
        )

    return config_param
