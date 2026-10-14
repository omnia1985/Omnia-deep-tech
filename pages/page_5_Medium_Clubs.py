import streamlit as st
import time

st.set_page_config(layout="wide")

# ✨ السطر السحري المؤمن: تأمين ذاكرة الجلسة واللغة وقائمة اللاعبين فوراً لمنع اختفاء المحتوى
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

# جلب اللغة المحددة وضمان Mزامنة التامة مع الصفحة الرئيسية
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

# 1️⃣ القاموس المركزي المترجم بالكامل للغات لباقة الأندية المتوسطة من الدرجة الأولى
P5_TXT = {
    "🇸🇦 العربية": {
        "title": "🏢 الأندية المتوسطة من الدرجة الأولى",
        "sub": "📌 باقة الأندية المتوسطة - مخصصة لإدارة وتغذية وعرض مواهب النادي وعمل إسقاط تكتيكي ومحاكاة الصفقات.",
        "price_label": "💰 اشتراك الباقة الشهري:",
        "features_title": "📋 الميزات النشطة في الباقة:",
        "f1": "✅ كل ميزات باقة ديمقراطية التكنولوجيا (الرمونتادا والثنائيات والطبي والـ GDPR)",
        "f2": "✅ دمج كاميرات البث المحترفة وتصوير الدرون (Drone Integration)",
        "f3": "✅ تصفح كامل لسوق المواهب العالمي وعمل إسقاط تكتيكي للمشتري",
        "live_cam_lbl": "🎥 المسار الأول: ربط بث الكاميرات المباشر وتصوير الملعب أو الدرون (Live AR Overlay):",
        "upload_lbl": "📥 المسار الثاني: رفع فيديو مسبق ومخزن للمباريات (لإخضاعه للإسقاط التكتيكي ومحاكاة الصفقات):",
        "process_live": "⚡ جاري معالجة البث الحي الاحترافي وعرض التحليلات التكتيكية الحية فوق الشاشة...",
        "process_file": "🔄 جاري رفع الفيديو المسبق وتجهيز ملفات محاكاة التوأم الرقمي والإسقاط...",
        "coach_dash": "📊 لوحة تحكم المدرب المتطورة وطور التحليل الفني (Coach Analytics Dashboard)",
        "pre_match": "🟢 طور قبل المباراة (محاكاة إسقاط الصفقات والتوأم الرقمي عبر 10,000 مباراة)",
        "in_match": "⚡ طور أثناء المباراة (تحليل الثنائيات، الاستحواذ اللحظي والخطط المضادة الحية)",
        "post_match": "🔴 طور بعد المباراة (التقرير التشريحي، التنبؤ بالإصابات وتطور الانسجام)",
        "market_title": "🔍 محرك الاستكشاف المفتوح وسوق الانتقالات العالمي المشترك (الجدول الموحد)",
        "btn_drop": "🔬 عمل إسقاط تكتيكي في خطة نادينا (10,000 مباراة)",
        "btn_buy": "💼 بدء تفاوض رسمي وشراء العقد",
        "success_drop": "📊 نتيجة محاكاة الإسقاط التكتيكي الموحد: هذا اللاعب يمتلك نسبة تأقلم تكتيكي وبدني 89% ونسبة تفوق في الثنائيات تصل لـ 72% بناءً على قوالب المباريات التاريخية.",
        "info_buy": "⚖️ امتثال المعاملات وعقود الانتقال وحماية الـ GDPR: تم فتح قناة المعاملات المشفرة، وسيتم حساب واقتطاع حقوق التكوين والتضامن وعمولة المنصة آلياً فور توقيع الأطراف لضمان حقوق المكوّن.",
        "logo_lbl": "🛡️ نظام الهوية الرقمية: ارفع شعار النادي المخصص لحقنه فوراً في التصميم عالي التقنية:"
    },
    "English": {
        "title": "🏢 Medium Clubs from Division 1",
        "sub": "📌 Medium Clubs Package - Tailored to manage, feed, display talents, and run advanced buyer tactical projections.",
        "price_label": "💰 Monthly Subscription Price:",
        "features_title": "📋 Active Features in Package:",
        "f1": "✅ All tech democratization features (Remontada, Duels, Medical & GDPR)",
        "f2": "✅ Integration with professional broadcast cameras and drone streams",
        "f3": "✅ Full access to browse global talents and perform buyer tactical projections",
        "live_cam_lbl": "🎥 Track 1: Connect Professional Live Broadcast Cameras or Drone Feed (Live AR Overlay):",
        "upload_lbl": "📥 Track 2: Upload a Preset/Pre-recorded Match Video (For tactical projections & contract simulations):",
        "process_live": "⚡ Processing professional live stream and broadcasting live tactical metrics on video...",
        "process_file": "🔄 Uploading pre-recorded file and initializing Digital Twin contract projection files...",
        "coach_dash": "📊 Advanced Coach Analytics Dashboard",
        "pre_match": "🟢 Pre-Match Phase (Tactical Projection Simulation over 10,000 matches)",
        "in_match": "⚡ Live / In-Match Phase (Duels Analysis, Live Possession & Tactical Solutions)",
        "post_match": "🔴 Post-Match Phase (Anatomical Report, Injury Prediction & Adaptation Metrics)",
        "market_title": "🔍 Open Scouting Engine & Global Unified Shared Transfer Market",
        "btn_drop": "🔬 Run Tactical Projection in Our System (10,000 matches)",
        "btn_buy": "💼 Start Official Negotiation & Buy Contract",
        "success_drop": "📊 Tactical Projection Result: This player has an 89% tactical and physical adaptation rate, and a 72% success rate in duels based on historical matches.",
        "info_buy": "⚖️ Transaction Compliance & GDPR Protection: Encrypted channel opened. Solidarity mechanisms and platform commission calculated automatically.",
        "logo_lbl": "🛡️ Digital Branding: Upload your official Club Logo to inject it into the high-tech interface instantly:"
    },
    "Français": {
        "title": "🏢 Clubs Moyens de Première Division",
        "sub": "📌 Pack Clubs Moyens - Conçu pour gérer, afficher les talents et exécuter des projections tactiques d'acheteurs.",
        "price_label": "💰 Prix de l'abonnement mensuel :",
        "features_title": "📋 Fonctionnalités actives dans le pack :",
        "f1": "✅ Toutes les fonctions de démocratisation (Remontada, Duels, Médical & GDPR)",
        "f2": "✅ Intégration de caméras de diffusion professionnelles et de flux de drones",
        "f3": "✅ Accès complet pour parcourir les talents mondiaux et faire des projections tactiques",
        "live_cam_lbl": "🎥 Piste 1 : Connecter les caméras de diffusion professionnelles ou flux de drone (Incrustation AR en direct) :",
        "upload_lbl": "📥 Piste 2 : Déposer une Vidéo Enregistrée (Pour projections tactiques et simulations de contrat) :",
        "process_live": "⚡ Traitement du flux pro en direct et affichage des métriques tactiques sur l'écran...",
        "process_file": "🔄 Chargement du fichier enregistré et initialisation des fichiers du Double Numérique...",
        "coach_dash": "📊 Tableau de Bord d'Analyses Entraîneur Avancé",
        "pre_match": "🟢 Phase d'Avant-Match (Simulation de Projection Tactique sur 10 000 matchs)",
        "in_match": "⚡ Phase En Direct (Analyse des Duels, Possession et Solutions Tactiques)",
        "post_match": "🔴 Phase d'Après-Match (Rapport Anatomique, Prédiction des Blessures et Métriques d'Adaptation)",
        "market_title": "🔍 Moteur de recherche ouvert & Marché mondial unifié des transferts",
        "btn_drop": "🔬 Lancer une projection tactique (10 000 matchs)",
        "btn_buy": "💼 Négociation officielle & Acheter le contrat",
        "success_drop": "📊 Résultat de la projection: Adaptation tactique et physique de 89% et 72% de réussite dans les duels.",
        "info_buy": "⚖️ Conformité & Protection GDPR: Canal chiffré ouvert. Calcul automatique des mécanismes de solidarité.",
        "logo_lbl": "🛡️ Identité Numérique : Déposez votre logo officiel pour l'intégrer instantanément sur l'interface :"
    },
    "Italiano": {
        "title": "🏢 Club Medi di Prima Divisione",
        "sub": "📌 Pacchetto Club Medi - Dedicato alla gestione, alimentazione e visualizzazione dei talenti del club con proiezioni tattiche.",
        "price_label": "💰 Abbonamento Mensile Ufficiale:",
        "features_title": "📋 Funzionalità Attive nel Pacchetto:",
        "f1": "✅ Tutte le funzioni di democratizzazione (Remontada, Duelli, Area Medica & GDPR)",
        "f2": "✅ Integrazione di telecamere broadcast professionali e riprese da droni",
        "f3": "✅ Accesso completo per sfogliare i talenti globali ed eseguire proiezioni tattiche",
        "live_cam_lbl": "🎥 Percorso 1: Collega Telecamere Broadcast Professionali o Feed Drone (Live AR Overlay):",
        "upload_lbl": "📥 Percorso 2: Carica un Video di Partita Registrato (Per proiezioni tattiche e simulazioni contrattuali):",
        "process_live": "⚡ Elaborazione dello streaming live professionale e proiezione delle metriche tattiche...",
        "process_file": "🔄 Caricamento del file archiviato e inizializzazione dei file di proiezione del Gemello Digitale...",
        "coach_dash": "📊 Pannello di Controllo Analisi Allenatore Avanzato",
        "pre_match": "🟢 Fase Prima della Partita (Simulazione della Proiezione Tattica su 10.000 partite)",
        "in_match": "⚡ Fase Durante la Partita (Analisi dei Duelli, Possesso Live e Soluzioni Tattiche)",
        "post_match": "🔴 Fase Post-Partita (Report Anatomico, Predizione Infortuni e Metriche di Adattamento)",
        "market_title": "🔍 Mercato Globale Unificato & Tabella Condivisa dei Trasferimenti",
        "btn_drop": "🔬 Esegui Proiezione Tattica nel Nostro Sistema (10.000 partite)",
        "btn_buy": "💼 Avvia Trattativa Ufficiale e Acquista Contratto",
        "success_drop": "📊 Risultato della Proiezione Tattica: Questo giocatore ha un tasso di adattamento dell'89% e il 72% di successo nei duelli.",
        "info_buy": "⚖️ Conformità delle transazioni e protezione GDPR: Canale crittografato aperto. Calcolo automatico delle commissioni.",
        "logo_lbl": "🛡️ Identità Digitale: Carica il logo ufficiale del club per inserirlo istantaneamente nell'interfaccia:"
    }
    "🇪🇸 Español": {
        "title": "🏢 Clubes Medianos de Primera División",
        "sub": "📌 Paquete de Clubes Medianos - Diseñado para gestionar, alimentar y exponer talentos junto con proyecciones tácticas de compradores.",
        "price_label": "💰 Suscripción Mensual Oficial:",
        "features_title": "📋 Funciones Activas en el Paquete:",
        "f1": "✅ Todas las funciones de democratización (Remontada, Duelos, Médica y GDPR)",
        "f2": "✅ Integración de cámaras de transmisión profesionales y flujos de drones",
        "f3": "✅ Acceso completo para explorar talentos globales y realizar proyecciones tácticas",
        "live_cam_lbl": "🎥 Vía 1: Conectar Cámaras de Transmisión Profesionales o Transmisión de Drone (Live AR Overlay):",
        "upload_lbl": "📥 Vía 2: Subir Video Pregrabado del Partido (Para proyecciones tácticas y simulaciones de contratos):",
        "process_live": "⚡ Procesando transmisión pro en vivo y proyectando métricas tácticas en tiempo real sobre el video...",
        "process_file": "🔄 Subiendo el archivo guardado e inicializando los datos de proyección de Gemelo Digital...",
        "coach_dash": "📊 Panel de Control de Analíticas de Entrenador Avanzado",
        "pre_match": "🟢 Fase Pre-Partido (Simulación de Proyección Táctica sobre 10,000 partidos)",
        "in_match": "⚡ Fase En Partido (Análisis de Duelos, Posesión en Vivo y Soluciones Tácticas)",
        "post_match": "🔴 Fase Post-Partido (Informe Anatómico, Predición de Lesiones y Métricas de Adaptación)",
        "market_title": "🔍 Mercado Global Unificado & Tabla Compartida de Fichajes",
        "btn_drop": "🔬 Correr Proyección Táctica en Nuestro Sistema (10,000 partidos)",
        "btn_buy": "💼 Iniciar Negociación Oficial y Comprar Contrato",
        "success_drop": "📊 Resultado de Proyección Táctica: Este jugador tiene un 89% de tasa de adaptación táctica y un 72% de éxito en duelos.",
        "info_buy": "⚖️ GDPR y Cumplimiento de Transacciones: Canal encriptado abierto. Mecanismos de solidaridad calculados automáticamente.",
        "logo_lbl": "🛡️ Identidad Digital: Suba el escudo oficial del club para inyectarlo instantáneamente en la interfaz de alta tecnología:"
    },
    "🇵🇹 Português": {
        "title": "🏢 Clubes Médios da Primeira Divisão",
        "sub": "📌 Pacote Clubes Médios - Destinado a gerar, alimentar e exibir talentos junto com projeções táticas de compradores.",
        "price_label": "💰 Assinatura Mensal Oficial:",
        "features_title": "📋 Recursos Ativos no Pacote:",
        "f1": "✅ Todos os recursos de democratização (Remontada, Duelos, Médico e GDPR)",
        "f2": "✅ Integração de câmeras de transmissão profissionais e fluxos de drones",
        "f3": "✅ Acesso total para navegar por talentos globais e realizar projeções táticas",
        "live_cam_lbl": "🎥 Canal 1: Conectar Câmeras de Transmissão Profissionais ou Feed de Drone (Live AR Overlay):",
        "upload_lbl": "📥 Canal 2: Carregar Vídeo Gravado do Jogo (Para projeções táticas e simulações de contratos):",
        "process_live": "⚡ Processando transmissão profissional ao vivo e exibindo métricas táticas em tempo real no vídeo...",
        "process_file": "🔄 Carregando arquivo gravado e inicializando os arquivos de projeção do Gêmeo Digital...",
        "coach_dash": "📊 Painel de Controle de Análises do Treinador Avançado",
        "pre_match": "🟢 Fase Pré-Jogo (Simulação de Projeção Tática sobre 10.000 jogos)",
        "in_match": "⚡ Fase No Jogo (Análise de Duelos, Posse ao Vivo e Soluções Táticas)",
        "post_match": "🔴 Fase Pós-Jogo (Relatório Anatômico, Predição de Lesões e Métricas de Adaptação)",
        "market_title": "🔍 Mercado Global Unificado & Tabela Compartilhada de Transferências",
        "btn_drop": "🔬 Executar Projeção Tática no Nosso Sistema (10.000 jogos)",
        "btn_buy": "💼 Iniciar Negociação Oficial & Comprar Contrato",
        "success_drop": "📊 Resultado da Projeção Tática: Este atleta possui 89% de taxa de adaptação tática e física e 72% de sucesso em duelos.",
        "info_buy": "⚖️ Conformidade e Proteção GDPR: Canal encriptado aberto. Direitos de formação e comissões calculados automaticamente.",
        "logo_lbl": "🛡️ Identidade Digital: Carregue o escudo oficial do clube para inseri-lo instantaneamente na interface:"
    }
}

