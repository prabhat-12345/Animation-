import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configurations for a Premium Dark UI Layout
st.set_page_config(
    page_title="ASMR Physics Step Engine", 
    page_icon="🟢", 
    layout="centered"
)

# Hide Streamlit Default UI branding
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
            max-width: 100% !important;
        }
        body, [data-testid="stAppViewContainer"] {
            background-color: #080c10;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #00ff66; font-family: monospace; letter-spacing: 2px; text-shadow: 0 0 10px rgba(0,255,102,0.3);'>🟢 PREMIUM SATISFYING STEP ENGINE 🟢</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6f7e8a; font-size: 14px; margin-bottom: 20px;'>Satisfying 2D physics loop simulation with dynamic gravity and step bouncing triggers</p>", unsafe_allow_html=True)

# 2. Interactive Premium Physics Render Block (HTML5 Canvas + Gravity Engines)
step_engine_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: #080c10;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            width: 100vw;
        }
        .container {
            position: relative;
            width: 100%;
            max-width: 450px;
            height: 680px;
            background: linear-gradient(180deg, #121c24 0%, #0c1218 100%);
            border-radius: 25px;
            border: 2px solid #1a2630;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7);
            overflow: hidden;
        }
        canvas {
            display: block;
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>

<div class="container">
    <canvas id="physicsCanvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('physicsCanvas');
    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    resize();

    // Physics Engine Configurations
    const gravity = 0.28;
    const bounceFactor = -0.75; 
    let balls = [];

    // Premium Colors matching your screenshot theme
    const ballColor = '#ccff33'; // Vibrant Lime Green
    const platformColor = '#39ff14'; // Bright Neon Green
    const darkHoleColor = '#05080c';

    // Step Platforms Database (Positions modeled from top to bottom)
    const steps = [
        { x: 120, y: 150, width: 90, height: 25, radius: 12.5 },
        { x: 260, y: 220, width: 95, height: 25, radius: 12.5 },
        { x: 140, y: 310, width: 100, height: 25, radius: 12.5 },
        { x: 280, y: 400, width: 90, height: 25, radius: 12.5 },
        { x: 110, y: 490, width: 110, height: 25, radius: 12.5 }
    ];

    // Bottom Catching Holes for infinity loops visualization
    const holes = [
        { x: 150, y: 620, radius: 30 },
        { x: 300, y: 620, radius: 30 }
    ];

    // Ball Class Handler
    class PhysicsBall {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.radius = 14;
            this.vx = (Math.random() - 0.5) * 1.5;
            this.vy = 0;
            this.glow = 0;
        }
        
        update() {
            this.vy += gravity;
            this.x += this.vx;
            this.y += this.vy;

            // Wall collisions (Left & Right boundaries)
            if (this.x - this.radius < 0) {
                this.x = this.radius;
                this.vx *= -0.8;
            } else if (this.x + this.radius > canvas.width) {
                this.x = canvas.width - this.radius;
                this.vx *= -0.8;
            }

            // Platform Step Bouncing Math Engine
            steps.forEach(step => {
                // AABB Box and Rounded Capsule overlap calculation
                let closestX = Math.max(step.x, Math.min(this.x, step.x + step.width));
                let closestY = Math.max(step.y, Math.min(this.y, step.y + step.height));
                
                let distanceX = this.x - closestX;
                let distanceY = this.y - closestY;
                let distance = Math.hypot(distanceX, distanceY);

                if (distance < this.radius) {
                    // Collision response from the top surface
                    if (this.y < step.y + 5 && this.vy > 0) {
                        this.y = step.y - this.radius;
                        this.vy *= bounceFactor;
                        // Add slight roll push based on direction displacement
                        this.vx += (this.x - (step.x + step.width/2)) * 0.02;
                        this.glow = 15; // Trigger bounce glow wave
                    } else {
                        // Side bounce triggers
                        this.vx *= -0.9;
                        this.x += distanceX * 0.1;
                    }
                }
            });

            // Decay glow wave animations
            if (this.glow > 0) this.glow -= 0.5;
        }

        draw() {
            ctx.save();
            // Drop shadow for 3D depth illusion matching the screenshot
            ctx.shadowColor = 'rgba(0, 0, 0, 0.4)';
            ctx.shadowBlur = 10;
            ctx.shadowOffsetY = 8;
            
            // Soft inner gradient styling
            let grad = ctx.createRadialGradient(this.x - 4, this.y - 4, 2, this.x, this.y, this.radius);
            grad.addColorStop(0, '#f3ff85');
            grad.addColorStop(1, ballColor);
            
            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }
    }

    // Auto Ball Generation Spawner Loop (Runs infinitely every 2.2 seconds)
    setInterval(() => {
        if(balls.length < 8) {
            balls.push(new PhysicsBall(120 + Math.random() * 200, -20));
        }
    }, 2200);

    // Initial ball spawn instantly on launch
    balls.push(new PhysicsBall(160, 20));

    // Core Animation Frame Loop Engine
    function loop() {
        // Clear background with soft gradient persistence
        ctx.fillStyle = '#0c1218';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 1. Draw Bottom Dark Destination Holes
        holes.forEach(hole => {
            ctx.save();
            ctx.fillStyle = darkHoleColor;
            ctx.beginPath();
            ctx.arc(hole.x, hole.y, hole.radius, 0, Math.PI * 2);
            ctx.fill();
            
            ctx.strokeStyle = '#1a2630';
            ctx.lineWidth = 3;
            ctx.stroke();
            ctx.restore();
        });

        // 2. Render and Draw 3D Capsule Steps
        steps.forEach(step => {
            ctx.save();
            // Premium Ambient Occlusion Shadows below steps
            ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 12;

            // Draw clean rounded pill shape vector graphics
            ctx.fillStyle = '#1e2f3d';
            ctx.beginPath();
            ctx.roundRect(step.x, step.y, step.width, step.height, step.radius);
            ctx.fill();
            
            // Neon edge glow striping
            ctx.strokeStyle = platformColor;
            ctx.lineWidth = 2.5;
            ctx.stroke();
            ctx.restore();
        });

        // 3. Update, Boundary Filter and Draw Balls Pipeline
        for (let i = balls.length - 1; i >= 0; i--) {
            balls[i].update();
            balls[i].draw();

            // Destroy ball safely if it enters the bottom black holes or leaves screen
            if (balls[i].y > canvas.height + 40) {
                balls.splice(i, 1);
            }
        }

        requestAnimationFrame(loop);
    }

    loop();
</script>
</body>
</html>
"""

# Render inside Streamlit interface frame pipeline layout
components.html(step_engine_html, height=700, scrolling=False)
