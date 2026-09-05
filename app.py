import streamlit as st
import streamlit.components.v1 as components

# Page configurations
st.set_page_config(page_title="For My Heartbeat ❤️", page_icon="💖", layout="centered")

# Hide Streamlit default styling for clean premium look
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 1rem;}
    </style>
""", unsafe_scale=True)

# App Title for you (Optional)
st.markdown("<h2 style='text-align: center; color: #ff3366; font-family: sans-serif;'>💖 Premium Interactive Love Gift 💖</h2>", unsafe_allow_html=True)

# Premium HTML, CSS aur JavaScript Injection
romantic_card_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Happy Birthday My Love</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: radial-gradient(circle at center, #ffccd5 0%, #ff4d6d 50%, #800f2f 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: 'Georgia', serif;
            overflow: hidden;
        }
        .container {
            position: relative;
            width: 100%;
            max-width: 480px;
            height: 680px;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-radius: 30px;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4), inset 0 0 20px rgba(255, 255, 255, 0.2);
            overflow: hidden;
            border: 2px solid rgba(255, 255, 255, 0.25);
        }
        canvas {
            display: block;
            width: 100%;
            height: 100%;
            cursor: grab;
        }
        canvas:active { cursor: grabbing; }
        .instruction {
            position: absolute;
            bottom: 40px;
            width: 100%;
            text-align: center;
            font-size: 13px;
            color: #fff;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 600;
            letter-spacing: 3px;
            text-transform: uppercase;
            pointer-events: none;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
            animation: pulseGlow 2s infinite ease-in-out;
        }
        @keyframes pulseGlow {
            0% { opacity: 0.5; transform: scale(0.98); text-shadow: 0 0 5px rgba(255,255,255,0.5); }
            50% { opacity: 1; transform: scale(1); text-shadow: 0 0 15px rgba(255,105,180,1); }
            100% { opacity: 0.5; transform: scale(0.98); text-shadow: 0 0 5px rgba(255,255,255,0.5); }
        }
    </style>
</head>
<body>

<div class="container">
    <canvas id="loveCanvas"></canvas>
    <div class="instruction">💖 Pull & Release the Heart 💖</div>
</div>

<script>
    const canvas = document.getElementById('loveCanvas');
    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    resize();

    // Slingshot parameters (styled as a beautiful glowing node)
    const anchor = { x: canvas.width / 2, y: canvas.height - 150 };
    const sling = { x: anchor.x, y: anchor.y, radius: 18 };
    let isDragging = false;

    let burstHearts = [];
    let bgHearts = [];
    let showCard = false;
    let cardScale = 0;
    let globalAlpha = 0;

    // Helper to draw a perfect vector heart shape
    function drawHeartShape(x, y, size) {
        ctx.beginPath();
        ctx.moveTo(x, y);
        ctx.bezierCurveTo(x - size/2, y - size/2, x - size, y + size/3, x, y + size);
        ctx.bezierCurveTo(x + size, y + size/3, x + size/2, y - size/2, x, y);
        ctx.fill();
    }

    // Background floating ambient hearts
    class AmbientHeart {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = canvas.height + Math.random() * 100;
            this.size = Math.random() * 8 + 6;
            this.speed = Math.random() * 0.8 + 0.4;
            this.opacity = Math.random() * 0.4 + 0.2;
        }
        update() {
            this.y -= this.speed;
            if (this.y < -20) {
                this.y = canvas.height + 20;
                this.x = Math.random() * canvas.width;
            }
        }
        draw() {
            ctx.save();
            ctx.fillStyle = `rgba(255, 182, 193, ${this.opacity})`;
            drawHeartShape(this.x, this.y, this.size);
            ctx.restore();
        }
    }

    // Premium Burst Hearts
    class BurstHeart {
        constructor(x, y, vx, vy) {
            this.x = x;
            this.y = y;
            // High energy physics dispersion
            this.vx = vx * 0.25 + (Math.random() - 0.5) * 12;
            this.vy = vy * 0.25 - (Math.random() * 8 + 6);
            this.size = Math.random() * 18 + 12;
            this.alpha = 1;
            this.decay = Math.random() * 0.01 + 0.008;
            this.angle = Math.random() * Math.PI * 2;
            this.rotationSpeed = (Math.random() - 0.5) * 0.05;
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            this.vy += 0.12; // gentle gravity
            this.vx *= 0.98;
            this.alpha -= this.decay;
            this.angle += this.rotationSpeed;
        }
        draw() {
            if (this.alpha <= 0) return;
            ctx.save();
            ctx.globalAlpha = this.alpha;
            ctx.translate(this.x, this.y);
            ctx.rotate(this.angle);
            
            // Neon shadow glow for premium feel
            ctx.shadowBlur = 15;
            ctx.shadowColor = '#ff0055';
            
            // Gradient fill for each heart
            let grad = ctx.createRadialGradient(0, 0, 2, 0, 0, this.size);
            grad.addColorStop(0, '#ff758c');
            grad.addColorStop(1, '#ff7eb3');
            ctx.fillStyle = grad;
            
            drawHeartShape(0, -this.size/2, this.size);
            ctx.restore();
        }
    }

    // Initialize background stars/hearts
    for(let i=0; i<25; i++) {
        bgHearts.push(new AmbientHeart());
    }

    // User Interaction handling
    function getMousePos(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches.clientX : e.clientX;
        const clientY = e.touches ? e.touches.clientY : e.clientY;
        return { x: clientX - rect.left, y: clientY - rect.top };
    }

    function startDrag(e) {
        const pos = getMousePos(e);
        const dist = Math.hypot(pos.x - sling.x, pos.y - sling.y);
        if (dist < 40) isDragging = true;
    }

    function drag(e) {
        if (!isDragging) return;
        const pos = getMousePos(e);
        const maxPull = 90;
        const dist = Math.hypot(pos.x - anchor.x, pos.y - anchor.y);
        
        if (dist < maxPull) {
            sling.x = pos.x;
            sling.y = pos.y;
        } else {
            const angle = Math.atan2(pos.y - anchor.y, pos.x - anchor.x);
            sling.x = anchor.x + Math.cos(angle) * maxPull;
            sling.y = anchor.y + Math.sin(angle) * maxPull;
        }
    }

    function endDrag() {
        if (!isDragging) return;
        isDragging = false;
        
        const vx = anchor.x - sling.x;
        const vy = anchor.y - sling.y;
        
        if (Math.hypot(vx, vy) > 20) {
            // Big dynamic romantic burst (50 premium hearts)
            for(let i=0; i<50; i++) {
                burstHearts.push(new BurstHeart(anchor.x, anchor.y, vx, vy));
            }
            showCard = true;
        }
        
        sling.x = anchor.x;
        sling.y = anchor.y;
    }

    canvas.addEventListener('mousedown', startDrag);
    canvas.addEventListener('mousemove', drag);
    window.addEventListener('mouseup', endDrag);

    canvas.addEventListener('touchstart', startDrag);
    canvas.addEventListener('touchmove', drag);
    window.addEventListener('touchend', endDrag);

    // Render loop
    function loop() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 1. Draw Ambient Background Hearts
        bgHearts.forEach(bh => {
            bh.update();
            bh.draw();
        });

        // 2. Draw Top Heading
        ctx.save();
        ctx.fillStyle = 'rgba(255, 230, 235, 0.9)';
        ctx.font = 'italic 20px Georgia';
        ctx.textAlign = 'center';
        ctx.shadowBlur = 8;
        ctx.shadowColor = '#000';
        ctx.fillText('a little something, for you', canvas.width / 2, 70);
        ctx.restore();

        // 3. Draw Premium Birthday Glass Card
        if (showCard) {
            if (cardScale < 1) cardScale += 0.04; // smooth pop up
            ctx.save();
            ctx.translate(canvas.width / 2, canvas.height / 3 + 10);
            ctx.scale(cardScale, cardScale);

            // Glowing Premium Translucent Box
            ctx.shadowBlur = 30;
            ctx.shadowColor = 'rgba(255, 0, 85, 0.6)';
            
            // Glass fill layer
            ctx.fillStyle = 'rgba(255, 255, 255, 0.88)';
            ctx.beginPath();
            ctx.roundRect(-160, -110, 320, 220, 20);
            ctx.fill();
            
            // Neon premium pink border line
            ctx.strokeStyle = '#ff2a6d';
            ctx.lineWidth = 3;
            ctx.stroke();

            // Inner clean gold accent border
            ctx.strokeStyle = 'rgba(218, 165, 32, 0.3)';
            ctx.lineWidth = 1;
            ctx.roundRect(-152, -102, 304, 204, 15);
            ctx.stroke();

            // Card Text Content Typography
            ctx.shadowBlur = 0;
            ctx.textAlign = 'center';
            
            ctx.fillStyle = '#ff0055';
            
