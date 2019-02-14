#!/usr/bin/env python
# coding: utf-8

# In[1]:


from SPARQLWrapper import SPARQLWrapper, JSON
def getDiseaseName(id):
    subject = """<""" + id + """>"""
    sparql = SPARQLWrapper("http://id.nlm.nih.gov/mesh/sparql")
    sparql.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX meshv: <http://id.nlm.nih.gov/mesh/vocab#>
        PREFIX mesh: <http://id.nlm.nih.gov/mesh/>
        PREFIX mesh2015: <http://id.nlm.nih.gov/mesh/2015/>
        PREFIX mesh2016: <http://id.nlm.nih.gov/mesh/2016/>
        PREFIX mesh2017: <http://id.nlm.nih.gov/mesh/2017/>
        PREFIX mesh2018: <http://id.nlm.nih.gov/mesh/2018/>
        PREFIX mesh2019: <http://id.nlm.nih.gov/mesh/2019/>
        SELECT DISTINCT ?s ?p ?o
        FROM <http://id.nlm.nih.gov/mesh>
        WHERE {""" + subject + """ <http://www.w3.org/2000/01/rdf-schema#label>  ?o.}""")
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    result = results["results"]["bindings"]
    if len(result) > 0:
        return result[0]["o"]["value"]
    else:
        return "None"


# In[2]:


inputpath = "/Users/arthur_0804/Desktop/RelDocsMentions/MentionsID/"
outputpath = "/Users/arthur_0804/Desktop/RelDocsMentions/MentionsLabel/"
for i in range(1,31):
    outputfile = open (outputpath + str(i) + ".txt", 'w')
    inputfile = inputpath + str(i)
    with open (inputfile, 'r') as f:
        for line in f:
            if(line[0:8] == 'Disease:'):
                Meshid = line[8:]
                Meshid = Meshid.strip()
                Query = "http://id.nlm.nih.gov/mesh/" + Meshid
                Disease = getDiseaseName(Query)
                outputfile.write(Disease + "\n")
    print("Topic No.{} is done".format(i))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




