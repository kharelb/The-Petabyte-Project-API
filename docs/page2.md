# Tutorial On API Usage And CRUD Operations
 This is a guide to interact with the TPP database using the
 API, enabling you to create new records, retrieve existing data, 
 update information, and delete unnecessary entries through step-by-step instructions.

### Make Necessary Import And Check API Status
```python
import requests

# To check if the API is up and running:
x = requests.get("http://ipaddress:port/")
print(x.text)

Output: {"message":"Welcome to the TPP Database API."}

```

### Inserting Data Into The Database
To perform insertions in the database, you need to define a Python dictionary that
represents the data you want to insert. It is crucial to ensure that you have 
the correct endpoint for the target collection in the database, and remember that 
endpoints in database are case-sensitive. The basic syntax is as follows:
```python
# Output may vary slightly from what is shown below.
x = requests.post("http://ipaddress:port/endpoint", json=dictionary_file, headers=headers_file)
print(x.json())
Output: {'message': 'Data added successfully', 'inserted_id': ['64aec5d5debe5c9809620978']}
```

### Retrieving Data From The Database
The items from a collection in the database can be obtained in different ways. 
I am starting here from the basic one:

- #### Simply get documents from a collection:
```python
# The print statement should give a list of dictionaries. 
x = requests.get("http://ipaddress:port/endpoint", headers=headers_file)
print(x.json())

# The above method gives you maximum of 10 documents.
# You can use skip and limit after the endpoint to get required number of documents skipping certain number of items.
x = requests.get("http://ipaddress:port/endpoint/?skip=0&limit=5", headers=headers_file)
print(x.json())
```

- #### Get the latest inserted document (Currently only supports pipeline_versions collection)
```python
x = requests.get("http://ipaddress:port/endpoint/latest", headers=headers_file)   # endpoint supported now is "pipeline_versions" 
print(x.json())
```

- #### Retrieve documents using ids
```python
# Syntax
x = requests.get("http://ipaddress:port/endpoint/document_id", headers=headers_file)

# Example
x = requests.get("http://ipaddress:port/endpoint/649a102534e36cac90953ac3", headers=headers_file)

# You can print and see the document if you wish to:
print(x.json())

```

- #### Retrieve documents by passing a query dictionary
```python
# Syntax:
x = requests.get("http://ipaddress:port/endpoint/search_data", json=query_dictionary, headers=headers_file)

# You can pass in any number of key-value pairs in the query dictionary but remember it is logical 'AND' operation.

# Example:
x = requests.get("http://localhost:8000/data/search_data", json={"obs_length": 1}, headers=headers)

print(x.json())
```

- #### Retrieve documents by passing more complex queries
  You can also pass complex queries like less than, greater than etc. in the query dictionary.

```python
# Syntax is same as before:
x = requests.get("http://ipaddress:port/endpoint/search_data", json=query_dictionary, headers=headers_file)

# Query dictionary should be modified accordingly:
# Examples of  query dictionaries are as follows:
query_1 = {"obs_length": {"$gte":2, "$lte":50}}
query_2 = {"obs_length": {"$gte":100, "$lte":4000}, "ra_j":{"$gte":0, "$lte":202}}


# lt --> less than, lte --> less than or equals to
# gt --> greater than, gte --> greater than or equals to
```

- #### Retrieve documents based on the queries in embedded documents
  If you have a dictionary nested inside another dictionary and want to access 
  documents based on the values of the nested dictionary, you can utilize this technique.
```python
# Syntax is similar to previous one just need to change the query dictionary
x = requests.get("http://ipaddress:port/endpoint/search_data", json=query_dictionary, headers=headers_file)

# For example consider "candidate_results" collection and the document structure is as follows:
# candidte_results = {....., "interesting_info":{"is_interesting":True, "submitting_user":"username"},....}
# If you want to get all the documents from candidate_results with "is_interesting"=True then define query dictionary as follows:
query_dictionary = {"interesting_info.is_interesting":True}

# Now pass this dictionary like this:
x = requests.get("http://ipaddress:port/candidate_results/search_data", json=query_dictionary, headers=headers_file)
```

### Updating Documents

You have two options for updating documents in a collection: the `patch` method
and the `put` method. Although these methods can be used interchangeably, it is
recommended to use `patch` when updating specific fields and `put` when updating
all fields in a document. 
```python
x = requests.patch("http://ipaddress:port/endpoint/id", json={"field": "new_value"})

# Example:
x = requests.patch("http://ipaddress:port/candidate_results/64aee5b616479f801052fc27",
                   json={"fetch_score":0.9}, headers=headers )
```

### Deleting Documents
You will need to have document id for deleting it.
```python
# Syntax
x = requests.delete("http://ipaddress:port/endpoint/id")
```

[__Home Page__](README.md)  |   [__Previous Page__](page1.md) | [__Next Page__](page3.md)
