import xmltodict

stream = open('Catalog', 'r', encoding="utf8").read()
xmln = xmltodict.parse(stream)["collection"]#["genre"]
for test in xmln['genre'] :
    print (test["decade"])

# for ob in xmln["movie"]:  # [0]["decade"][0]['movie'][0]["year"]:
#      print(ob)

