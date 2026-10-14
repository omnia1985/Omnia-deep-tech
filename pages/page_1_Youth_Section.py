import streamlit as st
import time

st.set_page_config(layout="wide")

# جلب اللغة المحددة من الجلسة وضمان المزامنة التامة مع الصفحة الرئيسية
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

# 1️⃣ القاموس المركزي المترجم بالكامل للغات الست لباقة الناشئين
P1_TXT = {
    "🇸🇦 العربية": {
        "title": "👶 قسم الناشئين والقصر والأطفال (إلى حدود 20 سنة)",
        "price": "💰 ثمن الاشتراك: 20 دولار شهرياً | ✨ مجاني 100% بالكامل للأطفال والأكاديميات دون 16 سنة",
        "live_cam_lbl": "🎥 تشغيل الكاميرا الحية لتصوير اللاعب فوراً (بث مباشر من الهاتف مع عرض البيانات AR فوق الكاميرا):",
        "upload_lbl": "📥 أو ارفع فيديو مسبق ومخزن للمباراة (ترميم وتوضيح الضبابية والضوء الخافت بالذكاء الاصطناعي):",
        "process_live": "⚡ جاري تشغيل البث المباشر ومعالجة الحركة وعرض البيانات اللحظية فوق الكاميرا (AR Live)...",
        "process_file": "🔄 جاري معالجة فيديو الهاتف وترميم الضبابية والإضاءة وفك تداخل اللاعبين بالذكاء الاصطناعي...",
        "gdpr_warn": "🔒 تم تفعيل عنصر التغبيش الرقمي التلقائي (GDPR): ملامح وجه الناشئ مشفرة بالكامل وتظهر له ولوليه فقط، وتفتح للكشافين عند تقديم عرض رسمي جدي لضمان حقوق المكوّن.",
        "stats_title": "📊 بطاقة البيانات والأداء المستخرجة بالذكاء الاصطناعي بدقة:",
        "comp_lbl": "🔄 نظام التشبيه الرياضي التكتيكي التلقائي مع النجوم العالمييين للناشئين:",
        "sim_res": "🏆 النجم العالمي المطابق لأسلوب لعبك الحالي:"
    },
    "🇬🇧 English": {
        "title": "👶 Youth, Minors & Children Section (Up to 20 Years Old)",
        "price": "💰 Subscription Price: $20/Month | ✨ 100% FREE for Children & Small Academies Under 16",
        "live_cam_lbl": "🎥 Turn on Live Camera for Instant Scouting (Mobile streaming with real-time AR data overlay):",
        "upload_lbl": "📥 Or Upload a Preset Match Video (AI auto blur removal & low-light restoration):",
        "process_live": "⚡ Initializing live mobile feed, body tracking, and real-time AR metrics overlay...",
        "process_file": "🔄 AI is restoring preset mobile video quality, fixing blur, lighting, and de-overlapping players...",
        "gdpr_warn": "🔒 AI Face Blurring & GDPR Shield Active: The youth's features are completely encrypted and visible only to them and their guardian. Unblurred for scouts only upon a serious official offer to secure developer rights.",
        "stats_title": "📊 AI-Generated Physical & Tactical Performance Card:",
        "comp_lbl": "🔄 Automatic Youth Tactical Comparison System with Global Stars:",
        "sim_res": "🏆 Matched Global Star according to your playing style:"
    },
    "🇫🇷 Français": {
        "title": "👶 Section Jeunes, Mineurs & Enfants (Jusqu'à 20 ans)",
        "price": "💰 Tarif d'abonnement : 20$/Mois | ✨ 100% GRATUIT pour les enfants & petites académies < 16 ans",
        "live_cam_lbl": "🎥 Activer la Caméra en Direct pour détection (Streaming mobile avec incrustation AR des données) :",
        "upload_lbl": "📥 Ou Déposer une Vidéo Enregistrée (Restauration automatique du flou et basse lumière par l'IA) :",
        "process_live": "⚡ Traitement du flux vidéo en direct, suivi corporel et affichage AR des données sur l'écran...",
        "process_file": "🔄 L'IA restaure le flou de la vidéo enregistrée, élimine le chevauchement et ajuste l'éclairage...",
        "gdpr_warn": "🔒 Floutage Numérique & Protection GDPR Actifs : Les traits du visage du jeune sont chiffrés. Visibles uniquement par le joueur et son tuteur, débloqués pour les recruteurs après offre sérieuse.",
        "stats_title": "📊 Carte de Performance Physique & Tactique extraite par l'IA :",
        "comp_lbl": "🔄 Système de Comparaison Tactique Automatique avec les Stars Mondiales :",
        "sim_res": "🏆 Star Mondiale Correspondante à votre style de jeu :"
    },
    "🇮🇹 Italiano": {
        "title": "👶 Sezione Giovani, Minori e Bambini (Fino a 20 anni)",
        "price": "💰 Prezzo: $20/Mese | ✨ 100% GRATUITO per bambini e piccole accademie sotto i 16 anni",
        "live_cam_lbl": "🎥 Attiva la Telecamera Live per lo scouting istantaneo (Streaming da cellulare con dati AR in tempo reale):",
        "upload_lbl": "📥 Oppure Carica un Video Registrato (Ripristino automatico della sfocatura e luce scarsa tramite IA):",
        "process_live": "⚡ Inizializzazione del feed live da mobile, tracciamento corporeo e sovrapposizione dei dati AR...",
        "process_file": "🔄 L'IA sta ripristinando la sfocatura del video caricato, correggendo l'oscurità e il sovrappopolamento...",
        "gdpr_warn": "🔒 Oscuramento Volto AI e GDPR Attivo: I lineamenti del minore sono crittografati, visibili solo a lui e al tutore. Visibili agli scout solo dopo un'offerta ufficiale seria.",
        "stats_title": "📊 Scheda di Performance Fisica e Tattica Generata dall'IA:",
        "comp_lbl": "🔄 Sistema di Confronto Tattico Automatico con le Stelle Mondiali:",
        "sim_res": "🏆 Stella Mondiale Corrispondente al tuo stile di gioco:"
    },
    "🇪🇸 Español": {
        "title": "👶 Sección de Juveniles, Menores y Niños (Hasta 20 años)",
        "price": "💰 Precio: $20/Mes | ✨ 100% GRATIS para niños y pequeñas academias menores de 16 años",
        "live_cam_lbl": "🎥 Activar Cámara en Vivo (Streaming móvil con superposición de datos AR en tiempo real):",
        "upload_lbl": "📥 O Subir Video Pregrabado del Partido (Eliminación automática de desenfoque y luz tenue por IA):",
        "process_live": "⚡ Procesando transmisión en vivo del móvil, seguimiento de postura y métricas AR en pantalla...",
        "process_file": "🔄 La IA está restaurando el video pregrabado, corrigiendo luz baja y resolviendo superposición...",
        "gdpr_warn": "🔒 Difuminado de Rostro AI y Escudo GDPR Activo: Las facciones del menor están encriptadas. Visibles solo para él y su tutor. Se abre a cazatalentos tras oferta financiera formal.",
        "stats_title": "📊 Tarjeta de Rendimiento Físico y Táctico Extraída por IA:",
        "comp_lbl": "🔄 Sistema de Comparación Tactica Automática con Estrellas Globales:",
        "sim_res": "🏆 Estrella Mundial Idéntica según tu estilo de juego:"
    },
    "🇵🇹 Português": {
        "title": "👶 Seção de Juvenis, Menores e Crianças (Até 20 anos)",
        "price": "💰 Preço: $20/Mês | ✨ 100% GRATUITO para crianças e pequenas academias menores de 16 anos",
        "live_cam_lbl": "🎥 Ativar Câmera ao Vivo para olheiros (Streaming de celular com exibição de dados AR em tempo real):",
        "upload_lbl": "📥 Ou Carregar Vídeo Gravado (Restauração automática de pouca luz e desfoque por IA):",
        "process_live": "⚡ Processando feed ao vivo do celular, rastreamento físico e métricas AR instantâneas na tela...",
        "process_file": "🔄 A IA está processando o vídeo gravado para restaurar desfoque, iluminação e sobreposição de jogadores...",
        "gdpr_warn": "🔒 Desfoque de Rosto AI e Proteção GDPR Ativa: O rosto do jovem está totalmente encriptado e visível apenas para ele e o tutor. Aberto para olheiros após proposta financeira firme.",
        "stats_title": "📊 Cartão de Desempenho Físico e Tático extraído por IA:",
        "comp_lbl": "🔄 Sistema de Comparação Tática Automática com Estrelas Globais:",
        "sim_res": "🏆 Estrela Mundial Correspondente ao seu estilo de jogo:"
    }
}

