from ultralytics import YOLO
from pathlib import Path
from PIL import Image

__version__ = '0.1.0'

BASE_DIR = Path(__file__).resolve(strict=True).parent
MODEL_PATH = BASE_DIR / "best.pt"


def response_pipeline(model, img):
    results = model(img)
    return results