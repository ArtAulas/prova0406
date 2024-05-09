#requests
from fastapi import FastAPI

app=FastAPI()

@app.get("/health-check")
def get_health():
    return {'status':'Saudável'}

if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)