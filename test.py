if __name__ == '__main__':
    from ultralytics import YOLO
    model = YOLO(r"C:\Users\Miilee\PycharmProjects\test\funny\runs\detect\train\weights\best.pt")
    device = 'cuda:0'
    results = model.predict(source=r"C:\Users\Miilee\Documents\test.mp4", save=True, conf=0.5)

