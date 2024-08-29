from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NicheSolv</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: white;
            padding: 1rem 2rem;
            text-align: center;
        }
        nav {
            background-color: #444;
            color: white;
            padding: 0.5rem 2rem;
        }
        nav a {
            color: white;
            text-decoration: none;
            margin: 0 1rem;
        }
        .hero {
            padding: 2rem;
            text-align: center;
            background-color: #555;
            color: white;
        }
        .hero h1 {
            margin: 0;
            font-size: 3rem;
        }
        .content {
            padding: 2rem;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to NicheSolv</h1>
</header>

<nav>
    <a href="#">Home</a>
    <a href="#">About</a>
    <a href="#">Services</a>
    <a href="#">Contact</a>
</nav>

<section class="hero">
    <h1>We Provide Innovative Solutions</h1>
    <p>Your success is our mission. Let us help you achieve your goals with our cutting-edge solutions.</p>
</section>

<section class="content">
    <h2>About Us</h2>
    <p>NicheSolv is a leading provider of technology solutions, specializing in helping businesses reach their full potential.</p>
    
    <h2>Our Services</h2>
    <p>We offer a range of services including cloud computing, data analytics, and cybersecurity.</p>
</section>

<footer>
    <p>&copy; 2024 NicheSolv. All rights reserved.</p>
</footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
