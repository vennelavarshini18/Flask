from flask import Flask,render_template,Response
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:
        success,frame=camera.read()    #success is a boolean that tells if we are able to read from camera
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)     # buffer helps to capture something that we are sending from backend to frontend
            frame=buffer.tobytes()
        yield(b'--frame\r\n'                             # yield keyword: To avoid capturing only one frame
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')      

@app.route('/')
def index():
    return render_template('index4.html')

@app.route('/video')
def video():   #we have to create some html content in index4.html, that should be continuously able to hit this url to take the streaming data 
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')      #Function takes the frames from the response and pass this entire response back to this index4.html

if __name__=='__main__':
    app.run(debug=True)