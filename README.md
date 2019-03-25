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
