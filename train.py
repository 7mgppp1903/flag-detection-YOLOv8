if __name__ == '__main__':
    from ultralytics import YOLO
    model = YOLO("yolo11n.pt")
    device = 'cuda:0'
    results = model.train(data="config.yaml", epochs=5,device=device)


