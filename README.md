# Code Test Machine Learning Engineer

This is a code test for the Machine Learning Engineer position. 

The code test is a REST API built with Python and Flask. This API receives a list of Spanish sentences and returns a list of the named entities identified in each sentence.

## Installation

#### Python Versions Needed
- Python: 3.11.4 or sup.
- Pip: 23.1.2 or sup

To install and use the API you should copy the requirements located at `requirements.txt` file.
To this we need to create a directory where we want to alocate the sourcecode.
Once the directory is created we should clone this repo.

```bash
git clone https://github.com/DavettoMX/CodeTestMachineLearningEngineer.git
```

Once the repo has been cloned we open the directory that was created and now open a new terminal in the route of the repository.
Inside the terminal we type the command

```bash
pip install -r requirements.txt
```

Once the requirements are installed we can launch our application by running the `run.py` file

```bash
python run.py
```

The application will start running in the port `4000`.
If for any reason you need to change the port. You need to go to `run.py` file and change the port:

```python
    app.run(debug=True, host='0.0.0.0', port=desired_port)
```

## Usinge the API
Once our app is running, its time to use Postman or the tool of your preference to test the API.

The API has only one endpoint that is `/ner` and it only accepts POST requests. The complete URL is `http://127.0.0.1:4000/api/v1/ner`.

The API expects a JSON object with the following structure:

```json
{
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera.",
        "En Nueva York se encuentra la estatua de la libertad",
        "Samsung es la competencia directa de Apple"
    ]
}
```

Where the key `oraciones` is a list of strings that contains the sentences that we want to analyze.
REMINDER: The API only works with Spanish sentences.

The expected output for this example is:

```json
{
    "resultado": [
        {
            "entidades": {
                "Apple": "ORG",
                "Reino Unido": "LOC"
            },
            "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."
        },
        {
            "entidades": {
                "San Francisco": "LOC"
            },
            "oración": "San Francisco considera prohibir los robots de entrega en la acera."
        },
        {
            "entidades": {
                "Nueva York": "LOC"
            },
            "oración": "En Nueva York se encuentra la estatua de la libertad"
        },
        {
            "entidades": {
                "Apple": "ORG",
                "Samsung": "ORG"
            },
            "oración": "Samsung es la competencia directa de Apple"
        }
    ]
}
```

## API Testing

For test the API you can use the test case in

```
app/test/ner_api_test.py
```

Here is a unit testing file were you can test the output by console.

Feel free to add more test cases if you want.

***The test cases are just think for the main purpouse of the API and cannot cover
all posible cases.***