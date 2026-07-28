import streamlit as st
import requests

# ====================== CONFIG ======================
st.set_page_config(
    page_title="blkn.lachiti",
    page_icon="⛧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== CSS SATANIC ANIMAT ======================
st.markdown("""
<style>
    .stApp {
        background: radial-gradient(ellipse at center, #1a0000 0%, #0a0a0a 70%);
        color: #e0e0e0;
        overflow-x: hidden;
    }

    .stApp::before {
        content: "⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧ ⛧";
        position: fixed;
        top: 0;
        left: 0;
        width: 200%;
        height: 200%;
        font-size: 3rem;
        color: rgba(139, 0, 0, 0.15);
        animation: floatPentagrams 40s linear infinite;
        pointer-events: none;
        z-index: 0;
        letter-spacing: 40px;
        line-height: 80px;
        white-space: pre-wrap;
        word-break: break-all;
    }

    @keyframes floatPentagrams {
        0% { transform: translateY(0) rotate(0deg); }
        100% { transform: translateY(-50%) rotate(10deg); }
    }

    h1, h2, h3 {
        color: #c41e3a !important;
        font-family: Georgia, serif;
        text-shadow: 0 0 10px #8B0000, 0 0 20px #8B0000, 0 0 40px #4a0000;
        animation: pulseGlow 3s ease-in-out infinite;
    }

    @keyframes pulseGlow {
        0%, 100% { text-shadow: 0 0 10px #8B0000, 0 0 20px #8B0000; }
        50% { text-shadow: 0 0 20px #c41e3a, 0 0 40px #c41e3a, 0 0 60px #8B0000; }
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111111 0%, #1a0000 100%);
        border-right: 2px solid #8B0000;
        box-shadow: 5px 0 20px rgba(139, 0, 0, 0.4);
    }

    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(90deg, #8B0000, #4a0000) !important;
        color: white !important;
        border: 1px solid #c41e3a !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-size: 0.9rem !important;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px rgba(139, 0, 0, 0.5);
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #c41e3a, #8B0000) !important;
        box-shadow: 0 0 25px rgba(196, 30, 58, 0.8);
        transform: scale(1.03);
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #1a1a1a !important;
        color: #e0e0e0 !important;
        border: 1px solid #8B0000 !important;
        border-radius: 6px !important;
    }

    img {
        max-width: 100% !important;
        height: auto !important;
        border-radius: 10px;
        border: 2px solid #8B0000;
        box-shadow: 0 0 15px rgba(139, 0, 0, 0.5);
        transition: all 0.4s ease;
    }
    img:hover {
        box-shadow: 0 0 30px rgba(196, 30, 58, 0.8);
        transform: scale(1.03);
    }

    [data-testid="stMetric"] {
        background: rgba(30, 0, 0, 0.6);
        border: 1px solid #8B0000;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 15px rgba(139, 0, 0, 0.3);
    }

    @media (max-width: 768px) {
        .stApp { padding: 0.5rem !important; }
        h1 { font-size: 1.8rem !important; }
        h2 { font-size: 1.3rem !important; }
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #8B0000, transparent);
    }

    .stCaption {
        color: #666 !important;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ====================== PAROLĂ ADMIN ======================
if "admin" not in st.session_state:
    st.session_state.admin = False

# ====================== SIDEBAR ======================
st.sidebar.markdown("## ⛧ blkn.lachiti")
st.sidebar.markdown("---")

pagina = st.sidebar.radio(
    "Navigare",
    ["🏠 Acasă", "🖼️ Galerie", "📜 Despre", "📞 Contact"],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")

with st.sidebar.expander("🔒 Admin", expanded=False):
    parola = st.text_input("Parolă", type="password", key="parola_admin")
    if st.button("Intră"):
        if parola == "lachita2026":
            st.session_state.admin = True
            st.success("Acces acordat")
            st.rerun()
        else:
            st.error("Parolă greșită")

    if st.session_state.admin:
        if st.button("Ieși din Admin"):
            st.session_state.admin = False
            st.rerun()

st.sidebar.caption("© 2026 blkn.lachiti")

# ====================== VALORI IMPLICITE ======================
defaults = {
    "titlu": "blkn.lachiti",
    "subtitlu": "Portalul întunecat",
    "descriere": "Bine ai venit în tărâmul umbrelor.\nSite-ul funcționează pe telefon, tabletă și PC.",
    "despre_titlu": "Cine suntem",
    "despre_text": "Scrie aici tot ce vrei să apară pe pagina Despre.",
    "contact_text": "Email: contact@blkn.lachiti\nInstagram: @blkn.lachiti\nDiscord: blkn#0000",
    "url1": "",
    "url2": "",
    "url3": "",
    "url4": "",
    "url5": "",
    "url6": "",
    "video1": "",
    "video2": "",
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ====================== PAGINA: ACASĂ ======================
if pagina == "🏠 Acasă":

    if st.session_state.admin:
        st.title("⛧ Setări Acasă (doar tu vezi)")
        st.session_state.titlu = st.text_input("Titlu principal", value=st.session_state.titlu)
        st.session_state.subtitlu = st.text_input("Subtitlu", value=st.session_state.subtitlu)
        st.session_state.descriere = st.text_area("Descriere", value=st.session_state.descriere, height=100)
        st.markdown("---")

    st.title(f"⛧ {st.session_state.titlu}")
    st.subheader(st.session_state.subtitlu)
    st.write(st.session_state.descriere)

    st.markdown("---")

    c1, c2, c3 = st.columns(3)
    c1.metric("Imagini", "6")
    c2.metric("Video", "2")
    c3.metric("Atmosferă", "Satanică")

# ====================== PAGINA: GALERIE ======================
elif pagina == "🖼️ Galerie":
    st.title("🖼️ Galerie")

    if st.session_state.admin:
        st.caption("🔐 Mod Admin – lipește linkuri de poze și video")

        st.markdown("##### Link-uri Poze")
        col_a, col_b = st.columns(2)
        with col_a:
            st.session_state.url1 = st.text_input("Poză 1", value=st.session_state.url1)
            st.session_state.url2 = st.text_input("Poză 2", value=st.session_state.url2)
            st.session_state.url3 = st.text_input("Poză 3", value=st.session_state.url3)
        with col_b:
            st.session_state.url4 = st.text_input("Poză 4", value=st.session_state.url4)
            st.session_state.url5 = st.text_input("Poză 5", value=st.session_state.url5)
            st.session_state.url6 = st.text_input("Poză 6", value=st.session_state.url6)

        st.markdown("##### Link-uri Filmări")
        st.session_state.video1 = st.text_input("Video 1", value=st.session_state.video1)
        st.session_state.video2 = st.text_input("Video 2", value=st.session_state.video2)

        st.markdown("---")

    # ===== POZE (mai mici) =====
    st.subheader("📸 Poze")

    # Rând 1
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**ella lachita**")
        if st.session_state.url1:
            st.image(st.session_state.url1, use_container_width=True)
    with c2:
        st.markdown("**ella lachita**")
        if st.session_state.url2:
            st.image(st.session_state.url2, use_container_width=True)
    with c3:
        st.markdown("**ella lachita**")
        if st.session_state.url3:
            st.image(st.session_state.url3, use_container_width=True)

    # Rând 2
    c4, c5, c6 = st.columns(3)
    with c4:
        st.markdown("**ella lachita**")
        if st.session_state.url4:
            st.image(st.session_state.url4, use_container_width=True)
    with c5:
        st.markdown("**ella lachita**")
        if st.session_state.url5:
            st.image(st.session_state.url5, use_container_width=True)
    with c6:
        st.markdown("**ella lachita**")
        if st.session_state.url6:
            st.image(st.session_state.url6, use_container_width=True)

    st.markdown("---")

    # ===== VIDEO =====
    st.subheader("🎬 Filmări")

    v1, v2 = st.columns(2)
    with v1:
        if st.session_state.video1:
            st.video(st.session_state.video1)
        else:
            st.info("Niciun video")
    with v2:
        if st.session_state.video2:
            st.video(st.session_state.video2)
        else:
            st.info("Niciun video")

# ====================== PAGINA: DESPRE ======================
elif pagina == "📜 Despre":
    st.title("📜 Despre")

    if st.session_state.admin:
        st.session_state.despre_titlu = st.text_input("Titlu secțiune", value=st.session_state.despre_titlu)
        st.session_state.despre_text = st.text_area("Textul tău", value=st.session_state.despre_text, height=200)
        st.markdown("---")

    st.header(st.session_state.despre_titlu)
    st.write(st.session_state.despre_text)

# ====================== PAGINA: CONTACT ======================
elif pagina == "📞 Contact":
    st.title("📞 Contact")

    if st.session_state.admin:
        st.session_state.contact_text = st.text_area("Informații de contact", value=st.session_state.contact_text,
                                                     height=150)
        st.markdown("---")

    st.write(st.session_state.contact_text)

    st.markdown("### Trimite un mesaj")
    with st.form("formular_contact"):
        nume = st.text_input("Numele tău")
        mesaj = st.text_area("Mesajul")
        trimite = st.form_submit_button("Trimite ⛧")

        if trimite:
            st.success(f"Mesajul de la **{nume}** a fost înregistrat.")

# ====================== FOOTER ======================
st.markdown("---")
st.caption("⛧ blkn.lachiti — 2026 • Funcționează pe telefon & PC")
