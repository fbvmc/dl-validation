# dl-validation
Digital libraries data-quality evaluation


### Criterion population completeness
This SPARQL query retrieves 2500 writers of poetry and plays from [Wikidata](http://tinyurl.com/y6xtdlvd). Then, the [python script](population-ids.py) generates a ramdon list of authors which has been used for the criterion population completeness.  

```
SELECT DISTINCT ?s ?sLabel
WHERE {
    ?s wdt:P31 wd:Q5.
    ?s wdt:P106 wd:Q49757.
    ?s wdt:P106 wd:Q214917.
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "es" .
    }
}
LIMIT 2500
```


### Criterion syntactic validity of RDF documents

SPARQL query to retrieve a list of authors from the [Biblioteca Virtual Miguel de Cervantes](http://data.cervantesvirtual.com).
Then, the [python script](bvmc-ids.py) generates a ramdon list of authors which has been used for this criterion.  

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdac: <http://rdaregistry.info/Elements/c/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?s ?viafid WHERE {
?s rdf:type rdac:Person.
?s owl:sameAs ?viafid.
FILTER(regex(str(?viafid), "viaf" ) )
}
LIMIT 20000
```


SPARQL query to retrieve a list of authors from the [Bibliothèque nationale de France](http://data.bnf.fr). Then, the [python script](bnf-ids.py) generates a ramdon list of authors which has been used for this criterion.  
```
SELECT DISTINCT ?s ?viafid
WHERE { ?s a foaf:Person .
?s owl:sameAs ?viafid.
FILTER(regex(str(?viafid), "viaf" ) )
}
LIMIT 100000
```

SPARQL query to retrieve a list of authors from the [Biblioteca Nacional de España](http://datos.bne.es). Then, the [python script](bne-ids.py) generates a ramdon list of authors which has been used for this criterion.  
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix ns2: <http://datos.bne.es/def/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT distinct ?s ?viafid WHERE {
?s rdf:type ns2:C1005.
?s owl:sameAs ?viafid.
FILTER(regex(str(?viafid), "viaf" ) )
}
LIMIT 100000
```

SPARQL query to retrieve a list of authors from the [British National Bibliography](http://bnb.data.bl.uk/). Then, the [python script](bnb-ids.py) generates a ramdon list of authors which has been used for this criterion.  
```
PREFIX bio: <http://purl.org/vocab/bio/0.1/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?viaf ?author WHERE {
    ?event a bio:Birth.
    ?author bio:event ?event.
    ?author owl:sameAs ?viaf.
}

LIMIT 100000
```