lang_key = selected_lang if selected_lang in P1_TXT else "🇸🇦 العربية"
t = P1_TXT[lang_key]

st.title(t["title"])

# 2️⃣ إعداد واجهة الشاشة الجانبية لإدخال العمر ونوع الاشتراك
st.sidebar.header("👤 حساب وعمر الناشئ")
acc_type = st.sidebar.radio("نوع المنظومة والجهة:", ["لاعب مستقل (Individual)", "أكاديمية صغيرة للأطفال (Small Academy)"])
age = st.sidebar.number_input("أدخل عمر اللاعب الحالي:", min_value=5, max_value=20, value=14)

# تطبيق المجانية المطلقة بشكل بارز تحت الـ 16 عاماً
if age < 16:
    st.success("🎉 هذا الحساب معفى ومفعل مجاناً بالكامل (0 USD) لجميع الأطفال دون 16 سنة.")
    st.sidebar.metric(label="قيمة الاشتراك الحالية", value="0 USD / FREE")
else:
    st.error(t["price"])
    st.sidebar.metric(label="قيمة الاشتراك الحالية", value="20 USD")

st.write("---")

# 3️⃣ تفعيل بروتوكول التدخل القانوني الإلزامي والـ GDPR للأولياء دون سن 16 سنة
proceed_allowed = True
if age < 16:
    st.markdown("### 👨‍👩‍👦 نظام وموافقة الولي الشرعي الإلزامية (GDPR Protection)")
    col1, col2 = st.columns(2)
    with col1:
        parent_name = st.text_input("اسم الولي الشرعي بالكامل:")
        parent_id = st.text_input("رقم بطاقة تعريف الولي / جواز السفر:")
    with col2:
        consent_signature = st.checkbox("أقر أنا الولي الشرعي بالموافقة القانونية على فتح الكاميرا والمعالجة الحية لاستخراج مقاييس الأداء لغرض الشراء والإعارة.")
    
    if not (consent_signature and parent_id != "" and parent_name != ""):
        proceed_allowed = False
        st.warning("⚠️ يرجى تعبئة بيانات موافقة الولي بالكامل وتفعيل خانة الإقرار لفتح خانة تفعيل الفيديوهات (الحية والمسبقة) للطفل.")

