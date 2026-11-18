
import pickle
import streamlit as st

st.set_page_config(
    page_title="AutoValue | Toyota Price Estimator",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================
# LOAD MODEL
# =====================================
@st.cache_resource
def load_model():
    with open("estimasi_mobil.sav", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception:
    st.error("File estimasi_mobil.sav tidak ditemukan.")
    st.stop()

# =====================================
# THEME
# =====================================
if "theme" not in st.session_state:
    st.session_state.theme = "Gelap"

# =====================================
# THEME COLORS
# =====================================
if st.session_state.theme == "Gelap":
    bg = "#10151C"
    panel = "#19212B"
    panel2 = "#202B38"
    text = "#F1F4F8"
    muted = "#A0ACBA"
    border = "#303C4A"
    accent = "#8DAECC"
    input_bg = "#202B38"
    metric_bg = "#19212B"
else:
    bg = "#F3F5F8"
    panel = "#FFFFFF"
    panel2 = "#F0F3F7"
    text = "#202A36"
    muted = "#748091"
    border = "#DFE4EA"
    accent = "#344F6B"
    input_bg = "#FFFFFF"
    metric_bg = "#FFFFFF"

# =====================================
# CSS
# =====================================
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {{
    background: {bg};
    color: {text};
    font-family: 'Inter', sans-serif;
}}

header[data-testid="stHeader"] {{
    background: {bg};
}}

.block-container {{
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}}

h1, h2, h3, p, label {{
    font-family: 'Inter', sans-serif;
    color: {text};
}}

/* NAVBAR */
.navbar {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid {border};
    padding: 5px 0 20px 0;
    margin-bottom: 28px;
}}

.logo {{
    font-size: 23px;
    font-weight: 800;
    letter-spacing: -1px;
    color: {text};
}}

.logo span {{
    color: {accent};
}}

.logo-sub {{
    font-size: 9px;
    letter-spacing: 2.5px;
    color: {muted};
    margin-top: 4px;
}}

/* HERO */
.hero {{
    background: {panel};
    border: 1px solid {border};
    border-radius: 14px;
    padding: 38px;
    min-height: 260px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.hero-tag {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    color: {accent};
    margin-bottom: 18px;
}}

.hero h1 {{
    color: {text};
    font-size: 36px;
    line-height: 1.25;
    letter-spacing: -1.5px;
    font-weight: 800;
    margin: 0 0 15px 0;
}}

.hero p {{
    color: {muted};
    font-size: 13px;
    line-height: 1.9;
    margin: 0;
    max-width: 590px;
}}

.hero-visual {{
    height: 260px;
    background: linear-gradient(145deg, {panel2}, {panel});
    border: 1px solid {border};
    border-radius: 14px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}}

.visual-label {{
    font-size: 10px;
    letter-spacing: 3px;
    color: {muted};
    font-weight: 700;
}}

.visual-number {{
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -3px;
    color: {accent};
    margin: 12px 0;
}}

.visual-caption {{
    color: {muted};
    font-size: 11px;
    letter-spacing: 1px;
}}

/* SECTION */
.section-title {{
    color: {text};
    font-size: 19px;
    font-weight: 700;
    margin: 30px 0 5px 0;
}}

.section-subtitle {{
    color: {muted};
    font-size: 12px;
    margin-bottom: 18px;
}}

/* FORM */
div[data-testid="stForm"] {{
    background: {panel};
    border: 1px solid {border};
    border-radius: 14px;
    padding: 25px;
}}

div[data-testid="stForm"] label {{
    color: {text} !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}}

div[data-baseweb="input"] {{
    background: {input_bg};
    border: 1px solid {border};
    border-radius: 7px;
}}

div[data-baseweb="input"] input {{
    color: {text} !important;
    -webkit-text-fill-color: {text} !important;
}}

div[data-testid="stFormSubmitButton"] button {{
    background: {accent};
    color: #101820;
    border: none;
    border-radius: 7px;
    height: 46px;
    font-weight: 700;
    letter-spacing: 1px;
    transition: 0.2s;
}}

div[data-testid="stFormSubmitButton"] button:hover {{
    background: #A9C1D8;
    color: #101820;
}}

/* RESULT */
.result-card {{
    background: {panel};
    border: 1px solid {border};
    border-radius: 14px;
    padding: 25px;
    margin-top: 25px;
}}

.result-label {{
    color: {muted};
    font-size: 10px;
    letter-spacing: 2px;
    font-weight: 700;
}}

.result-price {{
    color: {accent};
    font-size: 35px;
    font-weight: 800;
    margin-top: 12px;
    overflow-wrap: anywhere;
}}

.result-note {{
    color: {muted};
    font-size: 12px;
    margin-top: 5px;
}}

div[data-testid="stMetric"] {{
    background: {metric_bg};
    border: 1px solid {border};
    border-radius: 10px;
    padding: 18px;
}}

div[data-testid="stMetricLabel"] {{
    color: {muted};
}}

div[data-testid="stMetricValue"] {{
    color: {text};
    font-size: 21px;
}}

.info-box {{
    background: {panel2};
    border: 1px solid {border};
    border-radius: 9px;
    padding: 16px 19px;
    color: {muted};
    font-size: 11px;
    line-height: 1.8;
    margin-top: 18px;
}}

.footer {{
    border-top: 1px solid {border};
    margin-top: 45px;
    padding-top: 20px;
    text-align: center;
    color: {muted};
    font-size: 10px;
    letter-spacing: 1px;
}}

#MainMenu, footer {{
    visibility: hidden;
}}

