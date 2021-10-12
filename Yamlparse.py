import yaml
yamlfile=open("yamlfile",'r')
yamlfiletest=yaml.load_all(yamlfile,Loader=yaml.FullLoader)
print(type(yamlfiletest))

for e in yamlfiletest:
    d=e['people']
    for dd in d:
        print(dd["id"])


