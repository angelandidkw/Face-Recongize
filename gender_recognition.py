import cv2
import mediapipe as mp
import face_recognition

class FaceLocator:
    def __init__(self, camera_index=2):
        # Initialize MediaPipe Face Detection with a higher confidence threshold.
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=0, min_detection_confidence=0.7  # Increased threshold to reduce false positives
        )
        self.camera_index = camera_index

    def get_face_boxes(self, image):
        """
        Process the image using MediaPipe Face Detection and return a list of bounding boxes.
        Each bounding box is represented as a tuple: (x, y, width, height).
        """
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_detection.process(rgb_image)
        boxes = []
        if results.detections:
            h, w, _ = image.shape
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                confidence = detection.score[0]  # Get the confidence score
                x = int(bbox.xmin * w)
                y = int(bbox.ymin * h)
                width = int(bbox.width * w)
                height = int(bbox.height * h)
                # Ensure coordinates are within the frame boundaries.
                x, y = max(0, x), max(0, y)
                width, height = min(width, w - x), min(height, h - y)
                print(f"Detected face at ({x}, {y}) with confidence: {confidence:.2f}")
                boxes.append((x, y, width, height))
        return boxes

    def is_real_face(self, image):
        """Check if the image contains at least one detectable face."""
        boxes = self.get_face_boxes(image)
        return len(boxes) > 0

    def verify_face(self, face_region, reference_encoding):
        """
        Verify if the detected face matches the reference face encoding.
        Returns True if the face matches, False otherwise.
        """
        try:
            rgb_face_region = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_face_region)
            if not face_locations:
                return False

            face_encoding = face_recognition.face_encodings(rgb_face_region, face_locations)[0]
            return face_recognition.compare_faces([reference_encoding], face_encoding, tolerance=0.5)[0]
        except Exception as e:
            print(f"Error during face verification: {e}")
            return False

    def locate_user(self, name, reference_encoding):
        """
        Open the camera and try to locate the user.
        Draw bounding boxes around detected faces and display the provided name.
        Verify the detected face against the reference encoding.
        """
        cap = cv2.VideoCapture(2)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        print(f"Looking for {name}... Press 'q' to quit.")
        try:
            while True:
                success, frame = cap.read()
                if not success:
                    print("Failed to capture frame.")
                    break

                boxes = self.get_face_boxes(frame)

                # If at least one face is detected, annotate the frame.
                for (x, y, width, height) in boxes:
                    face_region = frame[y:y + height, x:x + width]

                    if not self.verify_face(face_region, reference_encoding):
                        label = "Unknown"
                        color = (0, 0, 255)  # Red for unknown faces
                    else:
                        label = f"Found {name}!"
                        color = (0, 255, 0)  # Green for verified faces

                    cv2.rectangle(frame, (x, y), (x + width, y + height), color, 2)
                    cv2.putText(frame, label, (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

                # Display the frame.
                cv2.imshow('Locate User', frame)

                # Exit if 'q' is pressed.
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            print("Interrupted by user.")
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def run(self):
        """
        Main function:
         1. Load the reference image and extract its face encoding.
         2. Open the camera and try to locate the user using face verification.
        """
        # Load the reference image.
        reference_image_path = "/Users/angelmarquezchavarria/AI Recong/IMG_8552.JPG"
        reference_image = cv2.imread(reference_image_path)
        if reference_image is None:
            print(f"Error: Could not load the reference image from {reference_image_path}. Please check the file path.")
            return

        # Ensure the reference image contains a face.
        if not self.is_real_face(reference_image):
            print("No face detected in the reference image. Please use an image with a clear face.")
            return

        # Extract the face encoding from the reference image.
        rgb_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_reference)
        if not face_locations:
            print("Failed to extract face encoding from the reference image.")
            return

        reference_encoding = face_recognition.face_encodings(rgb_reference, face_locations)[0]

        # Prompt the user for their name.
        name = input("What is your name? ").strip()

        # Start locating the user.
        self.locate_user(name, reference_encoding)


if __name__ == "__main__":
    face_locator = FaceLocator(camera_index=2)
    face_locator.run()