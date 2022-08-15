import yaml
def yamlObj():
    with open("config/commands.yml") as f:
        s=yaml.load(f,Loader=yaml.FullLoader)
    return s
