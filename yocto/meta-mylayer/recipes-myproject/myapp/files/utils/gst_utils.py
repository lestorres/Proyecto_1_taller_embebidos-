import cv2
import threading

def view(pipeline, stop_flag):
    cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)
    if not cap.isOpened():
        raise Exception("Error: Could not open GStreamer pipeline.")
        
    cv2.namedWindow("Video Analysis", cv2.WINDOW_NORMAL)
    
    while not stop_flag["value"]:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
            
        cv2.imshow("Video Analysis", frame)
        
        # Check for 'q' key press to exit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            stop_flag["value"] = True
            break
    
    cap.release()
    cv2.destroyAllWindows()

def gst_launch(pipeline_str):
    # Create a stop flag dictionary to be shared between threads
    stop_flag = {"value": False}
    
    print("Starting video. Press 'q' in the video window to stop.")
    
    # Run the video in a different thread
    thread = threading.Thread(target=view, args=(pipeline_str, stop_flag))
    thread.start()
    
    return thread, stop_flag  # Return both so the main program can set stop_flag["value"] = True to stop