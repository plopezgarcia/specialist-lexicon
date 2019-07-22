# specialist-lexicon

1. [01_generate_queries]

    1.1 [01_generate_total_queries.ipynb]: Script para generar las queries a partir de los DataFrames creados anteriormente (mesh-specialties-spa.csv, mesh-specialties-seealso.csv, mesh-specialties.csv)
    
    1.2 [total_queries.txt] : fichero con las queries generadas
    
2. [02_download_pubmed]: 
 
    2.1 [01_search_pubmed.ipynb]: Script para buscar en pubmed
    
    2.2 [02_count_files_xml.ipynb]: Script para contar el nº de documentos descargados
    
    2.3 [03_join_specialties.ipynb]: Script para juntar varios XMLs y tener una lectura correcta
    
    2.3 [total_queries.txt] : fichero con las queries generadas
    
    2.4 [estadísticas_especialidades_ndocs.ods]: fichero csv con estadísticas de nº de documentos, etc.
    
  
3. [03_treatment_text]:

    3.1 [01_create_dataframe_from_xml.ipynb]: Crea un dataframe por cada especialidad y lo almacena dentro de la carpeta dataframes.
    
    3.2 [02_create_xgrams.ipynb]: Script para crear una estructura más legible (diccionario) que incluye todas las especialidades y términos (1 -5 gramas)
    
    3.3 [03_obtain_term_weight.ipynb]: Script que crear un fichero csv en la carpeta term_weight por cada especialidad con los pesos de términos (nº de ocurrencias, idf, etc).
    
    3.4 [04_create_model_language.ipynb]: Pruebas de language model (borrar)
    
    3.5 [04_evaluate_model_language.ipynb.ipynb]: Pruebas de language model (borrar)
    
    3.6 [models_languages]: Pruebas de language model (borrar)
    
    3.7 [idfiles_by_specialty.txt]: fichero que contiene la especilidad y una lista con los ids de ficheros incluidos.
    
    3.8 [len_titles.txt]: fichero que contiene el id de un fichero y el nº de tokens del título
    
    3.9 [vocabulary.txt]: fichero de texto que contiene el vocabulario del corpus
    
    
4. [04_language_model]:
    
    Pruebas de language model

5. [generate-queries.ipynb] -> prueba de generar queries (borrar)

6. [mesh-specialties-seealso.csv]: Dataframe que contiene las especialidades y sus seeAlso de MeSH

7. [mesh-specialties-spa.csv]: Dataframe que contiene las especialidades y sus traducciones al español usando UMLS

8. [mesh-specialties.csv]: Dataframe que contiene la información de las especialidades de MeSH

9. [queries.csv] -> (borrar)
