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
