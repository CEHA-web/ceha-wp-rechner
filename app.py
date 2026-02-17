import streamlit as st

# --- CEHA BRANDING & DESIGN ---
st.set_page_config(page_title="ceha-Energieberatung | WP-Check", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #f2f2f2; }
    
    /* ABSTÄNDE OPTIMIEREN */
    div[data-testid="stWidgetLabel"] p {
        margin-bottom: -20px !important;
        padding-bottom: 0px !important;
        font-weight: 600 !important;
    }

    .stSelectbox, .stNumberInput, .stSlider, .stRadio {
        margin-bottom: 40px !important;
    }

    .ceha-header {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 48px;
        font-weight: 900;
        color: #333333;
        margin-bottom: 0px;
        letter-spacing: -1px;
    }
    .ceha-line {
        background-color: #e65500;
        height: 6px;
        width: 120px;
        margin-bottom: 30px;
    }
    .header-container {
        display: flex;
        align-items: center;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .orange-dot {
        height: 12px;
        width: 12px;
        background-color: #e65500;
        margin-right: 15px;
        flex-shrink: 0;
    }
    .custom-subheader {
        color: #333333 !important; 
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        font-size: 1.25rem;
        margin: 0;
    }

    .promo-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 5px;
        border: 1px solid #ddd;
        border-left: 5px solid #e65500;
        margin-bottom: 35px;
        line-height: 1.6;
    }
    .stButton > button { 
        background-color: #e65500; 
        color: white !important; 
        border-radius: 2px; 
        border: none;
        font-weight: bold;
        padding: 10px;
        width: 100%;
    }
    
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-bottom: 4px solid #e65500;
    }

    .wp-bedarf-box { 
        background-color: #ffffff; 
        padding: 25px; 
        border-left: 10px solid #e65500; 
        border-radius: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        text-align: center;
    }

    .disclaimer-box {
        font-size: 12px;
        color: #777777;
        line-height: 1.4;
        margin-top: 40px;
        padding: 15px;
        border-top: 1px solid #ddd;
    }
    hr { border-top: 2px solid #e65500 !important; opacity: 0.3; }
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
modus = st.radio("Datengrundlage:", ["Realer Verbrauch (Bestand)", "Berechneter Bedarf (Heizlast)"], horizontal=True)

waermebedarf, aktuelle_kosten, eta = 0.0, 0.0, 1.0

if "Verbrauch" in modus:
    c1, c2, c3 = st.columns([3, 1.5, 1.5])
    with c1:
        energietraeger = st.selectbox("Energieträger", ["Heizöl", "Erdgas", "Flüssiggas"])
        baujahr_auswahl = st.selectbox("Kesselbaujahr (Technik)", ["Vor 1995 (Konstanttemperaturkessel)", "1995 - 2005 (Niedertemperaturkessel)", "Ab 2006 (Brennwertgerät)"])
        eta = 0.78 if "Konstant" in baujahr_auswahl else (0.86 if "Nieder" in baujahr_auswahl else 0.94)
    with c2:
        unit = "Liter/Jahr" if energietraeger != "Erdgas" else "kWh/Jahr"
        verbrauch = st.number_input(unit, min_value=0, value=2500, step=100)
    with c3:
        preis_alt = st.number_input("Preis/Einheit (€)", value=1.05 if energietraeger != "Erdgas" else 0.12, step=0.01)
        aktuelle_kosten = verbrauch * preis_alt
        if energietraeger == "Heizöl": waermebedarf = verbrauch * 9.8 * eta
        elif energietraeger == "Erdgas": waermebedarf = verbrauch * eta if verbrauch > 8000 else verbrauch * 10.3 * eta
        else: waermebedarf = verbrauch * 6.57 * eta
    st.caption(f"Angenommener Wirkungsgrad Altanlage: **{eta*100:.0f}%**")
else:
    col_last, col_pers, col_kosten = st.columns([2, 1.5, 1.5])
    with col_last: heizlast = st.number_input("Norm-Heizlast (kW)", min_value=0.0, value=12.0, step=0.5)
    with col_pers: bewohner = st.number_input("Bewohner", min_value=1, value=4, step=1)
    with col_kosten: aktuelle_kosten = st.number_input("Aktuelle Heizkosten (€)", value=2800.0, step=50.0)
    waermebedarf = (heizlast * 2100) + (bewohner * 800)

st.divider()

# --- 2. TECHNIK ---
render_header("2. Technisches Konzept")
standard_wahl = st.radio("Wärmepumpen-Standard:", ["Aktueller Stand der Technik", "VDI 4650 (Konservativer Standard)"], horizontal=True)
sys_col, temp_col = st.columns(2)
with sys_col: 
    heizsystem = st.selectbox("Anlage-Hydraulik", ["1. Fußbodenheizung (FBH)", "2. Radiatorheizung (Heizkörper)", "3. Mischsystem (EG: FBH / OG: Radiatoren)"])
with temp_col:
    d, m = (35, 50) if "1." in heizsystem else (55, 70)
    vorlauf = st.slider("Vorlauftemperatur (°C)", 30, m, d)

jaz = 4.7 if vorlauf <= 35 else 3.4 if vorlauf <= 55 else 2.8

st.divider()

# --- 3. STROMTARIF & VERGLEICH ---
render_header("3. Stromtarif & Vergleich")
strombedarf_wp = waermebedarf / jaz if jaz > 0 else 0
st.markdown(f'<div class="wp-bedarf-box"><small>IHR WERT FÜR DEN TARIFVERGLEICH</small><br><span style="font-size: 32px; font-weight: bold; color: #e65500;">{strombedarf_wp:,.0f} kWh / Jahr</span></div>', unsafe_allow_html=True)

st.write("In unserem Rechner können Sie Ihren persönlichen Tarif finden und so eine aktuelle Einschätzung der Kosten bekommen. Wir empfehlen, die untenstehenden Vergleichsrechner zu nutzen, um dauerhaft im günstigsten Tarif Strom zu beziehen. Sollten Sie nicht die Zeit oder Lust haben, jährlich manuell Ihren Stromtarif zu wechseln, empfehlen wir den Service von Cheapenergy24 – dieser übernimmt den regelmäßigen Wechsel dauerhaft und automatisch für Sie.")

col_links, col_preis = st.columns([1.5, 1])
with col_links:
    st.link_button("Check24 Vergleich", "https://www.check24.de/strom/vergleich/")
    st.link_button("Cheapenergy24", "https://www.cheapenergy24.de")
with col_preis:
    strompreis_cent = st.number_input("Normalstrom (ct/kWh)", value=28.5, step=0.1)
    strompreis_euro = strompreis_cent / 100
stromkosten_wp, ersparnis = strombedarf_wp * strompreis_euro, aktuelle_kosten - (strombedarf_wp * strompreis_euro)

st.divider()

# --- ERGEBNISSE ---
render_header("Prognose-Ergebnis")
if ersparnis > 0: st.success(f"Einsparung: Jährlich ca. {ersparnis:,.2f} € gegenüber dem Alt-System.")
else: st.warning(f"Zusatzkosten von ca. {abs(ersparnis):,.2f} € p.a. gegenüber dem Alt-System.")
m1, m2, m3 = st.columns(3)
m1.metric("Arbeitszahl (JAZ)", f"{jaz}")
m2.metric("Strombedarf WP", f"{strombedarf_wp:,.0f} kWh")
m3.metric("Energiekosten WP", f"{stromkosten_wp:,.2f} €")

st.markdown("<br>", unsafe_allow_html=True)
st.link_button("Kontakt zur Fachplanung anfragen", "https://www.ceha-energieberatung.de/kontakt")
st.caption("© CEHA ENERGIEBERATUNG UG (haftungsbeschränkt)")

st.markdown("""
    <div class="disclaimer-box">
        <strong>Rechtlicher Hinweis:</strong> Diese Online-Prognose dient ausschließlich der unverbindlichen Erstinformation und Orientierung. 
        Sie ersetzt keine individuelle Fachplanung, Heizlastberechnung nach DIN 12831 oder Vor-Ort-Energieberatung. 
        Trotz sorgfältiger Programmierung wird für die Richtigkeit, Vollständigkeit und Aktualität der berechneten Werte sowie für daraus resultierende 
        Investitionsentscheidungen keine Haftung übernommen. Maßgeblich für Förderungen und technische Auslegungen sind ausschließlich die 
        individuellen Berechnungen im Rahmen einer persönlichen Beratung.
    </div>
""", unsafe_allow_html=True)
