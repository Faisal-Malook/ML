from flask import Flask
import requests
from google.auth import app_engine

app = Flask(__name__)

@app.route('/')
def serve_metadata():
    # URL for the Cloud Storage object metadata
    url1 = 'https://www.googleapis.com/storage/v1/b/my-image-bucket-task-2/o/London_Big_Ben_Phone_box.jpg'
    url2 = 'https://www.googleapis.com/storage/v1/b/my-image-bucket-task-2/o/filename-img-1097-jpg.jpg'
    url3 = 'https://www.googleapis.com/storage/v1/b/my-image-bucket-task-2/o/topic-london-gettyimages-760251843-feature.jpg'

    # Fetch metadata for each image
    response1 = requests.get(url1)
    response2 = requests.get(url2)
    response3 = requests.get(url3)

    # Extract metadata from responses
    metadata1 = response1.json()
    metadata2 = response2.json()
    metadata3 = response3.json()

    # Format the metadata as HTML
    html_metadata = "<h1>Metadata for the images:</h1><br>"

    html_metadata += "<h2>Image 1:</h2>"
    html_metadata += format_metadata(metadata1)

    html_metadata += "<h2>Image 2:</h2>"
    html_metadata += format_metadata(metadata2)

    html_metadata += "<h2>Image 3:</h2>"
    html_metadata += format_metadata(metadata3)

    # HTML template with CSS styling
    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Metadata</title>
        <style>
            body {{
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h1 {{
                color: #333;
            }}
            h2 {{
                color: #666;
                margin-bottom: 10px;
            }}
            p {{
                color: #999;
                margin-left: 20px;
            }}
        </style>
    </head>
    <body>
        {html_metadata}
    </body>
    </html>
    """

    return html_template

def format_metadata(metadata):
    formatted = "<ul>"
    for key, value in metadata.items():
        formatted += f"<li><strong>{key}:</strong> {value}</li>"
    formatted += "</ul>"
    return formatted

if __name__ == '__main__':
    app.run(host='127.0.1.1', port=8080)
