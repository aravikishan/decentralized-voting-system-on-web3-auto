from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    password = Column(String)

class Candidate(Base):
    __tablename__ = "candidates"

    candidate_id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    party = Column(String)

class Vote(Base):
    __tablename__ = "votes"

    vote_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    candidate_id = Column(String, ForeignKey("candidates.candidate_id"))

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Seed data
@app.on_event("startup")
def seed_data():
    db = SessionLocal()
    if not db.query(Candidate).first():
        candidate1 = Candidate(candidate_id="1", name="Alice", party="Party A")
        candidate2 = Candidate(candidate_id="2", name="Bob", party="Party B")
        db.add(candidate1)
        db.add(candidate2)
        db.commit()
    db.close()

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/register", response_class=HTMLResponse)
async def register_page():
    with open("templates/register.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/candidates", response_class=HTMLResponse)
async def candidates_page():
    with open("templates/candidates.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/vote", response_class=HTMLResponse)
async def vote_page():
    with open("templates/vote.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/results", response_class=HTMLResponse)
async def results_page():
    with open("templates/results.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/api/register")
async def register_user(user_id: str, name: str, password: str, db: Session = Depends(get_db)):
    user = User(user_id=user_id, name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get("/api/candidates")
async def get_candidates(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    return candidates

@app.post("/api/vote")
async def vote(vote_id: str, user_id: str, candidate_id: str, db: Session = Depends(get_db)):
    vote = Vote(vote_id=vote_id, user_id=user_id, candidate_id=candidate_id)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote

@app.get("/api/results")
async def get_results(db: Session = Depends(get_db)):
    results = db.query(Vote.candidate_id, func.count(Vote.candidate_id).label('votes')).group_by(Vote.candidate_id).all()
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
