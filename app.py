import streamlit as st
import streamlit.components.v1 as components

# Page Configurations for Full Screen Graphics Rendering
st.set_page_config(
    page_title="ASMR Vertical Step Pipeline Engine", 
    page_icon="🟢", 
    layout="centered"
)

# Hide Streamlit Default UI elements completely
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0.5rem;
            max-width: 100% !important;
        }
        body, [data-testid="stAppViewContainer"] {
            background-color: #1e3f20;
        }
    </style>
""", unsafe_allow_html=True)

# True 3D Depth Canvas Shading Injector
satisfying_physics_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: radial-gradient(circle at center, #2e6f40 0%, #16351e 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            width: 100vw;
            height: 100vh;
        }
        .app-viewport {
            position: relative;
            width: 100%;
            max-width: 460px;
            height: 780px;
            background: linear-gradient(180deg, #255c34 0%, #13301a 100%);
            border-radius: 35px;
            box-shadow: 0 35px 80px rgba(0, 0, 0, 0.6);
            overflow: hidden;
            border: 3px solid #1c4627;
        }
        canvas {
            display: block;
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>

<div class="app-viewport">
    <canvas id="flowCanvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('flowCanvas');
    const ctx = canvas.getContext('2d');

    function initViewport() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
    }
    initViewport();

    // Pure Physics Dynamics Constants
    const gravityForce = 0.32;
    let particlesArray = [];

    // Screen Asset Positions matching the exact layout of top-to-bottom steps
    const verticalPillars = [
        { id: 1, x: 120, y: 110, width: 70, height: 160, innerHoleX: 155 },
        { id: 2, x: 280, y: 220, width: 70, height: 160, innerHoleX: 315 },
        { id: 3, x: 150, y: 400, width: 75, height: 180, innerHoleX: 187 },
        { id: 4, x: 310, y: 530, width: 75, height: 180, innerHoleX: 347 }
    ];

    class FlowBall {
        constructor() {
            // Spawning near the first top platform gate path
            this.x = 155 + (Math.random() - 0.5) * 8;
            this.y = -30;
            this.radius = 15;
            this.vy = 0;
            this.vx = 0;
            this.currentStep = 0; 
            this.bounceTimer = 0;
        }

        physicsEngineUpdate() {
            this.vy += gravityForce;
            this.y += this.vy;
            this.x += this.vx;

            // Sequential Vertical Target Detection logic loop
            for (let index = 0; index < verticalPillars.length; index++) {
                let pillar = verticalPillars[index];
                
                // Detection layer for verifying ball impacts top lip of cylinder
                if (this.y + this.radius >= pillar.y && this.y - this.radius <= pillar.y + 15) {
                    if (this.x >= pillar.x && this.x <= pillar.x + pillar.width) {
                        
                        // Check if ball falls inside the hole or hits surface rims
                        let offsetFromHoleCenter = Math.abs(this.x - pillar.innerHoleX);
                        
                        if (offsetFromHoleCenter < 12) {
                            // Perfect alignment: Ball drops inside the shaft channel seamlessly
                            if (this.currentStep === index) {
                                this.currentStep = index + 1;
                                // Slow down speed inside channel for aesthetic satisfying look
                                this.vy = 2.2; 
                                this.vx = 0;
                                
                                // Divert trajectory path for next subsequent step target destination
                                if (this.currentStep < verticalPillars.length) {
                                    let nextPillar = verticalPillars[this.currentStep];
                                    // Soft math curve to push ball sideways out of bottom exit towards next pipe
                                    setTimeout(() => {
                                        this.vx = (nextPillar.innerHoleX - this.x) * 0.022;
                                    }, 280);
                                } else {
                                    // Final step exit push calculations
                                    setTimeout(() => { this.vx = (Math.random() > 0.5 ? 2.5 : -2.5); }, 300);
                                }
                            }
                        } else {
                            // Surface rim impact detection: perform elastic rebound
                            if (this.vy > 0 && this.y < pillar.y + 5) {
                                this.y = pillar.y - this.radius;
                                this.vy = -this.vy * 0.45; // Soft dampening rebound
                                this.vx += (this.x - pillar.innerHoleX) * 0.1; 
                                this.bounceTimer = 10;
                            }
                        }
                    }
                }
            }

            if (this.bounceTimer > 0) this.bounceTimer--;
        }

        renderGraphics() {
            ctx.save();
            // Vector lighting properties mimicking screenshots asset textures
            ctx.shadowColor = 'rgba(0, 0, 0, 0.45)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 10;

            let sphereGrad = ctx.createRadialGradient(this.x - 5, this.y - 5, 2, this.x, this.y, this.radius);
            sphereGrad.addColorStop(0, '#f9ff9e');
            sphereGrad.addColorStop(0.4, '#d8ff33');
            sphereGrad.addColorStop(1, '#9fcc00');

            ctx.fillStyle = sphereGrad;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }
    }

    // Time Trigger Loop Engine generating sequential drops fluidly
    setInterval(() => {
        if (particlesArray.length < 5) {
            particlesArray.push(new FlowBall());
        }
    }, 2800);

    // Initial item generated fast at boot runtime
    particlesArray.push(new FlowBall());

    function frameLoop() {
        // Redraw canvas frame configurations
        ctx.fillStyle = '#22522e';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 1. Render Layer: Solid Cylindrical Pillars Architecture
        verticalPillars.forEach(pillar => {
            ctx.save();
            // Drop shadows beneath background pipes assets
            ctx.shadowColor = 'rgba(0, 0, 0, 0.4)';
            ctx.shadowBlur = 15;
            ctx.shadowOffsetY = 15;

            // Pillar Solid Core body rendering block
            let bodyGrad = ctx.createLinearGradient(pillar.x, pillar.y, pillar.x + pillar.width, pillar.y);
            bodyGrad.addColorStop(0, '#59ab43');
            bodyGrad.addColorStop(0.3, '#7ed35b');
            bodyGrad.addColorStop(0.7, '#499335');
            bodyGrad.addColorStop(1, '#2f6620');

            ctx.fillStyle = bodyGrad;
            ctx.beginPath();
            ctx.roundRect(pillar.x, pillar.y, pillar.width, pillar.height, [0, 0, 35, 35]);
            ctx.fill();

            // Premium Inner Hole Rim Vector Ring Mapping
            ctx.shadowBlur = 0;
            ctx.shadowOffsetY = 0;
            ctx.fillStyle = '#0f2613'; // Hollow darkness indicator inside pipe ring
            ctx.beginPath();
            ctx.arc(pillar.innerHoleX, pillar.y, 22, 0, Math.PI * 2);
            ctx.fill();

            // Vibrant Neon Edge highlight profile borders
            ctx.strokeStyle = '#b2ff59';
            ctx.lineWidth = 3.5;
            ctx.stroke();
            ctx.restore();
        });

        // 2. Render Layer: Processing Active Particles Array Pipelines
        for (let i = particlesArray.length - 1; i >= 0; i--) {
            particlesArray[i].physicsEngineUpdate();
            particlesArray[i].renderGraphics();

            // Safeguard cleanup code checking bottom bound limits
            if (particlesArray[i].y > canvas.height + 50) {
                particlesArray.splice(i, 1);
            }
        }

        requestAnimationFrame(frameLoop);
    }

    frameLoop();
</script>
</body>
</html>
"""

# Render inside Streamlit interface pipeline view block
components.html(satisfying_physics_html, height=800, scrolling=False)
