import streamlit as st

# --- CEHA BRANDING & DESIGN (DARK MODE - MINIMALIST - V8.1) ---
st.set_page_config(page_title="ceha-Energieberatung | WP-Check", layout="centered")

# Hilfsfunktion für die Formatierung (Tausenderpunkt, keine Nachkommastellen)
def fmt(wert):
    return f"{int(wert):,}".replace(",", ".")

# --- SESSION STATE INITIALISIERUNG ---
if 'verbrauch_input' not in st.session_state:
    st.session_state['verbrauch_input'] = 2500.0

def handle_change():
    """ Callback: Passt den Verbrauchswert an, wenn der Energieträger gewechselt wird """
    et = st.session_state.et_select
    if et == "Erdgas":
        st.session_state.verbrauch_input = 20000.0
    elif et == "Heizöl":
        st.session_state.verbrauch_input = 2500.0
    elif et == "Flüssiggas":
        st.session_state.verbrauch_input = 3500.0

st.markdown("""
    <style>
    /* Haupt-Hintergrund */
    .stApp { 
        background-color: #0e1117; 
        color: #ffffff;
    }
    
    /* --- MINIMALIST INPUT STYLING --- */
    label, div[data-testid="stWidgetLabel"] p {
        color: #ffffff !important;
        font-weight: 600 !important;
        margin-bottom: 5px !important;
    }

    div[data-testid="stRadio"] label div p {
        color: #ffffff !important;
    }

    /* Minimalistische Eingabefelder (nur untere Linie) */
    div[data-baseweb="select"], div[data-baseweb="input"], .stNumberInput div {
        background-color: transparent !important;
        border: none !important;
        border-bottom: 1px solid #444 !important;
        border-radius: 0px !important;
        color: #ffffff !important;
        padding-left: 0px !important;
    }

    div[data-baseweb="select"]:focus-within, div[data-baseweb="input"]:focus-within {
        border-bottom: 2px solid #e65500 !important;
    }

    input {
        color: #ffffff !important;
    }

    /* Dropdown-Menü Liste */
    div[role="listbox"] {
        background-color: #1e1e1e !important;
        border: 1px solid #333 !important;
    }
    div[role="option"] {
        color: #ffffff !important;
    }
    div[role="option"]:hover {
        background-color: #e65500 !important;
    }

    /* --- SLIDER FARBANPASSUNG (CEHA ORANGE) --- */
    .stSlider [data-baseweb="slider"] > div [style*="background-color: rgb(255, 75, 75)"],
    .stSlider [data-baseweb="slider"] > div [style*="background-color: #ff4b4b"],
    .stSlider [data-baseweb="slider"] > div [style*="background-image: linear-gradient"] {
        background-color: #e65500 !important;
        background-image: none !important;
    }
    .stSlider [data-baseweb="slider"] [role="slider"] {
        background-color: #e65500 !important;
        border: 2px solid #ffffff !important;
    }

    .stSelectbox, .stNumberInput, .stSlider, .stRadio { margin-bottom: 40px !important; }

    .ceha-header {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 48px;
        font-weight: 900;
        color: #ffffff;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .ceha-line { background-color: #e65500; height: 6px; width: 120px; margin-bottom: 30px; }
    .header-container { display: flex; align-items: center; margin-top: 25px; margin-bottom: 15px; }
    .orange-dot { height: 12px; width: 12px; background-color: #e65500; margin-right: 15px; flex-shrink: 0; }
    .custom-subheader { color: #ffffff !important; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; font-size: 1.25rem; margin: 0; }

    .promo-box { 
        background-color: #1e1e1e; 
        padding: 25px; 
        border-radius: 5px; 
        border-left: 5px solid #e65500; 
        margin-bottom: 35px; 
        line-height: 1.6;
        color: #dddddd;
    }

    div[data-testid="stAlert"] > div { border: none !important; }
    div[data-testid="stAlert"] p { color: #ffffff !important; font-weight: 600 !important; }
    div[data-testid="stAlert"] svg { fill: #ffffff !important; }

    div[data-testid="stAlert"] > div[style*="rgba(0, 200, 83,"] { background-color: #00c853 !important; }
    div[data-testid="stAlert"] > div[style*="rgba(33, 150, 243,"] { background-color: #2196f3 !important; }
    div[data-testid="stAlert"] > div[style*="rgba(255, 171, 0,"] { background-color: #ffab00 !important; }
    div[data-testid="stAlert"] > div[style*="rgba(255, 171, 0,"] p { color: #000000 !important; }

    .stButton > button { 
        background-color: #e65500; 
        color: white !important; 
        border-radius: 4px; 
        font-weight: bold;
        padding: 12px;
        width: 100%;
        border: none;
    }

    div[data-testid="stMetric"] { 
        background-color: #1e1e1e !important; 
        padding: 20px; 
        border-radius: 5px; 
        border-bottom: 4px solid #e65500;
    }
    div[data-testid="stMetricValue"] { color: #ffffff !important; }
    div[data-testid="stMetricLabel"] { color: #aaaaaa !important; }

    .wp-bedarf-box { 
        background-color: #1e1e1e; 
        padding: 25px; 
        border-left: 10px solid #e65500; 
        border-radius: 4px;
        text-align: center; 
    }

    .disclaimer-box { 
        font-size: 12px; 
        color: #888888; 
        line-height: 1.4; 
        margin-top: 40px; 
        padding: 15px; 
        border-top: 1px solid #333; 
    }
    hr { border-top: 2px solid #e65500 !important; opacity: 0.5; }
    </style>
    """, unsafe_allow_html=True)

