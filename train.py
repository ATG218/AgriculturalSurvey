from ultralytics import YOLO
import torch

if __name__ == '__main__':
    model = YOLO("yolov8s.yaml")

    results = model.train(data="data.yaml", epochs = 300, device = 0)