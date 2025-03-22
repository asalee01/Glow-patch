# **Glow Patch**

## **Overview**
In machine learning and computer vision, tackling the problem of detection of road potholes at night has been a critical step
in furthering the safety of AI-powered vehicle transportation. In toward of solving this problem we present a baseline object
detector using **YOLOv11** and fine-tuning on the [Nighttime Pothole Dataset](https://doi.org/10.3390/electronics13193790) (NPD).
Over 50 epochs the model the model achieved an mAP@0.5 score of 0.93245, a 1.6% improvement compared to results found in 
Ling et. al's paper.

We use **Fiftyone** to streamline the COCO dataset sanitization and cleaning process. Training using the **Ultralytics** library
we deploy our model using **Flask, FastAPI, Docker, and AWS**.

Use our solution at [Glow Patch](http://18.190.152.65/)

This project was developed during the Voxel51 AI Hackathon at the University of British Columbia and we extended the functionality
by deploying the app afterwards.

### 📊 **Data Sanitzation**

Using the Fiftyone library and GUI we computed image embeddings to seperate images into many categories and filtered to ensure a
balanced dataset.

![Fiftyone Embeddings](/img/embeddings.png)

### 📈 **Training**

Over the 50 epochs we see a convergent increase in precision score

![Training graph results](/img/result.png)

### 🌟 **Results**

Our training resulted in favorable results as seen on the prediction of the validation set:

![Validation predictions picture](/img/val_pred.jpg)

---
## **Project Workflow**

1. **Data Sanitization** → Filtering out images based on *computed embeddings* to ensure a **balanced dataset**. 
2. **Training & Validation** → **Fine-tuned** pre-trained model on NPD on **NVIDIA 4060 Laptop** graphics card, validated on small set.
3. **Deployment** → Dockerized inference service and deployed on **AWS ECS** with a **integrated front-end**.

---
## **Tech Stack**

| **Technology** | **Usage** |
|---------------|----------|
| **Fiftyone** | Data visualization and filtration |
| **Ultralytics** | Fine-tuning and model inference |
| **Docker** | Containerization of solution |
| **AWS** | Deployment of solution with elastic demmand scaling |
| **FastAPI** | API middleware for inference |
| **Flask** | API routing and webapp |
| **Python** | Main programming language |
| **Bootstrap** | Front-end UI design and layout |

---
## **Usage & Installation**

### **Website**
Our service is live and hosted on [Glow Patch](http://18.190.152.65/), check it out!

### **Installation Prerequisites**
You must have **Python 3.9** and **Docker** installed along with the required packages in both `/requirements.txt` and
`api/requirements.txt`.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/asalee01/Glow-patch.git
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
cd api
pip install -r requirements.txt
```

### **3️⃣ Build Docker Image**
```bash
docker build -t glow-patch .
```

### **4️⃣ Run the Program**
```bash
docker run -d --name container -p 80:80 glow-patch
```

Now the app should be running locally on port 80.

---
## **Future Improvements**
✅ Video support for real-time object detection on web app.

✅ Real-time object detection with live video input.

✅ Port webapp to iOS, Android with Tesla compatability.

---
## **Contributions**
All contributions are welcome, open to pull requests and suggestions.

📩 **Contact:** ahusseinse@yahoo.com | 🌐 LinkedIn: Ali Osman

📩 **Contact:** asalee01@student.ubc.ca | 🌐 LinkedIn: Athif Saleem

📩 **Contact:** zxia0101@student.ubc.ca | 🌐 LinkedIn: Kaseya Xia

---
## **License**
This project is licensed under the MIT License. See `LICENSE` for details.
