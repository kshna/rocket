import yaml
def yamlObj():
    with open("commands.yml") as f:
        s=yaml.load(f,Loader=yaml.FullLoader)
    return s
