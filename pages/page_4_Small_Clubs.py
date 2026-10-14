import streamlit as st
import time

st.set_page_config(layout="wide")

# ✨ السطر السحري المؤمن: تأمين ذاكرة الجلسة واللغة وقائمة اللاعبين فوراً لمنع اختفاء المحتوى
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

# جلب اللغة المحددة وضمان المزامنة التامة مع الصفحة الرئيسية
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

# 1️⃣ القاموس المركزي المترجم بالكامل للغات الست لباقة أندية الهواة والأكاديميات الخاصة
P4_TXT = {
    "🇸🇦 العربية": {
        "title": "🏪 أندية الدرجة 2 و3، أندية الهواة، والأكاديميات الخاصة",
        "sub": "📌 باقة الأندية الصغيرة والأكاديميات - لإدارة وتغذية وعرض مواهب النادي وحمايتها بمبدأ الند للند السيادي.",
        "price_label": "💰 اشتراك الباقة الشهري:",
        "features_title": "📋 الميزات النشطة:",
        "f1": "✅ محرك الريمونتادا والخطط التبديلية الحية (50,000 محاكاة)",
        "f2": "✅ لوحة تحكم المدرب والتوأم الرقمي (قبل، أثناء، وبعد المباراة)",
        "f3": "✅ المنظومة المزدوجة للفيديو وجدار الحماية GDPR المعزول تماماً",
        "live_cam_lbl": "🎥 المسار الأول: تشغيل الكاميرا الحية للمباراة (AI Live Camera & AR Overlay) وعرض البيانات فوراً:",
        "upload_lbl": "📥 المسار الثاني: رفع فيديو مسبق ومسجل سابقاً (لإخضاعه للتحليل العميق ومحاكاة الريمونتادا):",
        "process_live": "⚡ جاري ربط الكاميرا وتتبع الهيكل الحركي وعرض مؤشرات الاستحواذ والـ xG حياً...",
        "process_file": "🔄 جاري معالجة الفيديو القديم المسجل، وتفكيك التمركز التكتيكي واستخراج الإحصائيات...",
        "coach_dash": "📊 لوحة تحكم المدرب الفائقة الذكية (Advanced Coach Dashboard)",
        "pre_match": "🟢 طور قبل المباراة (Pre-Match & Digital Twin Simulation)",
        "in_match": "⚡ طور أثناء المباراة (Live / In-Match Tactics & Remontada Engine)",
        "post_match": "🔴 طور بعد المباراة (Post-Match Analytics & Injury Update)",
        "market_title": "🔍 الجدول الموحد لبورصة الانتقالات والصفقات (المشترك مع الكشافين والأندية الكبرى)",
        "logo_lbl": "🛡️ نظام الهوية الرقمية: ارفع شعار النادي الرسمي لتخصيص الواجهة وبث السيادة المعزولة:"
    },
    "English": {
        "title": "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        "sub": "📌 Small Clubs & Academies Package - Tailored to manage, feed, and display your club's own talents securely peer-to-peer.",
        "price_label": "💰 Monthly Subscription Price:",
        "features_title": "📋 Active Features:",
        "f1": "✅ Live Remontada Engine & Substitution Tactics (50,000 simulations)",
        "f2": "✅ Advanced Coach Dashboard & Digital Twin (Pre, In, and Post-Match)",
        "f3": "✅ Dual Video System & Isolated GDPR Cybersecurity Shield",
        "live_cam_lbl": "🎥 Track 1: Launch Live Match Camera (AI Live Camera & AR Overlay) for real-time metrics:",
        "upload_lbl": "📥 Track 2: Upload a Preset/Pre-recorded Video (For deep post-game analysis & Remontada simulation):",
        "process_live": "⚡ Connecting camera feed, tracking body pose, and overlaying live possession & xG...",
        "process_file": "🔄 Processing pre-recorded file, extracting positioning metrics, and running analytics...",
        "coach_dash": "📊 Advanced AI Coach Dashboard",
        "pre_match": "🟢 Pre-Match Phase & Digital Twin Simulation",
        "in_match": "⚡ Live / In-Match Tactics & Remontada Crisis Management",
        "post_match": "🔴 Post-Match Analytics & Muscle Injury Update",
        "market_title": "🔍 Unified Transfer Marketplace & Deals Table (Shared with Scouts & Major Clubs)",
        "logo_lbl": "🛡️ Digital Branding: Upload official Club Logo to customize your isolated sovereign workspace:"
    },
    "Français": {
        "title": "🏪 Clubs de Division 2, 3, Amateurs & Académies Privées",
        "sub": "📌 Pack Petits Clubs & Académies - Conçu pour gérer et afficher les talents de votre club de manière sécurisée d'égal à égal.",
        "price_label": "💰 Prix de l'abonnement mensuel :",
        "features_title": "📋 Fonctionnalités actives :",
        "f1": "✅ Moteur de Remontada et tactiques de remplacement (50 000 simulations)",
        "f2": "✅ Tableau de Bord Entraîneur & Double Numérique (Avant, Pendant, Après Match)",
        "f3": "✅ Système Vidéo Double & Bouclier de Cybersécurité GDPR Isolé",
        "live_cam_lbl": "🎥 Piste 1 : Activer la Caméra en Direct (AI Live & AR Overlay) pour affichage instantané :",
        "upload_lbl": "📥 Piste 2 : Déposer une Vidéo Enregistrée (Pour analyse approfondie et simulation de Remontada) :",
        "process_live": "⚡ Connexion au flux caméra, suivi de posture et incrustation AR du xG en temps réel...",
        "process_file": "🔄 Traitement du fichier enregistré, extraction des blocs tactiques et des statistiques...",
        "coach_dash": "📊 Tableau de Bord Entraîneur IA Avancé",
        "pre_match": "🟢 Phase d'Avant-Match & Simulation du Double Numérique",
        "in_match": "⚡ Tactiques En Direct & Gestion de Crise du Moteur Remontada",
        "post_match": "🔴 Analyses d'Après-Match & Mise à jour des blessures musculaires",
        "market_title": "🔍 Tableau du Marché Unifié des Transferts (Partagé avec Recruteurs & Grands Clubs)",
        "logo_lbl": "🛡️ Identité Numérique : Déposez le logo officiel du club pour personnaliser votre espace souverain :"
    },
    "Italiano": {
        "title": "🏪 Club di Divisione 2, 3, Dilettanti e Accademie Private",
        "sub": "📌 Pacchetto Piccoli Club e Accademie - Per gestire, alimentare e mostrare i talenti del club in modo sicuro peer-to-peer.",
        "price_label": "💰 Abbonamento Mensile Ufficiale:",
        "features_title": "📋 Funzionalità Attive:",
        "f1": "✅ Motore Remontada e simulazioni di sostituzioni live (50.000 simulazioni)",
        "f2": "✅ Pannello Allenatore Avanzato e Gemello Digitale (Prima, Durante e Dopo Partita)",
        "f3": "✅ Doppia modalità video e scudo di protezione cyber GDPR isolato",
        "live_cam_lbl": "🎥 Percorso 1: Attiva Telecamera Live della Partita (AI Live & AR Overlay) per dati immediati:",
        "upload_lbl": "📥 Percorso 2: Carica un Video Registrato (Per analisi post-partita e simulazione Remontada):",
        "process_live": "⚡ Connessione alla telecamera, tracciamento della postura e sovrizzazione live xG...",
        "process_file": "🔄 Elaborazione del file archiviato, analisi del posizionamento ed estrazione statistiche...",
        "coach_dash": "📊 Pannello di Controllo Allenatore AI Integrato",
        "pre_match": "🟢 Fase Prima della Partita & Simulazione Gemello Digitale",
        "in_match": "⚡ Tattiche Live / Durante la Partita & Gestione Crisi Remontada",
        "post_match": "🔴 Analisi Post-Partita & Aggiornamento Infortuni Muscolari",
        "market_title": "🔍 Tabella Mercato Trasferimenti Unificata (Condivisa con Scout e Grandi Club)",
        "logo_lbl": "🛡️ Identità Digitale: Carica il logo ufficiale del club per personalizzare l'ambiente protetto:"
    },
    "🇪🇸 Español": {
        "title": "🏪 Clubes de División 2, 3, Amateurs y Academias Privadas",
        "sub": "📌 Paquete de Clubes Pequeños y Academias - Diseñado para gestionar y exponer los talentos propios bajo un entorno soberano.",
        "price_label": "💰 Suscripción Mensual Oficial:",
        "features_title": "📋 Funciones Activas:",
        "f1": "✅ Motor de Remontada táctica en vivo (50,000 simulaciones)",
        "f2": "✅ Panel de Entrenador Superior y Gemelo Digital (Antes, Durante y Después del partido)",
        "f3": "✅ Sistema de Video Dual y Blindaje de Ciberseguridad GDPR Aislado",
        "live_cam_lbl": "🎥 Vía 1: Iniciar Cámara en Vivo del Partido (AI Live & AR Overlay) para métricas en pantalla:",
        "upload_lbl": "📥 Vía 2: Subir Video Pregrabado del Partido (Para análisis profundo posterior y motor Remontada):",
        "process_live": "⚡ Conectando cámara en vivo, esqueleto motriz y proyección AR de posesión en tiempo real...",
        "process_file": "🔄 Procesando el archivo guardado, desglosando errores de posicionamiento y estadísticas...",
        "coach_dash": "📊 Panel de Control de Entrenador AI Advanced",
        "pre_match": "🟢 Fase Pre-Partido y Simulación de Gemelo Digital",
        "in_match": "⚡ Tácticas En Vivo / En Partido y Control de Crisis de Remontada",
        "post_match": "🔴 Analíticas Post-Partido y Actualización de Lesiones Musculares",
        "market_title": "🔍 Tabla de Mercado de Fichajes Unificada (Compartida con Cazatalentos y Grandes Clubes)",
        "logo_lbl": "🛡️ Identidad Digital: Suba el escudo oficial del club para personalizar su área de trabajo aislada:"
    }
    "🇵🇹 Português": {
        "title": "🏪 Clubes de Divisão 2, 3, Amadores e Academias Privadas",
        "sub": "📌 Pacote Pequenos Clubes & Academies - Feito para gerenciar, alimentar e exibir talentos do clube de forma peer-to-peer soberana.",
        "price_label": "💰 Preço da Assinatura Mensal:",
        "features_title": "📋 Recursos Ativos:",
        "f1": "✅ Motor de Remontada e substituições ao vivo (50.000 simulações)",
        "f2": "✅ Painel do Treinador Avançado e Gêmeo Digital (Antes, Durante e Depois do Jogo)",
        "f3": "✅ Sistema Duplo de Vídeo & Escudo de Cibersegurança GDPR Isolado",
        "live_cam_lbl": "🎥 Canal 1: Ativar Câmera ao Vivo do Jogo (AI Live & AR Overlay) para dados em tempo real:",
        "upload_lbl": "📥 Canal 2: Carregar Vídeo Gravado do Jogo (Para análise pós-jogo profunda e simulação de Remontada):",
        "process_live": "⚡ Conectando câmera ao vivo, rastreamento físico e métricas AR de posse na tela...",
        "process_file": "🔄 Processando arquivo gravado, desmembrando erros de posicionamento e estatísticas...",
        "coach_dash": "📊 Painel de Controle do Treinador AI Avançado",
        "pre_match": "🟢 Fase Pré-Jogo & Simulação de Gêmeo Digital",
        "in_match": "⚡ Táticas Ao Vivo / No Jogo & Gerenciamento de Crise de Remontada",
        "post_match": "🔴 Análises Pós-Jogo & Atualização de Lesões Musculares",
        "market_title": "🔍 Tabela do Mercado Unificado de Transferências (Compartilhada com Olheiros e Grandes Clubes)",
        "logo_lbl": "🛡️ Identidade Digital: Carregue o escudo oficial do clube para customizar sua área soberana isolada:"
    }
}


