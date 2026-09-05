import streamlit as st
import streamlit.components.v1 as components

# Page configurations
st.set_page_config(page_title="Interactive Birthday Gift", page_icon="❤️", layout="centered")

# App Header
st.title("🎉 Interactive Birthday Web App")
st.write("Slingshot (guthail) ko mouse se peeche **PULL karke RELEASE** karein surprise dekhne ke liye!")

# Premium HTML, CSS aur JavaScript Injection
birthday_card_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: linear-gradient(135deg, #ffe5ec 0%, #ffc2d1 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
        }
        .canvas-container {
            position: relative;
            width: 100%;
            max-width: 500px;
            height: 600px;
            background: #fff0f5;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(255, 105, 180, 0.3);
            overflow: hidden;
            border: 4px solid #ff85a2;
        }
        canvas {
            display: block;
            width: 100%;
            height: 100%;
            cursor: grab;
        }
        canvas:active { cursor: grabbing; }
        .hint-text {
            position: absolute;
            bottom: 30px;
            width: 100%;
            text-align: center;
            font-size: 14px;
            color: #ff5c8a;
            font-weight: bold;
            letter-spacing: 2px;
            text-transform: uppercase;
            pointer-events: none;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { opacity: 0.6; }
            50% { opacity: 1; }
            100% { opacity: 0.6; }
        }
    </style>
</head>
<body>

<div class="canvas-container">
    <canvas id="giftCanvas"></canvas>
    <div class="hint-text">PULL & RELEASE THE SLINGSHOT</div>
</div>

<script>
    const canvas = document.getElementById('giftCanvas');
    const ctx = canvas.getContext('2d');

    // Resize canvas resolution
    function resize() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    resize();

    // Slingshot parameters
    const sling = { x: canvas.width / 2, y: canvas.height - 120, radius: 10 };
    const anchor = { x: canvas.width / 2, y: canvas.height - 120 };
    let isDragging = false;

    // Heart animations array
    let hearts = [];
    let showCard = false;
    let cardScale = 0;

    // Heart class for floating effect
    class FloatingHeart {
        constructor(x, y, vx, vy) {
            this.x = x;
            this.y = y;
            this.vx = vx * 0.15;
            this.vy = vy * 0.15 - 5; // upward force
            this.size = Math.random() * 15 + 15;
            this.alpha = 1;
        }
        update() {
            this.x += this.vx;
            this.y += this.vy;
            this.vy *= 0.98; // slowdown
            this.alpha -= 0.01;
        }
        draw() {
            ctx.save();
            ctx.globalAlpha = this.alpha;
            ctx.fillStyle = '#ff477e';
            ctx.beginPath();
            // Draw smooth heart path
            ctx.moveTo(this.x, this.y);
            ctx.bezierCurveTo(this.x - this.size/2, this.y - this.size/2, this.x - this.size, this.y + this.size/3, this.x, this.y + this.size);
            ctx.bezierCurveTo(this.x + this.size, this.y + this.size/3, this.x + this.size/2, this.y - this.size/2, this.x, this.y);
            ctx.fill();
            ctx.restore();
        }
    }

    // Mouse/Touch Events
    function getMousePos(e) {
        const rect = canvas.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clientY = e.touches ? e.touches[0].clientY : e.clientY;
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
        const maxPull = 80;
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
        
        // Calculate velocity vectors based on pull distance
        const vx = anchor.x - sling.x;
        const vy = anchor.y - sling.y;
        
        // Spawn hearts on release
        if (Math.hypot(vx, vy) > 20) {
            for(let i=0; i<15; i++) {
                hearts.push(new FloatingHeart(anchor.x, anchor.y, vx + (Math.random()-0.5)*20, vy));
            }
            showCard = true;
        }
        
        // Snap back slingshot
        sling.x = anchor.x;
        sling.y = anchor.y;
    }

    canvas.addEventListener('mousedown', startDrag);
    canvas.addEventListener('mousemove', drag);
    window.addEventListener('mouseup', endDrag);

    canvas.addEventListener('touchstart', startDrag);
    canvas.addEventListener('touchmove', drag);
    window.addEventListener('touchend', endDrag);

    // Main animation loop
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 1. Draw Background Text
        ctx.fillStyle = '#ff85a2';
        ctx.font = 'italic 18px Georgia';
        ctx.textAlign = 'center';
        ctx.fillText('a little something, for you', canvas.width / 2, 80);

        // 2. Draw Birthday Card if Triggered
        if (showCard) {
            if (cardScale < 1) cardScale += 0.05;
            ctx.save();
            ctx.translate(canvas.width/2, canvas.height/3 + 30);
            ctx.scale(cardScale, cardScale);
            
            // Draw Glowing Card Box
            ctx.shadowBlur = 20;
            ctx.shadowColor = 'rgba(255, 71, 126, 0.5)';
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(-150, -100, 300, 200);
            ctx.strokeStyle = '#ff477e';
            ctx.lineWidth = 3;
            ctx.strokeRect(-150, -100, 300, 200);
            
            // Card Content
            ctx.shadowBlur = 0;
            ctx.fillStyle = '#ff477e';
            ctx.font = 'bold 24px Arial';
            ctx.fillText('🎂 HAPPY 🎂', 0, -40);
            ctx.fillText('BIRTHDAY! 🎉', 0, -5);
            ctx.fillStyle = '#333';
            ctx.font = '14px Arial';
            ctx.fillText('May all your dreams come true!', 0, 40);
            ctx.fillText('❤️ ✨ ❤️', 0, 70);
            ctx.restore();
        }

        // 3. Update & Draw Hearts
        hearts.forEach((heart, index) => {
            heart.update();
            heart.draw();
            if (heart.alpha <= 0) hearts.splice(index, 1);
        });

        // 4. Draw Slingshot base bands
        ctx.strokeStyle = '#ff85a2';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.moveTo(anchor.x - 40, anchor.y - 10);
        ctx.lineTo(sling.x, sling.y);
        ctx.moveTo(anchor.x + 40, anchor.y - 10);
        ctx.lineTo(sling.x, sling.y);
        ctx.stroke();

        // 5. Draw Slingshot Y frame
        ctx.strokeStyle = '#db7093';
        ctx.lineWidth = 6;
        ctx.beginPath();
        ctx.moveTo(anchor.x - 40, anchor.y - 15);
        ctx.lineTo(anchor.x - 40, anchor.y + 10);
        ctx.lineTo(anchor.x, anchor.y + 50);
        ctx.lineTo(anchor.x, anchor.y + 100);
        ctx.moveTo(anchor.x + 40, anchor.y - 15);
        ctx.lineTo(anchor.x + 40, anchor.y + 10);
        ctx.lineTo(anchor.x, anchor.y + 50);
        ctx.stroke();

        // 6. Draw Pull Handle node
        ctx.fillStyle = '#ff477e';
        ctx.beginPath();
        ctx.arc(sling.x, sling.y, sling.radius, 0, Math.PI * 2);
        ctx.fill();

        requestAnimationFrame(animate);
    }

    animate();
</script>
</body>
</html>
"""

# Streamlit interface wrapper inside components
components.html(birthday_card_html, height=650, scrolling=False)
