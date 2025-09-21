import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch
import numpy as np

def draw_sunflower(ax, x, y, scale=1.0, petal_count=18):
    # pétalos
    petal_length = 0.6 * scale
    petal_width = 0.25 * scale
    angles = np.linspace(0, 2*np.pi, petal_count, endpoint=False)
    for a in angles:
        e = Ellipse((x + np.cos(a) * 0.25 * scale, y + np.sin(a) * 0.25 * scale),
                    width=petal_length, height=petal_width,
                    angle=np.degrees(a), linewidth=0, facecolor="#FFD700")
        ax.add_patch(e)

    # centro marrón
    c = Circle((x, y), 0.18*scale, color="#5A331F")
    ax.add_patch(c)

def draw_stem(ax, x0, y0, x1, y1):
    t = np.linspace(0,1,100)
    ctrl_x = (x0 + x1)/2 + 0.2*(x1-x0)
    ctrl_y = min(y0, y1) - 0.5*(abs(y1-y0)+0.2)
    xs = (1-t)**2 * x0 + 2*(1-t)*t*ctrl_x + t**2 * x1
    ys = (1-t)**2 * y0 + 2*(1-t)*t*ctrl_y + t**2 * y1
    ax.plot(xs, ys, linewidth=6, color="#2E7D32")

def draw_bouquet():
    fig, ax = plt.subplots(figsize=(5,7))
    ax.set_xlim(-2,2)
    ax.set_ylim(-3,3)
    ax.set_aspect("equal")
    ax.axis("off")

    flower_positions = [(-0.9, 1.0, 0.9),
                        (-0.3, 1.4, 1.0),
                        (0.3, 1.2, 0.9),
                        (0.9, 1.5, 1.05),
                        (-0.5, 0.6, 0.85),
                        (0.5, 0.7, 0.85)]

    for (fx, fy, scale) in flower_positions:
        draw_stem(ax, fx, fy-0.15*scale, 0, -2.5)
        draw_sunflower(ax, fx, fy, scale=scale, petal_count=18)

    # envoltorio en la base
    wrap = FancyBboxPatch((-0.4,-2.8),0.8,0.6,
                          boxstyle="Round,pad=0.05,rounding_size=0.15",
                          facecolor="#8B5A2B")
    ax.add_patch(wrap)
    return fig

# --- Streamlit ---
st.set_page_config(page_title="Ramo de Girasoles", page_icon="🌻", layout="centered")

st.title("🌻 Ramo de Girasoles Amarillos")
st.write("Un ramo virtual creado con Python y Streamlit.")

# mostrar ramo
fig = draw_bouquet()
st.pyplot(fig)

# mensaje romántico
st.markdown(
    """
    <div style="text-align: center; font-size:20px; color:#333; margin-top:20px;">
    <b>“Eres lo que más Amo y lo que más Adoro,<br>
    te amo tanto que espero que sepas y entiendas<br>
    que todo lo que siento por ti es verdadero,<br>
    nos veremos más tarde cuando te vaya a recoger macaca.”</b>
    </div>
    """ ,
    unsafe_allow_html=True
)
