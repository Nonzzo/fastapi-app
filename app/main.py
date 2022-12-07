from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

print(settings.database_username)
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["https://www.google.com", "https://www.youtube.com"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}








#to activate your virtual environment: navigate to your interpreter ./venv/bin/python 
# source venv/bin/activate    

# to get pip install psycopg2 to work in mac osx run the command:
# export PATH=$PATH:/Library/PostgreSQL/14/bin






