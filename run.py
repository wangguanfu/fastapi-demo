from typing import Optional

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from tutorial import app03, app04

app = FastAPI()

app.mount(path='/static', app=StaticFiles(directory='./coronavirus/static'),
          name='static')  # .mount()不要在分路由APIRouter().mount()调用，模板会报错

app.include_router(app03, prefix='/demo3')
app.include_router(app04, prefix='/demo4')

if __name__ == '__main__':
    uvicorn.run('run:app', host='127.0.0.1', port=8001, reload=True, debug=True)
