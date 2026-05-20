from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   
    quote = "Чем гуще лес ,тем скиюидидопесес"
    author = "пикасо"
    
    return f'''
    <html>
        <head>
            <title>пупупу</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 100px;
                    background-color: #f0f0f0;
                }}
                .quote {{
                    font-size: 24px;
                    color: #333;
                    margin: 20px;
                }}
                .author {{
                    font-size: 18px;
                    color: #666;
                    font-style: italic;
                }}
            </style>
        </head>
        <body>
            <div class="quote">"{quote}"</div>
            <div class="author">— {author}</div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)