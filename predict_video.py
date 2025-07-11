from ultralytics import YOLO
import cv2

# Paths on Windows
weights_path = r'C:\Users\Ishan\PycharmProjects\test\funny\runs\detect\train\weights\best.pt'  # Path to your YOLOv8 weights
video_path = r'C:\Users\Ishan\PycharmProjects\test\funny\video.mp4'  # Path to your input video
output_path = r'C:\Users\Ishan\PycharmProjects\test\funny\output_video.mp4'  # Path to save the output video

# Load the YOLOv8 model
model = YOLO(weights_path)

# Open the video file
cap = cv2.VideoCapture(video_path)

# Get video details
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model.predict(source=frame, save=False, conf=0.25)  # Adjust confidence threshold if needed

    # Annotate the frame with the detection results
    annotated_frame = results[0].plot()

    # Write the annotated frame into the output video
    out.write(annotated_frame)

    # Display the frame (optional)
    cv2.imshow('Video', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
