import streamlit as st

# إعداد الصفحة وتفعيل التصميم العريض
st.set_page_config(page_title="Omnia DeepArena IA", layout="wide", initial_sidebar_state="expanded")

# 1️⃣ حقن التصميم والتقنيات العالية: خلفية الملعب المتحركة والجماليات السينمائية (Experituelle)
st.markdown("""
<style>
    /* خلفية الملعب المتحركة بأسلوب تكنولوجي عالي */
    .stApp {
        background: linear-gradient(rgba(0, 4, 10, 0.85), rgba(0, 15, 5, 0.85)), 
                    url('https://unsplash.com');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }
    /* تصميم بطاقات الباقات والأسعار الدائرية الاحترافية */
    .pricing-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 255, 136, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .pricing-card:hover {
        border-color: #00ff88;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 255, 136, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# 2️⃣ القاموس المركزي لست لغات والأعلام لجميع شاشات وأقسام المنصة مع دمج الأسعار المحدثة وحذف الاستثمار
LANG_DATA = {
    "🇸🇦 العربية": {
        "welcome": "⚽ مرحباً بك في منصة Omnia DeepArena الرقمية الموحدة لكشافي الملاعب وسوق الانتقالات العالمية والند للند",
        "info": "← يرجى تصفح الأقسام والانتقال بين الصفحات الست الفرعية المتاحة عبر القائمة الجانبية (Sidebar).",
        "headline": "🏟️ باقات الاشتراك المتاحة والأسعار الرسمية الموحدة بالمنظومة:",
        "music_lbl": "🎵 مشغل الصوتيات والأجواء الملحمية (Experituelle):",
        "ucl_track": "🏆 تشغيل موسيقى رابطة الأبطال الأوروبية الرسمية (UEFA Champions League)",
        "p1_title": "👶 باقة الناشئين والأطفال (القسم الأول)",
        "p1_desc": "💰 السعر: 20 دولار/شهرياً | ✨ مجاناً بالكامل للأطفال دون 16 سنة بموافقة الولي الشرعي الإلزامية والامتثال لـ GDPR.",
        "p2_title": "🏃 باقة اللاعبين الكبار وسينيور (القسم الثاني)",
        "p2_desc": "💰 السعر: 30 دولار/شهرياً للوصول التشريحي الشامل، الكاميرا الحية، والتشبيه بالنجوم الـ 15 وحراس المرمى.",
        "p3_title": "🔍 باقة الكشافين ووكلاء الأندية وسوق الانتقالات",
        "p3_desc": "💰 السعر: 50 دولار/شهرياً للولوج الفوري للبورصة، التصفح الشامل، وقنوات التعاقد والشراء مع اقتطاع عمولة المنصة (5%-10%).",
        "p4_title": "🏪 أندية الدرجة 2 و3، أندية الهواة، والأكاديميات",
        "p4_desc": "💰 السعر: 500 دولار/شهرياً لتفعيل لوحة تحكم المدرب، محرك الريمونتادا (50,000 محاكاة)، والمنظومة المزدوجة للفيديو.",
        "p5_title": "🏢 الأندية المتوسطة من الدرجة الأولى",
        "p5_desc": "💰 السعر: 500 دولار/شهرياً للحصول على لوحة تحكم المدرب الكاملة، إسقاط صفقات التوأم الرقمي، وتكامل كاميرات البث والدرون.",
        "p6_title": "🏰 أندية البطولات والكؤوس الكبرى",
        "p6_desc": "💰 السعر: 1500 دولار/شهرياً للدخول السيبراني المعزول (Sandbox)، محاكي الأزمات وجدار حماية السرية العسكري الفائق."
    },
    "🇬🇧 English": {
        "welcome": "⚽ Welcome to Omnia DeepArena Unified Scouting, Global Transfer Marketplace & Peer-to-Peer Platform",
        "info": "← Please navigate through the 6 available sub-pages via the Sidebar.",
        "headline": "🏟️ Active Subscription Plans & Official Pricing within the System:",
        "music_lbl": "🎵 Audio Player & Atmospheric Experience (Experituelle):",
        "ucl_track": "🏆 Play Official UEFA Champions League Anthem",
        "p1_title": "👶 Youth & Minors Package (Section 1)",
        "p1_desc": "💰 Price: $20/Month | ✨ 100% FREE for children under 16 with mandatory legal parental consent & GDPR shield.",
        "p2_title": "🏃 Senior Players Package (Section 2)",
        "p2_desc": "💰 Price: $30/Month for complete anatomical stack, live mobile camera AR, and matching with the 15 global stars.",
        "p3_title": "🔍 Certified Scouts, Club Agents & Transfer Market",
        "p3_desc": "💰 Price: $50/Month for live index access, advanced browsing, and instant contract negotiation/purchase (5%-10% commission).",
        "p4_title": "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        "p4_desc": "💰 Price: $500/Month for full Coach Dashboard, Remontada engine (50,000 simulations), and dual live/preset video feed.",
        "p5_title": "🏢 Medium Clubs from Division 1",
        "p5_desc": "💰 Price: $500/Month for comprehensive dashboard metrics, Digital Twin contract projection, drone and stadium stream setup.",
        "p6_title": "🏰 Major Championship & Cup Clubs",
        "p6_desc": "💰 Price: $1500/Month for isolated cyber sandbox environment, AI crisis simulator, and military-grade encryption shield."
    },
    "🇫🇷 Français": {
        "welcome": "⚽ Bienvenue sur la plateforme unifiée de recrutement mondial Omnia DeepArena et Peer-to-Peer",
        "info": "← Veuillez naviguer à travers les 6 sous-pages disponibles via le menu latéral (Sidebar).",
        "headline": "🏟️ Offres d'Abonnement et Tarifs Officiels (Visibles immédiatement) :",
        "music_lbl": "🎵 Lecteur Audio & Expérience Atmosphérique (Experituelle) :",
        "ucl_track": "🏆 Jouer l'Hymne Officiel de l'UEFA Champions League",
        "p1_title": "👶 Pack Jeunes & Mineurs (Section 1)",
        "p1_desc": "💰 Tarif: 20$/Mois | ✨ Entièrement GRATUIT pour les enfants de moins de 16 ans avec accord parental obligatoire & GDPR.",
        "p2_title": "🏃 Pack Joueurs Seniors (Section 2)",
        "p2_desc": "💰 Tarif: 30$/Mois pour l'accès anatomique complet, caméra AR en direct et comparaison avec les 15 stars.",
        "p3_title": "🔍 Recruteurs, Agents & Marché des Transferts",
        "p3_desc": "💰 Tarif: 50$/Mois pour l'accès complet, filtrage et boutons de négociation/achat (commission de 5% à 10%).",
        "p4_title": "🏪 Clubs de Division 2, 3, Amateurs & Académies",
        "p4_desc": "💰 Tarif: 500$/Mois pour le Tableau de Bord Entraîneur, moteur Remontada (50K simulations) et double flux vidéo.",
        "p5_title": "🏢 Clubs Moyens de Première Division",
        "p5_desc": "💰 Tarif: 500$/Mois pour le pack complet entraîneur, projection tactique Double Numérique et intégration Drone.",
        "p6_title": "🏰 Grands Clubs de Championnats & Coupes",
        "p6_desc": "💰 Tarif: 1500$/Mois pour l'environnement cyber isolé (Sandbox), simulateur de crise et bouclier militaire."
    },
    "🇮🇹 Italiano": {
        "welcome": "⚽ Benvenuto sulla piattaforma unificata di scouting e mercato trasferimenti Omnia DeepArena Peer-to-Peer",
        "info": "← Si prega di navigare attraverso le 6 pagine secondarie disponibili tramite il menu laterale.",
        "headline": "🏟️ Piani di Abbonamento e Prezzi Ufficiali Visibili nel Sistema:",
        "music_lbl": "🎵 Riproduttore Audio & Esperienza Atmosferica (Experituelle):",
        "ucl_track": "🏆 Riproduci l'Inno Ufficiale della UEFA Champions League",
        "p1_title": "👶 Pacchetto Giovani e Minori (Sezione 1)",
        "p1_desc": "💰 Prezzo: $20/Mese | ✨ Completamente GRATUITO sotto i 16 anni con consenso legale dei genitori obbligatorio e GDPR.",
        "p2_title": "🏃 Pacchetto Giocatori Senior (Sezione 2)",
        "p2_desc": "💰 Prezzo: $30/Mese per accesso anatomico totale, telecamera live AR e abbinamento con le 15 stelle mondiali.",
        "p3_title": "🔍 Scout, Agenti di Club e Mercato Trasferimenti",
        "p3_desc": "💰 Prezzo: $50/Mese per accesso alla borsa, navigazione e canali di acquisto/contratto (commissione del 5%-10%).",
        "p4_title": "🏪 Club di Divisione 2, 3, Dilettanti e Accademie",
        "p4_desc": "💰 Prezzo: $500/Mese per il Pannello Allenatore, motore Remontada (50k simulazioni) e doppio feed video live/archiviato.",
        "p5_title": "🏢 Club Medi di Prima Divisione",
        "p5_desc": "💰 Prezzo: $500/Mese per metriche avanzate, proiezione contrattuale Gemello Digitale e integrazione streaming e droni.",
        "p6_title": "🏰 Grandi Club di Campionati e Coppe",
        "p6_desc": "💰 Prezzo: $1500/Mese per ambiente sandbox cyber isolato, simulatore di crisi AI e scudo di crittografia militare."
    },
    "🇪🇸 Español": {
        "welcome": "⚽ Bienvenido a la plataforma unificada de ojeadores, mercado global y peer-to-peer Omnia DeepArena",
        "info": "← Por favor, navegue a través de las 6 páginas secundarias disponibles a través del menú lateral.",
        "headline": "🏟️ Planes de Suscripción y Tarifas Oficiales Visibles en el Sistema:",
        "music_lbl": "🎵 Reproductor de Audio y Experiencia Atmosférica (Experituelle):",
        "ucl_track": "🏆 Reproducir el Himno Oficial de la UEFA Champions League",
        "p1_title": "👶 Paquete Juvenil y Menores (Sección 1)",
        "p1_desc": "💰 Precio: $20/Mes | ✨ 100% GRATIS para menores de 16 años con consentimiento paterno obligatorio y escudo GDPR.",
        "p2_title": "🏃 Paquete Jugadores Seniors (Sección 2)",
        "p2_desc": "💰 Precio: $30/Mes para acceso anatómico completo, cámara móvil en vivo AR y emparejamiento con 15 estrellas.",
        "p3_title": "🔍 Cazatalentos, Agentes y Mercado de Fichajes",
        "p3_desc": "💰 Precio: $50/Mes para acceso a bolsa unificada y botones de compra/negociación directa (comisión del 5%-10%).",
        "p4_title": "🏪 Clubes de División 2, 3, Amateurs y Academias",
        "p4_desc": "💰 Precio: $500/Mes para Panel de Entrenador, motor de Remontada (50,000 simulaciones) y opción de video doble.",
        "p5_title": "🏢 Clubes Medianos de Primera División",
        "p5_desc": "💰 Precio: $500/Mes para análisis avanzado, proyección de Gemelo Digital e integración de drones y cámaras fijas.",
        "p6_title": "🏰 Grandes Clubes de Campeonatos y Copas",
        "p6_desc": "💰 Precio: $1500/Mes para entorno aislado cibernético (Sandbox), simulador de crisis de vestuario y blindaje militar."
    },
    
    "🇵🇹 Português": {
        "welcome": "⚽ Bem-vindo à plataforma unificada de olheiros, mercado global e peer-to-peer Omnia DeepArena",
        "info": "← Por favor, navegue pelas 6 páginas secundárias disponíveis através do menu lateral.",
        "headline": "🏟️ Planos de Assinatura e Preços Oficiais Visíveis no Sistema:",
        "music_lbl": "🎵 Reprodutor de Áudio & Experiência Atmosférica (Experituelle):",
        "ucl_track": "🏆 Reproduzir o Hino Oficial da UEFA Champions League",
        "p1_title": "👶 Pacote Juvenil e Menores (Seção 1)",
        "p1_desc": "💰 Preço: $20/Mês | ✨ 100% GRATUITO para menores de 16 anos com consentimento legal dos pais e proteção GDPR.",
        "p2_title": "🏃 Pacote Jogadores Seniores (Seção 2)",
        "p2_desc": "💰 Preço: $30/Mês para acesso anatômico total, câmera live AR no celular e comparação com as 15 estrelas mundiais.",
        "p3_title": "🔍 Olheiros, Agentes e Bolsa de Transferências",
        "p3_desc": "💰 Preço: $50/Mês para acesso à bolsa de valores e botões de compra/negociação de contratos (comissão de 5%-10%).",
        "p4_title": "🏪 Clubes de Divisão 2, 3, Amadores e Academias",
        "p4_desc": "💰 Preço: $500/Mês para Painel do Treinador, motor de Remontada (50k simulações) e canais duplos de vídeo.",
        "p5_title": "🏢 Clubes Médios da Primeira Divisão",
        "p5_desc": "💰 Preço: $500/Mês para métricas de desempenho completas, projeção de contrato Gêmeo Digital e fluxo de drones.",
        "p6_title": "🏰 Grandes Clubes de Campeonatos e Copas",
        "p6_desc": "💰 Preço: $1500/Mese para ambiente sandbox cibernético isolado, simulador de crises de elenco e criptografia militar."
    }
}

# 3️⃣ شريط اختيار اللغة والأعلام العلوي العام والموحد لجميع شاشات التطبيق
st.markdown("### 🌐 Select Language / اختر اللغة")
selected_lang = st.selectbox("", list(LANG_DATA.keys()), label_visibility="collapsed")

# حفظ الاختيار في الجلسة لضمان التزامن الموحد والكامل مع الصفحات الفرعية الست الأخرى
st.session_state["lang"] = selected_lang
st.session_state["language"] = selected_lang.split(" ")[1] if " " in selected_lang else "العربية"

tx = LANG_DATA[selected_lang]

# 4️⃣ قسم تشغيل الموسيقى الحماسية لرابطة الأبطال الأوروبية والأجواء الملحمية (Experituelle)
st.sidebar.markdown(f"### {tx['music_lbl']}")
st.sidebar.caption(tx["ucl_track"])
st.sidebar.audio("https://soundhelix.com")

# 5️⃣ تصميم واجهة الترحيب ومصادر التوجيه والتحكم
st.title(tx["welcome"])
st.info(tx["info"])
st.write("---")

# 6️⃣ مكان ظهور الباقات والأسعار الرسمية الموحدة مباشرة تحت اختيار اللغة
st.markdown(f"### {tx['headline']}")

st.markdown(f"""
<div class="pricing-card">
    <h4 style="color:#00ff88; margin-top:0;">{tx['p1_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p1_desc']}</p>
</div>
<div class="pricing-card">
    <h4 style="color:#00ccff; margin-top:0;">{tx['p2_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p2_desc']}</p>
</div>
<div class="pricing-card">
    <h4 style="color:#ffcc00; margin-top:0;">{tx['p3_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p3_desc']}</p>
</div>
<div class="pricing-card">
    <h4 style="color:#ff3366; margin-top:0;">{tx['p4_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p4_desc']}</p>
</div>
<div class="pricing-card">
    <h4 style="color:#b366ff; margin-top:0;">{tx['p5_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p5_desc']}</p>
</div>
<div class="pricing-card">
    <h4 style="color:#ff6600; margin-top:0;">{tx['p6_title']}</h4>
    <p style="margin:0; font-size:14px; color:#e0e0e0;">{tx['p6_desc']}</p>
</div>
""", unsafe_allow_html=True)

st.write("---")
st.caption("Omnia DeepArena IA © 2026 | Secure Cyber-Tactical Platform Secured under Global Multi-Tenancy Sandbox Protocols.")
