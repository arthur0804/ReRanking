import requests
import pandas as pd


def getGeneMentions(id):
    resultlist = []
    url = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Gene/" + id + "/JSON/"
    result = requests.get(url).json()
    if(len(result) != 0):
        genelist = result[0]['denotations']
        if(len(genelist) != 0):
            for gene in genelist:
                resultlist.append(gene['obj'])
    # concatenate to string
    genes = "-".join(resultlist)
    return genes


def getDiseaseMentions(id):
    resultlist = []
    url = "https://www.ncbi.nlm.nih.gov/CBBresearch/Lu/Demo/RESTful/tmTool.cgi/Disease/" + id + "/JSON/"
    result = requests.get(url).json()
    if(len(result) != 0):
        diseaselist = result[0]['denotations']
        if(len(diseaselist) != 0):
            for disease in diseaselist:
                resultlist.append(disease['obj'])
    diseases = "-".join(resultlist)
    return diseases


df = pd.read_csv("/Users/arthur_0804/Desktop/testResult2.txt", header=None, sep="\t")
df.columns = ["TOPIC", "ID", "RANK", "SCORE", "TYPE"]


# list of all the document ids
idlist = list(set(df["ID"]))
print(len(idlist))
# dictionary of <document id; mentions>
genesdic = {}
diseasesdic = {}


for i in range(0, len(idlist)):
    genesdic[idlist[i]] = getGeneMentions(idlist[i])
    print("No. {} in list is done".format(i))

for i in range(0, len(idlist)):
    diseasesdic[idlist[i]] = getDiseaseMentions(idlist[i])
    print("No. {} in list is done".format(i))


len(genesdic)
len(diseasesdic)


df["GENE"] = df["ID"].map(genesdic)
df["DISEASE"] = df["ID"].map(diseasesdic)

df.to_csv("results_with_mentions.csv", index=False, header=True)