lang_key = selected_lang if selected_lang in P5_TXT else "🇸🇦 العربية"
t = P5_TXT[lang_key]

# 2️⃣ تفعيل ميزة الهوية الرقمية وشعارات الأندية المخصصة في الشريط الجانبي
st.sidebar.markdown(f"### {t['logo_lbl']}")
club_logo = st.sidebar.file_uploader("", type=["png", "jpg", "jpeg"], key="club_logo_uploader")

if club_logo:
    st.sidebar.image(club_logo, caption="Official Club Logo Registered", use_container_width=True)

st.sidebar.metric(label=t['price_label'], value="500 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])

st.title(t['title'])
st.write(t['sub'])
st.write("---")

# 3️⃣ المنظومة المزدوجة للفيديو (الحي والمسبق) الموحدة في الصفحة الخامسة
st.markdown(f"### {t['live_cam_lbl']}")
live_video = st.camera_input("Universal AI Broadcast & Drone Live Cam")

st.markdown(f"### {t['upload_lbl']}")
uploaded_file = st.file_uploader("", type=["mp4", "mov"], key="club_medium_match_uploader")

video_source = None
processing_msg = ""

if live_video:
    video_source = live_video
    processing_msg = t["process_live"]
elif uploaded_file:
    video_source = uploaded_file
    processing_msg = t["process_file"]

# 4️⃣ ظهور لوحة تحكم المدرب والتحليلات المتكاملة وعنصر الإسقاط التكتيكي
if video_source:
    with st.spinner(processing_msg):
        time.sleep(1.5)
        
    st.header(t["coach_dash"])
    
    # طور قبل المباراة: الإسقاط التكتيكي التلقائي
    with st.expander(t["pre_match"], expanded=True):
        st.write(t["sub"])
        st.header(t['market_title'])
        st.write(t['market_sub'])
        
        c_btn1, c_btn2 = st.columns(2)
        with c_btn1:
            if st.button(t['btn_drop']): 
                st.success(t['success_drop'])
        with c_btn2:
            if st.button(t['btn_buy']): 
                st.info(t['info_buy'])
                
    # طور أثناء المباراة: البيانات المباشرة والتحليل فوق الكاميرا البثية والدرون
    with st.expander(t["in_match"], expanded=True):
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            st.metric(label="📊 نسبة الاستحواذ اللحظية عبر الدرون", value="61%")
            st.metric(label="🎯 معدل تسجيل الأهداف المتوقع الفوري (xG Live)", value="2.10")
        with col_in2:
            st.progress(0.72, text="⚔️ نسبة التفوق الإجمالية في الالتحامات والثنائيات: 72%")
            st.progress(0.09, text="🚨 نسبة الأخطاء العامة وتمركز الخطوط الخلفية: 9%")

    # طور بعد المباراة: التنبؤ بالإصابات والتقرير التشريحي المتقدم وحالة الجاهزية
    with st.expander(t["post_match"], expanded=False):
        col_post1, col_post2 = st.columns(2)
        with col_post1:
            st.progress(0.05, text="🩺 مؤشر التنبؤ المسبق بالإصابة العضلية العميقة: 5%")
            st.progress(0.96, text="🟢 حالة وجاهزية التشكيلة البدنية التكتيكية ككل: 96%")
        with col_post2:
            st.progress(0.89, text="🤝 نسبة انسجام وتأقلم اللاعبين الجدد مع الزملاء أثناء اللعب: 89%")
            st.progress(0.91, text="🧠 معدل التركيز السلوكي والثبات تحت الضغط العالي (Emotion AI): 91%")

# 5️⃣ إدراج الجدول الذكي الموحد لبورصة الانتقالات والشراء (المشترك مع حظر دون 16 سنة)
st.write("---")
st.header(t["market_title"])

th_id = "رمز اللاعب (ID)"
th_status = "حالة العقد والطلب"
th_star = "أقرب تشبيه عالمي"
th_value = "القيمة السوقية"
th_blur = "حماية الـ GDPR"

market_data = [
    {th_id: "YOUTH_TALENT_#992", th_status: "متاح للإعارة المؤقتة (For Loan)", th_star: "Lamine Yamal", th_value: "1,500,000 USD", th_blur: "🔒 Blurred (مغشّى)"},
    {th_id: "SENIOR_PRO_#402", th_status: "معروض للبيع الفوري (For Sale)", th_star: "Kylian Mbappé", th_value: "45,000,000 USD", th_blur: "🔒 Blurred (مغشّى)"},
    {th_id: "YOUTH_PRO_#551", th_status: "معروض للبيع الفوري (For Sale)", th_star: "Erling Haaland", th_value: "5,000,000 USD", th_blur: "🔒 Blurred (مغشّى)"}
]

st.dataframe(market_data, use_container_width=True)
st.caption("⚖️ نظام بورصة الصفقات متزامن ومحمي بالكامل. حقوق التكوين والعمولة مستوفاة ومحاطة بالخصوصية السيبرانية التامة لمنع التداخل.")
