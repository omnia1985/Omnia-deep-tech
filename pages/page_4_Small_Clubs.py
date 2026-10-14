import streamlit as st
import time
import numpy as np
import pandas as pd

# إعداد الصفحة وتفعيل التصميم العريض
st.set_page_config(layout="wide")

# التصميم والتأثيرات السينمائية عالية التقنية (Experituelle) مع خلفية الملعب المتحركة والجماليات
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 4, 10, 0.9), rgba(0, 15, 5, 0.9)), 
                    url('https://unsplash.com');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }
    .coach-card {
        background: rgba(255, 255, 255, 0.03);
        border-right: 4px solid #ffcc00;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# استرجاع وتأمين اللغة المحددة من الجلسة المركزية لمنع اختفاء المحتوى
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
lang_key = "العربية"
for k in ["العربية", "English", "Français", "Italiano", "Español", "Português"]:
    if k in selected_lang:
        lang_key = k

# مصفوفة التراجم الكاملة والموحدة للغات (مغلقة تماماً عند نهاية اللغة الإسبانية)
P4_TXT = {
    'العربية': {
        'title': "🏪 أندية الدرجة 2 و3، أندية الهواة، والأكاديميات الخاصة",
        'sub': "📌 باقة الأندية الصغيرة والأكاديميات - إدارة المواهب وحمايتها سيبرانياً بمبدأ الند للند.",
        'price': "💰 قيمة الاشتراك: 500 دولار شهرياً",
        'logo_lbl': "🛡️ ارفع شعار النادي الرسمي لتخصيص الهوية وبدء الجلسة السيبرانية المعزولة:",
        'time_phase': "⏳ اختر طور التحليل الزمني للمباراة:",
        'pre': "🟢 قبل المباراة (تحليل الخصم والتوأم الرقمي)",
        'live': "⚡ أثناء المباراة (البث الحي والخطط المضادة)",
        'post': "🔴 بعد المباراة (التقرير التشريحي والإصابات)",
        'vid_live_lbl': "🎥 المسار الأول: تشغيل الكاميرا الحية (Universal AI Camera & AR Overlay)",
        'vid_old_lbl': "📂 المسار الثاني: رفع فيديو مسبق ومسجل للمباراة للتحليل العميق والتنظيف",
        'ai_tactical': "🧠 مساعد الذكاء الاصطناعي التكتيكي وطوارئ الريمونتادا (50,000 محاكاة): تم رصد ثغرة في الرواق الأيسر للخصم، نقترح التحول فوراً إلى خطة 3-5-2 الهجومية. نسبة العودة والانتصار هي 78%!",
        'ai_medical': "🩺 التقرير الطبي والنفسي الاستباقي (متلازمة اليوم السلبي): لغة جسد اللاعب تشير إلى إجهاد عضلي حاد ونرفزة مرتفعة (مؤشر التركيز: 62%)، نقترح استبداله لتفادي الكرت أو الإصابة العضلية.",
        'market_title': "📊 جدول بورصة الانتقالات الموحد والذكي المشترك (للبيع والإعارة)",
        'market_sub': "📌 يعرض كافة اللاعبين المتاحين فوق 16 سنة في المنظومة مع تشبيههم وقيمتهم السوقية (معزول ومحمي سيبرانياً من الاختراق وتجسس الأندية الأخرى).",
        'success_pub': "📥 تم تحديث الجدول ونشر البيانات بنجاح مع تشفير المعطيات وتفعيل التغبيش رقمياً."
    },
    'English': {
        'title': "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        'sub': "📌 Small Clubs Package - Secure Talent Management under Peer-to-Peer protocols.",
        'price': "💰 Subscription Price: $500 / Month",
        'logo_lbl': "🛡️ Upload Official Club Logo to authorize sandbox security session:",
        'time_phase': "⏳ Select Match Analytical Timeline Phase:",
        'pre': "🟢 Pre-Match (Opponent Analysis & Digital Twin)",
        'live': "⚡ In-Match (Live Feed & Tactical Counter-Plans)",
        'post': "🔴 Post-Match (Anatomical Report & Injury Prediction)",
        'vid_live_lbl': "🎥 Path 1: Activate Live Mobile Camera Feed (Universal AI Camera & AR Overlay)",
        'vid_old_lbl': "📂 Path 2: Upload Pre-recorded Match Video for Deep Analytics & Quality Restoration",
        'ai_tactical': "🧠 AI Tactical Assistant & Remontada Engine (50K Simulations): Weakness detected in opponent's left flank. We suggest shifting to 3-5-2. Win probability is 78%!",
        'ai_medical': "🩺 Proactive Medical & Psychological Report (Negative Day Syndrome): Player body language shows acute muscle fatigue and high stress (Focus: 62%). Substitution recommended to avoid red cards or injuries.",
        'market_title': "📊 Unified Global Transfer Marketplace Table (For Sale & Loan)",
        'market_sub': "📌 Displays all registered players over 16 with their market values and AI matching stars. Fully protected from competitor espionage.",
        'success_pub': "📥 Data successfully synchronized and published with active GDPR blurring shields."
    },
    'Français': {
        'title': "🏪 Clubs de Division 2, 3, Amateurs & Académies Privées",
        'sub': "📌 Pack Petits Clubs - Gestion sécurisée des talents et souveraineté Peer-to-Peer.",
        'price': "💰 Tarif de l'abonnement: 500 $ / Mois",
        'logo_lbl': "🛡️ Déposez le logo officiel du club pour activer la session sandbox sécurisée :",
        'time_phase': "⏳ Sélectionnez la phase temporelle de l'analyse :",
        'pre': "🟢 Avant-Match (Analyse de l'adversaire & Double Numérique)",
        'live': "⚡ En Direct (Flux Live & Contre-Tactiques Immédiates)",
        'post': "🔴 Après-Match (Rapport Anatomique & Prédiction des Blessures)",
        'vid_live_lbl': "🎥 Voie 1: Activer la caméra en direct du téléphone (AI Camera & AR Overlay)",
        'vid_old_lbl': "📂 Voie 2: Déposer une vidéo pré-enregistrée pour analyse approfondie et restauration",
        'ai_tactical': "🧠 Assistant Tactique IA & Moteur de Remontada (50K simulations): Faille détectée sur le flanc gauche adverse. Transition recommandée vers 3-5-2 (Taux de succès: 78%).",
        'ai_medical': "🩺 Rapport Médical & Psychologique Proactif (Syndrome du Jour Négatif): Fatigue musculaire aiguë et stress détectés (Focus: 62%). Remplacement conseillé.",
        'market_title': "📊 Tableau Mondial Unifié du Marché des Transferts (Vente & Prêt)",
        'market_sub': "📌 Affiche tous les profils de plus de 16 ans avec valeurs marchandes. Entièrement isolé contre l'espionnage.",
        'success_pub': "📥 Données synchronisées avec succès sous protection des masques GDPR."
    },
    'Italiano': {
        'title': "🏪 Club di Divisione 2, 3, Dilettanti e Accademie Private",
        'sub': "📌 Pacchetto Piccoli Club - Gestione sicura dei talenti e protocolli Peer-to-Peer.",
        'price': "💰 Prezzo Abbonamento: $500 / Mese",
        'logo_lbl': "🛡️ Carica il logo ufficiale del club per avviare la sessione sandbox protetta:",
        'time_phase': "⏳ Seleziona la fase temporale dell'analisi della partita:",
        'pre': "🟢 Pre-Partita (Analisi Avversario & Gemello Digitale)",
        'live': "⚡ Durante la Partita (Feed Live & Contro-Piani Tattici)",
        'post': "🔴 Post-Partita (Report Anatomico & Previsione Infortuni)",
        'vid_live_lbl': "🎥 Percorso 1: Attiva la telecamera live del telefono (AI Camera & AR Overlay)",
        'vid_old_lbl': "📂 Percorso 2: Carica video pre-registrato della partita per analisi profonda",
        'ai_tactical': "🧠 Assistente Tattico AI (50k Simulazioni): Rilevato punto debole sul lato sinistro avversario. Suggeriamo il passaggio al 3-5-2. Probabilità di successo 78%!",
        'ai_medical': "🩺 Report Medico e Psicologico (Sindrome del Giorno Negativo): La postura mostra affaticamento muscolare e alto stress (Focus: 62%). Sostituzione raccomandata.",
        'market_title': "📊 Tabella di Mercato Trasferimenti Unificata (Vendita & Prestito)",
        'market_sub': "📌 Mostra i giocatori sopra i 16 anni con valori di mercato e stelle corrispondenti. Protetto da spionaggio.",
        'success_pub': "📥 Dati pubblicati con successo con attivazione dei filtri di sfocatura GDPR."
    },
    'Español': {
        'title': "🏪 Clubes de División 2, 3, Amateurs y Academias Privadas",
        'sub': "📌 Paquete Clubes Pequeños - Gestión segura de talentos bajo entorno Peer-to-Peer.",
        'price': "💰 Precio de Suscripción: $500 / Mes",
        'logo_lbl': "🛡️ Suba el escudo oficial del club para autorizar la sesión sandbox segura:",
        'time_phase': "⏳ Seleccione la fase cronológica del análisis del partido:",
        'pre': "🟢 Pre-Partido (Análisis del Rival y Gemelo Digital)",
        'live': "⚡ En Vivo (Cámara en Directo y Planes Contratácticos)",
        'post': "🔴 Pos-Partido (Informe Anatómico y Predicción de Lesiones)",
        'vid_live_lbl': "🎥 Vía 1: Activar cámara en vivo desde móvil (Universal AI Camera & AR Overlay)",
        'vid_old_lbl': "📂 Vía 2: Subir video pregrabado del partido para restauración y análisis profundo",
        'ai_tactical': "🧠 Asistente Táctico IA y Motor de Remontada (50K Simulaciones): Brecha detectada en el flanco izquierdo rival. Se sugiere cambiar a 3-5-2. Éxito del 78%.",
        'ai_medical': "🩺 Informe Médico y Psicológico Proactivo (Síndrome del Día Negativo): Fatiga muscular aguda y alto estrés detectados (Enfoque: 62%). Se recomienda sustitución.",
        'market_title': "📊 Tabla Unificada del Mercado Global de Fichajes (Venta y Préstamo)",
        'market_sub': "📌 Muestra los jugadores mayores de 16 años con sus valores y estrellas de IA. Protegido contra espionaje entre clubes.",
        'success_pub': "📥 ¡Publicado con éxito! Escudo GDPR y difuminación digital activados automáticamente."
    }
}
