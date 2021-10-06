import yaml
  # resolve to get rid of any symlinks

def read_config(config_path):
    with open(config_path) as config_file:
        content= yaml.safe_load(config_file)
    return content
