#requests
from fastapi import FastAPI

app=FastAPI()

@app.get("/helloworld")
def helloworld():
    return 'Hello World'

if __name__=='__main__':
    import uvicorn
    uvicorn.run("routes_fastapi:app", host="127.0.0.1", port=8003, reload=True)