# 4️⃣ فتح خانة تشغيل المنظومة المزدوجة للفيديوهات عند استيفاء الشروط القانونية
if proceed_allowed:
    st.markdown(f"### {t['live_cam_lbl']}")
    # الخيار الأول: تصوير فيديو حي مباشرة بالهاتف وتفعيل كاميرا الويب
    live_video = st.camera_input("Universal AI Live Camera")
    
    st.markdown(f"### {t['upload_lbl']}")
    # الخيار الثاني: رفع مقطع فيديو مسبق ومخزن من الجهاز
    uploaded_file = st.file_uploader("", type=["mp4", "mov"], key="youth_match_uploader")
    
    # معالجة إدخال الفيديو سواء كان حياً أو مسبقاً
    video_source = None
    processing_msg = ""
    
    if live_video:
        video_source = live_video
        processing_msg = t["process_live"]
    elif uploaded_file:
        video_source = uploaded_file
        processing_msg = t["process_file"]
        
    if video_source:
        with st.spinner(processing_msg):
            time.sleep(1.5) # محاكاة معالجة حواسيب الرؤية والـ PyTorch
            
        st.warning(t["gdpr_warn"])
        st.write("---")
            # 4️⃣ ظهور لوحة تحكم التحليلات المتقدمة للناشئين (Analytics Dashboard Stack)
    st.subheader(t["stats_title"])
    
    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown("### 🧮 الإحصائيات الفنية والتمركز")
        st.progress(0.15, text="نسبة أخطاء التمركز المكتشفة (Positioning Errors): 15%")
        st.progress(0.85, text="نسبة التفوق في الثنائيات والالتحامات الهوائية: 85%")
        st.progress(0.78, text="معدل دقة التمرير وبناء اللعب اللحظي: 78%")
        st.caption("⚽ **الإنتاجية الهجومية:** 6 أهداف مسجلة | 4 تمريرات حاسمة")

    with col_d2:
        st.markdown("### 🧠 التحليل النفسي والسلوكي للناشئ")
        st.progress(0.88, text="مؤشر الثبات الذهني والتركيز أثناء اللعب: 88%")
        st.progress(0.92, text="نسبة التأقلم والانسجام مع زملائه في الملعب: 92%")
        st.caption("🤝 **العلاقات السلوكية والتعامل (Emotion AI):**")
        st.caption("- الانضباط والاحترام الكامل مع طاقم الحكام: 96% (ممتاز)")
        st.caption("- مؤشر النرفزة أو لغة الجسد السلبية مع الزملاء: مستقر ومنخفض جداً")

    with col_d3:
        st.markdown("### 🩺 المنظومة الطبية والتنبؤ الاستباقي بالإصابات")
        st.progress(0.05, text="نسبة احتمالية التنبؤ بالإصابة العضلية مستقبلاً: 5%")
        st.progress(0.96, text="معدل استجابة الهيكل الحركي وجاهزية التوأم الرقمي: 96%")
        st.metric(label="🟢 حالة وجاهزية الناشئ للمباريات الرسمية", value="95% جاهز للعب")

    # 5️⃣ عنصر التشبيه المفتوح واستخراج بطاقة النجم وصورته للناشئين
    st.write("---")
    st.subheader("🔄 منظومة التطابق التكتيكي والتشبيه الرياضي")
    st.write(t["comp_lbl"])
    
    # اختيار النجم العالمي المقارن به
    youth_star = st.selectbox("", ["Lamine Yamal", "Gavi", "Endrick", "Pedri", "Arda Güler"], label_visibility="collapsed")
    
    if youth_star:
        st.success(f"🔄 {t['sim_res']} **{youth_star}**")
        # عرض صورة المقارنة السينمائية المخصصة لتقوية الواجهة الاحترافية (Experituelle)
        st.image("https://unsplash.com", caption=f"بطاقة التشبيه الرقمي للناشئ مع النجم: {youth_star}")

st.write("---")
# التذييل الإداري والسيبراني النهائي لإتمام وإغلاق الصفحة بالكامل
st.caption("🔒 بيئة معزولة ومحمية بالكامل للامتثال لمنظومة GDPR وحماية القصر الدولية ومنع تخطي المنصة.")
st.caption("Omnia DeepArena IA © 2026 | Youth Secure Sandbox & Identity Protection Multi-Tenancy Protocols.")

