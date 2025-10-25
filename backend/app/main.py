from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from backend.app.database import SessionLocal, get_db
from backend.app.schemas.user import UserCreate, UserLogin, UserUpdate, FollowRequest
from backend.app.crud.user import register_user, authenticate_user
from backend.app.crud.profile import get_profile as get_profile_data
from backend.app.crud.profile import update_profile as update_profile_data
from backend.app.crud.profile import create_post as create_post_data
from backend.app.crud.profile import follow as follow_user
from backend.app.crud.profile import feed as get_feed
from backend.app.schemas.post import PostCreate
import re
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

origins =[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://social-media-app-jade-seven.vercel.app"
]

# Regex to cover any Vercel preview deployment URLs (which might not be in the list above)
allow_origin_regex = r"https://.*\.vercel\.app"


app.add_middleware(
    CORSMiddleware,
    # Use the specific list of allowed origins. 
    # This is MANDATORY when allow_credentials=True.
    allow_origins = origins, 
    
    # Keep the regex to cover dynamic Vercel preview domains
    allow_origin_regex=allow_origin_regex,
    
    # This is required if you are sending authentication tokens, cookies, or authorization headers
    allow_credentials=True,
    
    # Allow all methods and headers
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/testdb")
def test_db():
    return {"message": "Connected to db!!"}

#@app.post("/register")
#def register(user: UserCreate, db: Session = Depends(get_db)):
    #return register_user(db, user.username, user.email, user.password)
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        # This calls your authenticate_user function
        result = authenticate_user(db, user.username, user.password)
        
        # ... (logic for handling successful login)
            
    except Exception as e:
        # This catches CRITICAL errors like DB connection failures and logs them.
        logger.error(f"Critical 500 error during login for user {user.username}: {e}", exc_info=True)
        # This returns a proper 500 HTTP response (with CORS headers)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected critical server error occurred. Check server logs."
        )


@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(db, user.username, user.password)

@app.get("/profile/{username}")
def get_profile(username:str, db: Session = Depends(get_db)):
    return get_profile_data(username, db)

@app.patch("/profile/{username}")
def update_profile(update_data: UserUpdate, username:str, db: Session = Depends(get_db)):
    return update_profile_data(update_data, username, db)

@app.post("/profile/post/{username}")
def create_post(username:str, post_data: PostCreate, db: Session = Depends(get_db)):
    return create_post_data(username, post_data, db)

@app.post("/profile/follow/{username}")
def follow(username: str, otherUser: FollowRequest, db: Session = Depends(get_db)):
    return follow_user(username, otherUser, db)

@app.get("/feed/{username}")
def feed(username: str, db: Session = Depends(get_db)):
    return get_feed(username, db)