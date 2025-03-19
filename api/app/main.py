from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

from ultralytics import YOLO

from pathlib import Path
from PIL import Image
import io

from flask import Flask, render_template

from app.model.model import response_pipeline
from app.model.model import __version__ as model_version


# Set the base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent

# Initialize and load the model
model = YOLO(f"{BASE_DIR}/model/best.pt")

# Initialize the FastAPI app
api = FastAPI(title="Nighttime Pothole Detection API")

# Add CORS middleware
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

# Mount flask on fastapi
api.mount("/index/", WSGIMiddleware(app))


@api.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


@api.get("/info")
def info():
    return {"model_version": model_version, "description": "Object detection model for nighttime potholes"}

@api.post("/generate")
async def generate(image: UploadFile):
    image_data = await image.read()
    img = Image.open((io.BytesIO(image_data)))
    output = response_pipeline(model=model, img=img)[0]

    output_io = io.BytesIO()
    output.save("temp.png")
    out = Image.open("temp.png")
    out.save(output_io, format="PNG")
    output_io.seek(0)

    return StreamingResponse(output_io, media_type="image/png")

# Mount the static folder
test_dir = f"{BASE_DIR}/static"
api.mount(f"{BASE_DIR}/static", StaticFiles(directory="app/static"), name="static")