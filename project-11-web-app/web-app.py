from flask import Flask
app = Flask(__name__)

@app.route("/")
def home() :
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>t5
        <meta charset="UTF-8">
        <title>Mohit's First HTML Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e5e7eb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: #111827;
                padding: 24px 32px;
                border-radius: 16px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                text-align: center;
                max-width: 400px;
            }
            h1 {
                margin-top: 0;
            }
            button {
                margin-top: 12px;
                padding: 8px 16px;
                border-radius: 999px;
                border: none;
                cursor: pointer;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, Mohit 👋</h1>
            <p>This is a simple HTML + CSS page.</p>
            <button onclick="alert('Keep coding, don\'t be lazy 😏')">
                Click Me
            </button>
        </div>
    </body>
    </html>
    """


@app.route("/about")
def abouta() :
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Login Page</title>
        <style>
            body {
                margin: 0;
                background: #1e293b;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .box {
                background: #0f172a;
                padding: 30px;
                width: 300px;
                border-radius: 12px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.4);
                color: #f1f5f9;
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
            }
            input {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border-radius: 8px;
                border: none;
            }
            button {
                width: 100%;
                padding: 10px;
                margin-top: 20px;
                border-radius: 8px;
                border: none;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background: #334155;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Login</h2>
            <input type="text" placeholder="Username">
            <input type="password" placeholder="Password">
            <button onclick="alert('Login button clicked!')">Login</button>
        </div>
    </body>
    </html>
    """

if __name__== '__main__':
    app.run(debug=True, use_reloader=False) 