from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse , Response

app = FastAPI()

class Numbers(BaseModel):
    values : list[int]

@app.get('/hello')
def hello():
    return {'message':'sam'}

@app.post('/plot_it')
def plot(data : Numbers):
    try :
        #buf = BytesIO()
        #plt.savefig(buf, format="png")
        #plt.close()
        #buf.seek(0)
            
        return {"max_value":max(data.values)}
    except Exception as e :
        raise ValueError("There is no ")

