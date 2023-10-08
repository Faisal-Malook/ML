from flask import Flask

app = Flask(__name__)

@app.route('/')
def image_gallery():
    return """
    <h1>Image Gallery</h1>
    <div>
        <h3>Image 1</h3>
        <img src="https://storage.googleapis.com/my-image-bucket-task-2/filename-img-1097-jpg.jpg" alt="Image 1">
    </div>
    <div>
        <h3>Image 2</h3>
        <img src="https://storage.googleapis.com/my-image-bucket-task-2/London_Big_Ben_Phone_box.jpg" alt="Image 2">
    </div>
    <div>
        <h3>Image 3</h3>
        <img src="https://storage.googleapis.com/my-image-bucket-task-2/topic-london-gettyimages-760251843-feature.jpg" alt="Image 3">
    </div>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
