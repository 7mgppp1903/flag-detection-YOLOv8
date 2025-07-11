if __name__ == '__main__':
    from ultralytics import YOLO
    model = YOLO("yolov8.yaml")
    device = 'cuda:0'
    results = model.train(data="config.yaml", epochs=100,device=device)


