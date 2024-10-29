import uvicorn

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, EmailStr
from pymongo.errors import PyMongoError

app = FastAPI()

# Allow requests from these origins.
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

# Allow CORS for all origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the model for creating an item.
class ItemCreate(BaseModel):
    email: str
    image: str

# Define the model for the email request.
class EmailRequest(BaseModel):
    email: EmailStr

# Define the model for the item.
class Item(BaseModel):
    email: str

# Convert the BSON ObjectId to a string.
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "image": item["image"],
    }

# Connect to MongoDB.
client = AsyncIOMotorClient("mongodb://localhost:27017/")

# Select the database.
db = client.faces


# Check if an email is already registered.
@app.post("/face-id/checkpoint/email")
async def validate_email(request: EmailRequest):
    try:
        # Extract the email from the request.
        email = request.email

        # Find the item in the database.
        item = await db.items.find_one({"email": email})
        print(item)

        # If the item is not found, return a 404 error.
        if item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item no encontrado {email}")

        # If the item is found, return it.
        return item_helper(item)

    except HTTPException as http_exc:
        # Re-raise HTTP exceptions.
        raise http_exc

    except PyMongoError as e:
        # Capture any database errors and return a 500.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error en la base de datos: {str(e)}")

    except Exception as e:
        # Capture any other errors and return a 500.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error en el servidor: {str(e)}")


# Register a new item.
@app.post('/face-id/register', response_model=Item)
async def register(request: ItemCreate):
    item_dict = request.dict()

    try:
        # Try to insert the new item into the database.
        result = await db.items.insert_one(item_dict)

        # Try to retrieve the new item after insertion.
        new_item = await db.items.find_one({"_id": result.inserted_id})

        if new_item is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item not recovered after insertion: {item_dict}")

        # If the new item is found, return it.
        return item_helper(new_item)

    except PyMongoError as e:
        # Capture any database errors and return a 500.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Database Error: {str(e)}")

    except Exception as e:
        # Capture any other errors and return a 500.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Service Error: {str(e)}")


# Health check endpoint.
@app.get("/health")
async def root():
    return {"message": "I'm alive!"}


# Run the application.
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
