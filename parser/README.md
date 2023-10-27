## Parser

The dependencies parser of `pom.xml` is being built using the **FastAPI** library of Python

### Getting started

1. Install the dependencies by running the following command

```
pip install -r requirements.txt
```

2. Update the environment variables by editing `.env` file as follows

```
GITHUB_TOKEN=<github-token>
```

Replace the `<github-token>` with the your github token to authorize the API requests

3. Run the following command to start the FastAPI server

```
uvicorn main:app --reload
```

4. The server will start on `http://localhost:8000`. Open your browser and enter `http://localhost:8000/docs` to access all the apis available.

**Note**:
Fetching all the `pom.xml` files from a repo may take a long time depending on the size of the repository and level of nesting of the files. That's why along with getting dependencies of all the files in the repo I also created a route that will return dependencies of only first file i.e. the top `pom.xml` file in the repo

### Rotues

- `/all-repo`: It will return all the repositories a user have.

  - [Sample response](./responses/all-repo.json) <!-- Few repo has beed removed from responses -->

- `/dependencies/{repo_name:path}`: It will return all the dependencies in all the `pom.xml` files that is present in the specified repository

  - [Sample Response](./responses/dependencies.json)

- `one-file-dependencies/{repo_name:path}`: It will give the dependencies of only one file which will be hitted first in nested search.
  - [Sample Response](./responses/one-file-dependencies.json)

**Note**: Please note that the repository name will be the full name along with user username, i.e. `<github-username>/<repository-name>` For example:
**repo_name: shopizer-ecommerce/shopizer**

### Response format of dependencies

```
{
  "length": <number of pom.xml files>,
  data:{
    "filepath": {
      "download_url": "https://github.com/",
      "dependencies":{
        "groupId":[
            {
              "artifactId":"artifactId",
              "version":"version" // if version is not specified then "Version not found" will be returned
            }
          ]
      }
    }

  }
}

```

Sample responses are present in the `/responses` folder