@media(max-width: 700px) {{
    .hero {{
        padding: 25px;
    }}
    .hero h1 {{
        font-size: 27px;
    }}
    .hero-visual {{
        height: 170px;
    }}
    .result-price {{
        font-size: 27px;
    }}
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# NAVBAR + THEME SELECTOR
# =====================================
nav1, nav2 = st.columns([5, 1])

with nav1:
    st.markdown("""
    <div style="padding-top:5px">
        <div class="logo">AUTO<span>VALUE</span></div>
        <div class="logo-sub">AUTOMOTIVE PRICE INTELLIGENCE</div>
    </div>
    """, unsafe_allow_html=True)

with nav2:
    selected_theme = st.selectbox(
        "Theme",
        ["Gelap", "Terang"],
        index=0 if st.session_state.theme == "Gelap" else 1,
        label_visibility="collapsed"
    )

if selected_theme != st.session_state.theme:
    st.session_state.theme = selected_theme
    st.rerun()

# =====================================
# HERO SECTION
# =====================================
hero1, hero2 = st.columns([1.6, 1])

with hero1:
    st.markdown("""
    <div class="hero">
        <div class="hero-tag">TOYOTA · USED CAR ESTIMATOR</div>
        <h1>Discover Your Car's<br>Estimated Value.</h1>
        <p>
            Dapatkan estimasi harga mobil bekas Toyota berdasarkan
            spesifikasi kendaraan dengan teknologi Machine Learning.
            Masukkan detail kendaraan untuk mengetahui perkiraan nilainya.
        </p>
    </div>
    """, unsafe_allow_html=True)

with hero2:
    st.markdown("""
    <div class="hero-visual">
        <div class="visual-label">AUTOMOTIVE INTELLIGENCE</div>
        <div class="visual-number">AV.</div>
        <div class="visual-caption">SMART VEHICLE VALUATION</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# INPUT FORM
# =====================================
st.markdown("""
<div class="section-title">Vehicle Information</div>
<div class="section-subtitle">
    Masukkan spesifikasi kendaraan untuk mendapatkan hasil estimasi.
</div>
""", unsafe_allow_html=True)

with st.form("form_estimasi"):
    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Tahun Produksi",
            min_value=1990,
            max_value=2026,
            value=2018,
            step=1
        )

        mileage = st.number_input(
            "Jarak Tempuh (KM)",
            min_value=0,
            value=30000,
            step=1000
        )

        tax = st.number_input(
            "Pajak Mobil",
            min_value=0,
            value=150,
            step=10
        )

    with col2:
        mpg = st.number_input(
            "Konsumsi BBM (MPG)",
            min_value=0.0,
            value=55.0,
            step=1.0
        )

        engineSize = st.number_input(
            "Ukuran Mesin (Engine Size)",
            min_value=0.0,
            value=1.5,
            step=0.1
        )

    st.write("")
    submit = st.form_submit_button(
        "CALCULATE ESTIMATED PRICE",
        use_container_width=True
    )

# =====================================
# PREDICTION
# =====================================
if submit:
    try:
        data_mobil = [[
            year,
            mileage,
            tax,
            mpg,
            engineSize
        ]]

        hasil_prediksi = model.predict(data_mobil)
        harga_pounds = float(hasil_prediksi[0])

        kurs = 19000
        harga_rupiah = harga_pounds * kurs
        harga_juta = harga_rupiah / 1_000_000

        st.markdown(f"""
        <div class="result-card">
            <div class="result-label">ESTIMATED VEHICLE VALUE</div>
            <div class="result-price">£ {harga_pounds:,.2f}</div>
            <div class="result-note">
                Estimated price in Poundsterling
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        result1, result2 = st.columns(2)

        with result1:
            st.metric(
                "Estimasi Harga dalam Rupiah",
                f"Rp {harga_rupiah:,.0f}"
            )

        with result2:
            st.metric(
                "Estimasi Harga dalam Juta",
                f"Rp {harga_juta:,.2f} juta"
            )

        st.markdown("""
        <div class="info-box">
            <b>Disclaimer:</b> Hasil merupakan estimasi berdasarkan model
            Machine Learning, bukan harga jual pasti. Konversi Rupiah
            menggunakan asumsi kurs tetap Rp19.000 per Poundsterling.
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")

# =====================================
# FOOTER
# =====================================
st.markdown("""
<div class="footer">
    AUTO VALUE &nbsp; | &nbsp; TOYOTA USED CAR PRICE ESTIMATOR
    <br><br>
    POWERED BY MACHINE LEARNING
</div>
""", unsafe_allow_html=True)
