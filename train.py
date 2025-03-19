import os
from pathlib import Path
from ultralytics import YOLO
import torch

if __name__ == '__main__':
    # directory management
    BASE_DIR = Path(os.path.abspath('')).resolve(strict=True)
    EXPORT_DIR = BASE_DIR / "images"
    YAML_FILE = EXPORT_DIR / "dataset.yaml"

    # check cuda
    print(f"Cuda is available: {torch.cuda.is_available()}")

    # initalize model
    model = YOLO("yolo11n.pt")

    # train model
    model.train(data=YAML_FILE, epochs=50, imgsz=320, batch=24, project="model_out")