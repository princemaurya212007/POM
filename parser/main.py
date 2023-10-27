from fastapi import FastAPI
import xml.etree.ElementTree as ET

from User import User

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all-repo")
async def all_repo():
    try:
        user = User()
        repos = user.parse_all_repo()
    except Exception as e:
        return {"message": str(e)}
    return {"length": len(repos), "data": repos}


@app.get("/dependencies/{repo_name:path}")
async def dependencies(repo_name):
    try:
        user = User()
        dependencies = user.get_repo_dependency(repo_name, recusrive=True)
    except Exception as e:
        return {"message": str(e)}

    return {"length": len(dependencies), "data": dependencies}


@app.get("/one-file-dependencies/{repo_name:path}")
async def dependencies(repo_name):
    try:
        user = User()
        dependencies = user.get_repo_dependency(repo_name, recusrive=False)
    except Exception as e:
        return {"message": str(e)}

    return {"length": len(dependencies), "data": dependencies}
