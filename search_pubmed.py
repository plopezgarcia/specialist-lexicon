'''
Created on 4 jun. 2019

@author: plubeda
'''

from Bio import Entrez
from pprint import pprint
import json
import os
from urllib.error import HTTPError
import pandas as pd

def search(query):
  Entrez.email = 'email@email.es'
  handle = Entrez.esearch(db='pubmed', 
                          sort='relevance', 
                          retmax='100000',
                          retmode='xml', 
                          term=query)
  
  results = Entrez.read(handle)
  return results

def fetch_abstract(pmid):
  handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
  xml_data = Entrez.read(handle)
  try:
      json_data = json.dumps(xml_data)
      return json_data
  
  except IndexError:
      return None

def donwload_files(specialty, query):
            
  specialty = specialty.lower()
  specialty = specialty.replace(" ", '-')
  
  results = search(query)

  id_list = results['IdList']
  
  path = '/home/plubeda/git_repo/specialist-lexicon/pubmed_files/'
  try:
      # Create target Directory
      os.mkdir(path + specialty)
  
  except FileExistsError:
      print("Existe la carpeta")
      pass
  
  for index, pmid in enumerate(id_list):
    
    # if not exists
    if not os.path.isfile(os.path.join(path, specialty, pmid)):
        
        try:
            json_data = fetch_abstract(pmid)
            
            print("[", index , "/", len(id_list) , "] Creamos fichero: ", pmid) 

            with open(os.path.join(path, specialty, pmid), 'w') as outfile:  
                json.dump(json_data, outfile)

        except HTTPError:
            print("except HTTP Error")
            pass 

def search_specialties(mesh_specialties, mesh_seealso):
  for index, specialty in mesh_specialties.iterrows():
    call_failed = True
    
    while(call_failed):
        try:
            specialty_descriptor = specialty['descriptor']
            specialty_name_en = specialty['label']
            specialty_name_spa = specialty['labelSpa']
            
            #Journal [TA] 
            #Affiliation [AD]
            #Text Words[TW]
            
            query_direct_spa = "SPA[LA] AND "

            # english mesh
            query_direct_spa += "(" + specialty_name_en + "[TA] OR " + specialty_name_en + "[TW] OR " + specialty_name_en + "[AD] OR "

            # spanish mesh
            query_direct_spa +=  specialty_name_spa + "[TA] OR " + specialty_name_spa + "[TW] OR " + specialty_name_spa + "[AD] OR "
            
            # see also mesh (solo en español porque buscamos en MH y no se encuentan en español en pubmed)
            data_seealso = mesh_seealso.loc[mesh_seealso['descriptor'] == specialty_descriptor]

            for seeAlso in data_seealso['seeAlso'].tolist():
              query_direct_spa += seeAlso + "[MH] OR "

            query_direct_spa = query_direct_spa[:-4]
            query_direct_spa += ")"


            print(specialty_name_en, '->', query_direct_spa, '\n\n')

            donwload_files(specialty_name_en, query_direct_spa)

            call_failed = False
        except:
            print("-------------------------------->FAILED, repeating!!!")


if __name__ == '__main__':
  mesh_specialties = pd.read_csv("/home/plubeda/git_repo/specialist-lexicon/mesh-specialties-spa.csv")
  
  mesh_seealso = pd.read_csv("/home/plubeda/git_repo/specialist-lexicon/mesh-specialties-seealso.csv")
  
  search_specialties(mesh_specialties, mesh_seealso)
  
  
    
                
        
