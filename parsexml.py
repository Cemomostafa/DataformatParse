import xml.etree.ElementTree as ET


stream=open('Catalog','r',encoding='utf8')
testxmlfile=ET.parse(stream)
root=testxmlfile.getroot()
for r in root.iter("year"):

    #print(ET.tostring(r).decode('utf8'))
    print(r.tag,r.attrib,r.text)

for movie in root.findall("./genre/decade/movie/[year='1992']"):# will search the file and print only the movies attribute in year 1992
    print(movie.attrib["title"])

for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):# will search the file and print only the format attribute with yes
    print(movie.attrib)

for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):# will search the file and print only the movies attribute with format attribute with yes
    #to return to parent use ...
    print(movie.attrib)
    #to modify the attribute


for movie in root.findall("./genre/decade/movie[ @ title = 'Back 2 the Future']"):
    movie.attrib['title']="Back to the Future"
    print (movie.attrib['title'])
    testxmlfile.write("Catalog")