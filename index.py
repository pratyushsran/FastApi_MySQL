from fastapi import FastAPI
from routes.index import user

app = FastAPI()

# Include the router
app.include_router(user)
