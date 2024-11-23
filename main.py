from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('templates'):
        os.makedirs('templates')

    html_content = '''<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            background: #e19aaa;
            padding: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            position: relative;
            overflow: hidden;
        }

        .rose {
            position: absolute;
            font-size: 1.8rem;
            opacity: 0;
            animation: floatRose 3s ease-in-out infinite;
        }

        .text-reveal {
            font-size: 3.5rem;
            color: white;
            text-align: center;
            position: relative;
            z-index: 3;
            font-weight: 900;
            text-shadow: 
                -3px -3px 0 #000,
                3px -3px 0 #000,
                -3px 3px 0 #000,
                3px 3px 0 #000,
                0 0 10px rgba(0,0,0,0.5);
            font-family: Arial, sans-serif;
        }

        .line {
            opacity: 0;
            transform: perspective(500px) translateZ(-100px);
            margin: 20px 0;
            letter-spacing: 2px;
            -webkit-text-stroke: 2px black;
        }

        .line:nth-child(1) {
            animation: revealText 1s ease forwards;
            animation-delay: 0.5s;
        }

        .line:nth-child(2) {
            animation: revealText 1s ease forwards;
            animation-delay: 1.5s;
        }

        .line:nth-child(3) {
            animation: revealText 1s ease forwards;
            animation-delay: 2.5s;
        }

        .wink-emoji {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) scale(0);
            font-size: 8rem;
            opacity: 0;
            z-index: 10;
        }

        .text-fade {
            animation: fadeOut 1s ease forwards;
            animation-delay: 3.5s;
        }

        .wink-appear {
            animation: winkReveal 1s ease forwards;
            animation-delay: 4.5s;
        }

        @keyframes revealText {
            0% {
                opacity: 0;
                transform: perspective(500px) translateZ(-100px);
            }
            100% {
                opacity: 1;
                transform: perspective(500px) translateZ(0);
            }
        }

        @keyframes fadeOut {
            to {
                opacity: 0;
                transform: scale(0.8);
            }
        }

        @keyframes winkReveal {
            0% {
                opacity: 0;
                transform: translate(-50%, -50%) scale(0) rotate(-180deg);
            }
            70% {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1.2) rotate(0deg);
            }
            100% {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1) rotate(0deg);
            }
        }

        @keyframes floatRose {
            0% {
                opacity: 0;
                transform: translateY(20px) scale(0);
            }
            20% {
                opacity: 0.6;
                transform: translateY(0) scale(1);
            }
            80% {
                opacity: 0.6;
                transform: translateY(0) scale(1);
            }
            100% {
                opacity: 0;
                transform: translateY(-20px) scale(0.8);
            }
        }
    </style>
</head>
<body>
    <div class="container" id="container">
        <div class="text-reveal text-fade">
            <div class="line">SİZ SİZ OLUN ZATEN</div>
            <div class="line">BİZ OLAMAZSINIZ,</div>
            <div class="line">HAYIRLI CUMALAR</div>
        </div>
        <div class="wink-emoji wink-appear">😉</div>
    </div>

    <script>
        function createRoses() {
            const container = document.getElementById('container');
            const roses = '🌹';
            const numberOfRoses = 150;

            for (let i = 0; i < numberOfRoses; i++) {
                const rose = document.createElement('div');
                rose.className = 'rose';
                rose.textContent = roses;

                const left = Math.random() * 100;
                const top = Math.random() * 100;

                rose.style.left = `${left}%`;
                rose.style.top = `${top}%`;
                rose.style.animationDelay = `${Math.random() * 3}s`;

                container.appendChild(rose);
            }
        }

        createRoses();
    </script>
</body>
</html>'''

    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    app.run(debug=True)