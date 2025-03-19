import os; os.environ["YOLO_VERBOSE"] = "False"

from pathlib import Path
import fiftyone as fo
import fiftyone.utils.ultralytics as fou
from ultralytics import YOLO

BASE_DIR = Path(os.path.abspath('')).resolve(strict=True)

MODEL_DIR = BASE_DIR / "model_out" / "train2" / "weights" / "best.pt"

# load filtered dataset back in
dataset = fo.Dataset()

DATASET_PATH = BASE_DIR / "data" / "NPD" / "NPD-filtered"

TRAIN_IMG_DIR = DATASET_PATH / "data"
TRAIN_ANNOTATION_DIR = DATASET_PATH / "labels.json"

validation = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=str(TRAIN_IMG_DIR),
    labels_path=str(TRAIN_ANNOTATION_DIR),
    split='validation',
    max_samples=750,
)

print("Loaded in dataset...")

ft_model = YOLO(str(MODEL_DIR))

print("Running inference")
# run inference
validation.apply_model(ft_model, label_field="ft_predict")

results = validation.evaluate_detections(
    "ft_predict",
    gt_field="detections",
    eval_key="eval"
)