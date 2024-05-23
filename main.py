#requests
from fastapi import FastAPI
from routes_usuario import router as router1

app=FastAPI()

@app.get("/helloworld")
def helloworld():
    return 'Hello World'

app.include_router(router1)

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)