import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configurations (Premium Dark Premium Theme Layout)
st.set_page_config(
    page_title="Vortex Mandala Engine | Interactive Studio", 
    page_icon="🎨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyberpunk Pink/Neon Theme Overlay for Streamlit Interface
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 2rem;
            max-width: 100% !important;
        }
        body, [data-testid="stAppViewContainer"] {
            background-color: #05050a;
            color: #ffffff;
        }
        [data-testid="stSidebar"] {
            background-color: #0b0c16;
            border-right: 1px solid #1f223f;
        }
        .stSlider label {
            color: #00ffcc !important;
            font-weight: bold;
            letter-spacing: 1px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Design for Fine-Tuning Controls
st.sidebar.markdown("<h2 style='text-align: center; color: #ff007f; font-family: sans-serif; letter-spacing: 2px; text-shadow: 0 0 10px rgba(255,0,127,0.5);'>🛠️ ENGINE ENGINE</h2>", unsafe_allow_html=True)
st.sidebar.write("Customize the live particle generation math dynamically.")

# UI Custom Controls Parameters injected from Streamlit to JS Fluidly
cycles = st.sidebar.slider("Mandala Cycles (Geometry Branching)", min_value=2, max_value=12, value=6, step=1)
render_speed = st.sidebar.slider("Rendering Trace Speed (Frames per batch)", min_value=1, max_value=20, value=8, step=1)
max_iterations = st.sidebar.slider("Total Particle Iterations", min_value=100, max_value=600, value=360, step=20)
size_scale = st.sidebar.slider("Vector Scale Factor", min_value=0.05, max_value=0.25, value=0.13, step=0.01)
glow_effect = st.sidebar.checkbox("Activate High-End Neon Shadow Glow Effect", value=True)

# Main Studio Banner Typography
st.markdown("<h1 style='text-align: center; color: #00ffcc; font-family: monospace; letter-spacing: 4px; text-shadow: 0 0 15px rgba(0,255,204,0.6);'>🌀 VORTEX MANDALA GRAPHICS ENGINE 🌀</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8f93a9; font-style: italic; font-size: 15px; margin-bottom: 25px;'>Premium procedural vector animation using mathematics and algorithmic geometry shading</p>", unsafe_allow_html=True)

# Boolean helper for JS compatibility
glow_str = "true" if glow_effect else "false"

# Ultra Premium Render Engine Block (HTML5 + Responsive Shaders)
premium_graphics_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-color: #05050a;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            width: 100vw;
        }}
        .stage {{
            position: relative;
            width: 92vw;
            height: 72vh;
            background: linear-gradient(145deg, #020205, #0a0b18);
            border-radius: 24px;
            border: 2px solid #1a1c38;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), inset 0 0 40px rgba(26, 28, 56, 0.3);
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        canvas {{
            display: block;
            max-width: 100%;
            max-height: 100%;
        }}
        .hud-display {{
            position: absolute;
            top: 20px;
            left: 25px;
            font-family: 'Courier New', Courier, monospace;
            color: rgba(0, 255, 204, 0.7);
            font-size: 12px;
            pointer-events: none;
            line-height: 1.6;
            letter-spacing: 1px;
            text-shadow: 0 0 5px rgba(0,255,204,0.3);
        }}
    </style>
</head>
<body>

<div class="stage">
    <div class="hud-display">
        SYS_STATUS: ACTIVE<br>
        ENGINE_MODE: PROCEDURAL_VORTEX<br>
        VECTOR_CYCLES: {cycles}<br>
        COMPUTED_NODES: <span id="nodeCounter">0</span>
    </div>
    <canvas id="renderEngineCanvas"></canvas>
</div>

<script>
    const canvas = document.getElementById('renderEngineCanvas');
    const ctx = canvas.getContext('2d');
    const nodeCounter = document.getElementById('nodeCounter');

    // Make canvas automatically respond seamlessly to all screen ratios
    function autoResize() {{
        const parentWidth = canvas.parentElement.clientWidth;
        const parentHeight = canvas.parentElement.clientHeight;
        const squareSize = Math.min(parentWidth, parentHeight) - 30;
        canvas.width = squareSize;
        canvas.height = squareSize;
    }}
    autoResize();

    // High performance analytical HSV to RGB color translator
    function hsvToRgb(h, s, v) {{
        let r, g, b;
        let i = Math.floor(h * 6);
        let f = h * 6 - i;
        let p = v * (1 - s);
        let q = v * (1 - f * s);
        let t = v * (1 - (1 - f) * s);
        switch (i % 6) {{
            case 0: r = v, g = t, b = p; break;
            case 1: r = q, g = v, b = p; break;
            case 2: r = p, g = v, b = t; break;
            case 3: r = p, g = q, b = v; break;
            case 4: r = t, g = p, b = v; break;
            case 5: r = v, g = p, b = q; break;
        }}
        return `rgb(${{Math.floor(r * 255)}}, ${{Math.floor(g * 255)}}, ${{Math.floor(b * 255)}})`;
    }}

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    
    // UI control variables passed straight from Streamlit sliders
    const maxIterations = {max_iterations};
    const cycles = {cycles};
    const renderSpeed = {render_speed};
    const scaleFactor = {size_scale};
    const useGlow = {glow_str};

    let i = 0;

    function renderEngineLoop() {{
        // Rendering multiple computation loops per frame matching top-tier graphics hardware rendering
        for (let batch = 0; batch < renderSpeed; batch++) {{
            if (i >= maxIterations) return;

            let hue = i / maxIterations;
            let neonColor = hsvToRgb(hue, 1.0, 1.0);
            let contrastFill = hsvToRgb((hue + 0.5) % 1.0, 0.85, 0.25);

            // Vector matrix mathematical spirals formula mirroring screen coordinate shifts
            let angle = i * (360 / cycles) + (i * 0.5);
            let angleRad = angle * Math.PI / 180;
            
            // Adjust distance scaling based on dynamically sizing canvas resolutions
            let baseDistance = Math.sqrt(i) * (canvas.width * 0.035); 

            let targetX = cx + Math.cos(angleRad) * baseDistance;
            let targetY = cy + Math.sin(angleRad) * baseDistance;

            ctx.save();
            ctx.translate(targetX, targetY);
            ctx.rotate(angleRad);

            // Premium algorithmic structural glow shadows injections
            if(useGlow) {{
                ctx.shadowBlur = 18;
                ctx.shadowColor = neonColor;
            }}

            ctx.beginPath();
            let size = i * (canvas.width * scaleFactor * 0.003); 
            let curX = 0, curY = 0;
            let internalRot = 0;

            ctx.moveTo(curX, curY);

            // Computational loops for drawing advanced star geometries
            for (let j = 0; j < 5; j++) {{
                curX += Math.cos(internalRot) * size;
                curY += Math.sin(internalRot) * size;
                ctx.lineTo(curX, curY);
                
                internalRot += 144 * Math.PI / 180;
                
                curX += Math.cos(internalRot) * size;
                curY += Math.sin(internalRot) * size;
                ctx.lineTo(curX, curY);
                
                internalRot -= 72 * Math.PI / 180;
            }}

            ctx.closePath();

            ctx.fillStyle = contrastFill;
            ctx.fill();
            
            ctx.strokeStyle = neonColor;
            ctx.lineWidth = Math.abs(Math.sin(i * 0.05)) * 2.0 + 0.5;
            ctx.stroke();

            ctx.restore();
            
            i++;
            nodeCounter.innerText = i + " / " + maxIterations;
        }}
        requestAnimationFrame(renderEngineLoop);
    }}

    // Start engine core loops
    renderEngineLoop();
</script>
</body>
</html>
"""

# Dynamic high-performance view window embedding inside main grid blocks
components.html(premium_graphics_html, height=620, scrolling=False)
