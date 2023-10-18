import os
import cv2
from ultralytics import YOLO

video_path = 'C:/Users/Games/Downloads/sURVEY/Mesmerising Mass Sheep Herding.mp4'
video_path_out = '{}_out_train29_threshold025_Epoch200+.mp4'.format(video_path)
confidences_output_path = 'sheepconfidences25_output.txt'

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = os.path.join('.', 'runs', 'detect', 'train31', 'weights', 'last.pt')

model = YOLO(model_path)  # load a custom model

threshold = 0.25

# Create/open a file to store confidences
with open(confidences_output_path, 'w') as conf_file:
    while ret:
        results = model(frame)[0]
        
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            
            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                label = "{} {:.2f}".format(results.names[int(class_id)].upper(), score)
                cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

                # Write confidence and class to file
                conf_file.write(f"{results.names[int(class_id)]}: {score}\n")
        
        out.write(frame)
        ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()
