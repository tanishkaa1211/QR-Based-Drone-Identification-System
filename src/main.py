import cv2

cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()

    data, bbox, _ = detector.detectAndDecode(frame)

    if bbox is not None:
        bbox = bbox.astype(int)

        for i in range(len(bbox[0])):
            pt1 = tuple(bbox[0][i])
            pt2 = tuple(bbox[0][(i + 1) % len(bbox[0])])
            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

        cv2.putText(
            frame,
            f"Drone ID: {data}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    cv2.imshow("Drone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
