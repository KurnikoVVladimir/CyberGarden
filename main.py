import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel



class Dogs(BaseModel):
    name: str
    age: float
    species: str
    price:float

class Cats(BaseModel):
    name: str
    age: float
    species: str
    price: float

bd_dog = []
bd_cat = []

app = FastAPI(title='Keber_PES')
router = APIRouter()

@router.get('/')
async def gett():
    return {'Dogs': bd_dog,'Cats': bd_cat}

@router.post('/dog/')
async def post_dog(dog: Dogs):
    bd_dog.append(dog)
    return dog

@router.post('/cat/')
async def post_cat(cat: Cats):
    bd_cat.append(cat)
    return cat

@router.post('/dog_sale/')
async def dog_sells(dog):
    clear(bd_dog)

@router.post('/cat_sale/')
async def cat_sells(cat):
    clear(bd_cat)


app.include_router(router)