def render_header(text):
    st.markdown(f'<div class="header-container"><div class="orange-dot"></div><p class="custom-subheader">{text}</p></div>', unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="ceha-header">CEHA</p><div class="ceha-line"></div>', unsafe_allow_html=True)
st.header("Ihre Zukunft heizt mit System")

st.markdown("""
<div class="promo-box">
    <strong>Moderne Wärmepumpen sind die perfekte Heizlösung – auch im Bestand.</strong><br>
    Vergessen Sie die Mythen, dass eine Wärmepumpe nur mit Fußbodenheizung oder in kernsanierten Häusern funktioniert. Mit der richtigen Fachplanung lässt sich fast jedes Gebäude effizient umrüsten.<br><br>
    Wir von <strong>CEHA</strong> machen den Umstieg für Sie einfach: Wir berechnen die optimale Systemauslegung und bieten Ihnen <strong>umfassende Unterstützung bei Förderanträgen</strong>. 
    Wir führen Sie sicher durch den Dschungel der Förderkriterien und helfen Ihnen dabei, alle notwendigen Voraussetzungen für die bestmöglichen Zuschüsse zu erfüllen. 
    So wird Ihr Projekt technisch perfekt und auch finanziell eine "feine Sache".<br><br>
    Nutzen Sie unseren Rechner für eine erste Einschätzung – für die fachmännische Planung und Begleitung bei der Förderung stehen wir Ihnen persönlich zur Seite.
</div>
""", unsafe_allow_html=True)

st.link_button("Jetzt Beratung & Förder-Support anfragen", "https://www.ceha-energieberatung.de/kontakt")
st.divider()

# --- 1. GEBÄUDEDATEN ---
render_header("1. Gebäude-Bestandsdaten")
modus = st.radio("Datengrundlage wählen:", ["Realer Verbrauch (Bestand)", "Berechneter Bedarf (Heizlast)"], horizontal=True)

waermebedarf, aktuelle_kosten, eta, co2_alt = 0.0, 0.0, 1.0, 0.0

if "Verbrauch" in modus:
    c1, c2, c3 = st.columns([3, 1.5, 1.5])
    with c1:
        energietraeger = st.selectbox(
            "Energieträger", 
            ["Heizöl", "Erdgas", "Flüssiggas"], 
            key="et_select", 
            on_change=handle_change
        )
        baujahr_auswahl = st.selectbox("Kesselbaujahr (Technik)", ["Vor 1985 (Konstanttemperaturkessel)", "1985 - 2005 (Niedertemperaturkessel)", "Ab 2006 (Brennwertgerät)"])
        eta = 0.78 if "Konstant" in baujahr_auswahl else (0.86 if "Nieder" in baujahr_auswahl else 0.94)
        co2_faktor_alt = 0.266 if energietraeger == "Heizöl" else (0.202 if energietraeger == "Erdgas" else 0.229)
    with c2:
        unit = "Liter/Jahr" if energietraeger != "Erdgas" else "kWh/Jahr"
        verbrauch = st.number_input(unit, min_value=0.0, step=100.0, key="verbrauch_input")
    with c3:
        preis_alt = st.number_input("Preis/Einheit (€)", value=1.05 if energietraeger != "Erdgas" else 0.12, step=0.01)
        aktuelle_kosten = verbrauch * preis_alt
        if energietraeger == "Heizöl": 
            waermebedarf = verbrauch * 9.8 * eta
            co2_alt = verbrauch * 9.8 * co2_faktor_alt
        elif energietraeger == "Erdgas": 
            waermebedarf = verbrauch * eta if verbrauch > 8000 else verbrauch * 10.3 * eta
            co2_alt = verbrauch * co2_faktor_alt
        else: 
            waermebedarf = verbrauch * 6.57 * eta
            co2_alt = verbrauch * 6.57 * co2_faktor_alt
    st.caption(f"Angenommener Wirkungsgrad Altanlage: {eta*100:.0f}%")
else:
    col_last, col_pers, col_kosten = st.columns([2, 1.5, 1.5])
    with col_last: heizlast = st.number_input("Norm-Heizlast (kW)", min_value=0.0, value=12.0, step=0.5)
    with col_pers: bewohner = st.number_input("Bewohner", min_value=1, value=4, step=1)
    with col_kosten: aktuelle_kosten = st.number_input("Aktuelle Heizkosten (€)", value=2800.0, step=50.0)
    waermebedarf = (heizlast * 2100) + (bewohner * 800)
    co2_alt = waermebedarf * 0.23

st.divider()

# --- 2. TECHNIK ---
render_header("2. Technisches Konzept")
standard_wahl = st.radio("Berechnungsverfahren auswählen:", ["Moderner Technikstandard", "VDI 4650 (Konservative Normrechnung)"], horizontal=True)
sys_col, temp_col = st.columns(2)
with sys_col: 
    heizsystem = st.selectbox("Anlage-Hydraulik", ["1. Fußbodenheizung (FBH)", "2. Radiatorheizung (Heizkörper)", "3. Mischsystem (EG: FBH / OG: Radiatoren)"])

# Logik für die differenzierten Vorlauftemperaturen
if "1." in heizsystem: # FBH
    d, m = 35, 50
elif "2." in heizsystem: # Radiator
    d, m = 55, 70
else: # 3. Mischsystem
    d, m = 45, 60

with temp_col:
    vorlauf = st.slider("Vorlauftemperatur (°C)", 30, m, d)

# --- JAZ LOGIK ---
jaz_basis = 6.45 - (0.078 * vorlauf) + (0.0004 * (vorlauf**2))
if "Moderner Technikstandard" in standard_wahl:
    jaz = jaz_basis
else:
    jaz = jaz_basis * 0.90
jaz = max(2.3, min(jaz, 5.5))

st.divider()

# --- 3. STROMTARIF & VERGLEICH ---
render_header("3. Stromtarif & Vergleich")
strombedarf_wp = waermebedarf / jaz
# Formatierung angewendet: fmt(strombedarf_wp)
st.markdown(f'<div class="wp-bedarf-box"><small style="color: #aaaaaa;">ERRECHNETER STROMBEDARF</small><br><span style="font-size: 32px; font-weight: bold; color: #e65500;">{fmt(strombedarf_wp)} kWh / Jahr</span></div>', unsafe_allow_html=True)

col_links, col_preis = st.columns([1.5, 1])
with col_links:
    st.write("Finden Sie den besten Tarif für Ihr Projekt:")
    st.link_button("Check24 Vergleich", "https://www.check24.de/strom/vergleich/")
with col_preis:
    strompreis_euro = st.number_input("Strompreis (€/kWh)", value=0.285, step=0.005, format="%.3f")

stromkosten_wp = strombedarf_wp * strompreis_euro
ersparnis = aktuelle_kosten - stromkosten_wp
co2_wp = strombedarf_wp * 0.380
co2_ersparnis = co2_alt - co2_wp

st.divider()

# --- ERGEBNISSE ---
render_header("Prognose-Ergebnis")
c_res1, c_res2 = st.columns(2)
with c_res1:
    if ersparnis > 0: st.success(f"**Finanzielle Ersparnis:** ca. {ersparnis:,.2f} € / Jahr")
    else: st.warning(f"**Differenzkosten:** ca. {abs(ersparnis):,.2f} € / Jahr")
with c_res2:
    st.info(f"**CO2-Einsparung:** {co2_ersparnis/1000:,.2f} Tonnen / Jahr")

m1, m2, m3 = st.columns(3)
m1.metric("Arbeitszahl (JAZ)", f"{jaz:.2f}")
# Formatierung angewendet: fmt(strombedarf_wp)
m2.metric("Strombedarf", f"{fmt(strombedarf_wp)} kWh")
m3.metric("Heizkosten Neu", f"{stromkosten_wp:,.2f} €")

st.markdown("<br>", unsafe_allow_html=True)
st.link_button("Jetzt Beratung & Förder-Support anfragen", "https://www.ceha-energieberatung.de/kontakt")
st.caption("© CEHA ENERGIEBERATUNG UG (haftungsbeschränkt)")

st.markdown(f"""
    <div class="disclaimer-box">
        <strong>Rechtlicher Hinweis:</strong> Diese Online-Prognose dient ausschließlich der unverbindlichen Erstinformation und Orientierung. 
        Sie ersetzt keine individuelle Fachplanung, Heizlastberechnung nach DIN 12831 oder Vor-Ort-Energieberatung. 
        Trotz sorgfältiger Programmierung wird für die Richtigkeit, Vollständigkeit und Aktualität der berechneten Werte sowie für daraus resultierende 
        Investitionsentscheidungen keine Haftung übernommen. Maßgeblich für Förderungen und technische Auslegungen sind ausschließlich die 
        individuellen Berechnungen im Rahmen einer persönlichen Beratung.
    </div>
""", unsafe_allow_html=True)
