import streamlit as st
import time

st.set_page_config(layout="wide")

# جلب اللغة المحددة من الجلسة وضمان المزامنة التامة مع الصفحة الرئيسية
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

# 1️⃣ القاموس المركزي المترجم بالكامل للغات الست لباقة اللاعبين الكبار
P2_TXT = {
    "🇸🇦 العربية": {
        "title": "🏃 قسم اللاعبين الكبار (سينيور - فوق 20 سنة)", 
        "price": "💰 ثمن الاشتراك: 30 دولار شهرياً للوصول التشريحي الشامل والجاهزية", 
        "live_cam_lbl": "🎥 تشغيل الكاميرا الحية بالهاتف لتتبع الهيكل الحركي والبيانات AR فورياً في الملعب:",
        "upload_lbl": "📥 أو ارفع فيديو مسبق ومخزن للمباراة (تحسين تلقائي، ترميم الضبابية والضوء الخافت):",
        "process_live": "⚡ جاري معالجة البث الحي وتتبع الهيكل الحركي للاعب وفك تداخل المدافعين فوراً...",
        "process_file": "🔄 جاري تشغيل معالجة وترميم الفيديو الرقمي المسبق واستخراج لوحة التحليلات العميقة...",
        "gdpr_warn": "🔒 بروتوكول حماية المعطيات الشخصية (GDPR) نشط: تم تفعيل عنصر التغبيش الرقمي الموحد على الوجه. لا يرى ملامح وجهك والبيانات الطبية والنفسية الحساسة إلا نفسك فقط لحين تقديم صفقات البيع لضمان حقوق المكوّن.",
        "stats_title": "📋 لوحة تحليلات الأداء والجاهزية الاحترافية المتكاملة (Full Analytics Stack)",
        "comp_lbl": "🔄 عنصر التشبيه المفتوح ومقارنة أرقامك الحالية مع نجوم قاعدة البيانات الـ 15 وحراس المرمى الدوليين:",
        "comp_active": "🔄 ميزة التطابق التكتيكي والتشبيه الرياضي نشطة الآن مع النجم العالمي المختار:",
        "weak_lbl": "⚠️ نسبة نقاط الضعف وثغرات الأداء الإجمالية المكتشفة:",
        "weak_desc": "15% (نقص طفيف في استغلال الكرات الهوائية الثانية والارتقاء العضلي).",
        "advice_lbl": "💡 نصائح وتوجيهات موجهة للمحترف:",
        "advice_desc": "يوصى بتكثيف تمارين القوة الارتدادية العضلية لرفع كفاءة الارتقاء الرأسي وتغطية أخطاء التمركز المستخرجة من مقطع الفيديو المحسن."
    },
    "English": {
        "title": "🏃 Senior Players Section (Over 20 Years Old)", 
        "price": "💰 Subscription Price: $30/Month for Full Anatomical, Tactical & Medical Stack", 
        "live_cam_lbl": "🎥 Turn on Live Mobile Camera for Real-Time AR Data & Pose Tracking on the pitch:",
        "upload_lbl": "📥 Or Upload a Preset Match Video (AI auto footage enhancement, blur & low-light restoration):",
        "process_live": "⚡ Initializing live mobile body pose tracking and real-time AR metrics projection...",
        "process_file": "🔄 Running digital video restoration on pre-recorded file and generating deep analytics stack...",
        "gdpr_warn": "🔒 GDPR Protection Protocol Active: Automatic digital face blurring enabled. Your identity, medical, and psychological stats remain private to you until a formal sale offer is presented to secure developer rights.",
        "stats_title": "📋 Full Professional Performance, Readiness & Tactical Analytics Stack",
        "comp_lbl": "🔄 Open Scouting Comparison System with our 15 Global Stars Database & International Goalkeepers:",
        "comp_active": "🔄 Tactical matching active with the selected global star:",
        "weak_lbl": "⚠️ Total Detected Performance Weaknesses & Gaps:",
        "weak_desc": "15% (Slight deficiency in second aerial ball duels and muscular lift).",
        "advice_lbl": "💡 Tailored Professional Advice:",
        "advice_desc": "It is recommended to intensify plyometric training to enhance vertical leap performance and cover the positioning errors extracted via AI video analysis."
    },
    "Français": {
        "title": "🏃 Section Joueurs Seniors (Plus de 20 ans)", 
        "price": "💰 Tarif d'abonnement : 30$ / Mois pour un accès anatomique, tactique et médical complet", 
        "live_cam_lbl": "🎥 Activer la Caméra Mobile en Direct (Suivi corporel et données AR instantanées sur le terrain) :",
        "upload_lbl": "📥 Ou Déposer une Vidéo de Match Enregistrée (Correction automatique d'éclairage faible et flou) :",
        "process_live": "⚡ Traitement du flux vidéo mobile en direct, suivi de posture et superposition AR...",
        "process_file": "🔄 Restauration numérique de la vidéo enregistrée et génération des analyses détaillées...",
        "gdpr_warn": "🔒 Protocole GDPR Actif : Le floutage numérique du visage est activé. Vos traits et données médicales sensibles restent confidentiels jusqu'à présentation d'une offre commerciale pour garantir vos droits.",
        "stats_title": "📋 Tableau de Bord des Analyses d'Performance et de Disponibilité Professionnelle",
        "comp_lbl": "🔄 Système de Comparaison Ouvert avec notre base de données des 15 Stars Mondiales & Gardiens :",
        "comp_active": "🔄 Correspondance tactique active avec la star mondiale sélectionnée :",
        "weak_lbl": "⚠️ Taux Global des Points Faibles et Failles de Performance détectés :",
        "weak_desc": "15% (Léger déficit dans les seconds ballons aériens et l'impulsion musculaire).",
        "advice_lbl": "💡 Conseils Personnalisés pour le Professionnel :",
        "advice_desc": "Il est recommandé d'intensifier l'entraînement pliométrique pour améliorer la détente verticale et corriger les erreurs de positionnement détectées par l'analyse vidéo IA."
    },
    "Italiano": {
        "title": "🏃 Sezione Giocatori Senior (Oltre 20 anni)", 
        "price": "💰 Prezzo di abbonamento: $30/Mese per l'accesso anatomico, tattico e medico completo", 
        "live_cam_lbl": "🎥 Attiva la Telecamera Live dal Cellulare (Tracciamento corporeo e dati AR istantanei sul campo):",
        "upload_lbl": "📥 Oppure Carica un Video Registrato (Ripristino automatico dell'oscurità e video borrosi):",
        "process_live": "⚡ Elaborazione del feed live da mobile, tracciamento della postura e metriche AR in tempo reale...",
        "process_file": "🔄 Ripristino digitale del video caricato e generazione del pannello di analisi approfondite...",
        "gdpr_warn": "🔒 Protocollo di Protezione GDPR Attivo: Oscuramento automatico del volto abilitato. Le tue statistiche e dati medici sensibili rimangono privati fino alla presentazione di un'offerta ufficiale.",
        "stats_title": "📋 Pannello di Controllo Integrato delle Performance e della Prontezza Professionale",
        "comp_lbl": "🔄 Sistema di Confronto Aperto con il nostro Database delle 15 Stelle Mondiali e Portieri:",
        "comp_active": "🔄 Corrispondenza tattica attiva con la stella mondiale selezionata:",
        "weak_lbl": "⚠️ Percentuale dei Punti Deboli e delle Carenze di Performance Rilevate:",
        "weak_desc": "15% (Lieve carenza nei duelli aerei sui secondi balloni e nell'elevazione muscolare).",
        "advice_lbl": "💡 Consigli Mirati per il Professionista:",
        "advice_desc": "Si consiglia di intensificare l'allenamento pliometrico per migliorare l'elevazione verticale e coprire gli errori di posizionamento estratti dall'analisi video dell'IA."
    },
    "Español": {
        "title": "🏃 Sección de Jugadores Seniors (Más de 20 años)", 
        "price": "💰 Precio de suscripción: $30/Mes para acceso anatómico, táctico y médico completo", 
        "live_cam_lbl": "🎥 Activar Cámara en Vivo del Móvil (Seguimiento de postura y datos AR instantáneos en la cancha):",
        "upload_lbl": "📥 O Subir Video Pregrabado del Partido (Restauración de luz tenue y videos borrosos de móviles):",
        "process_live": "⚡ Procesando transmisión en vivo, seguimiento de esqueleto motriz y métricas AR en pantalla...",
        "process_file": "🔄 Ejecutando restauración del archivo pregrabado y extrayendo el panel completo de analíticas...",
        "gdpr_warn": "🔒 Protocolo GDPR Activo: El difuminado de rostro digital está habilitado. Tu identidad y datos médicos sensibles son privados hasta el inicio de negociaciones comerciales formales.",
        "stats_title": "📋 Panel Integrado de Analíticas de Rendimiento y Disponibilidad Profesional",
        "comp_lbl": "🔄 Sistema de Comparación Abierto con nuestra Base de Datos de 15 Estrellas Globales y Guardametas:",
        "comp_active": "🔄 Emparejamiento táctico activo con la estrella mundial seleccionada:",
        "weak_lbl": "⚠️ Porcentaje Total de Puntos Débiles y Brechas de Rendimiento Detectados:",
        "weak_desc": "15% (Deficiencia leve en segundos balones aéreos y elevación muscular).",
        "advice_lbl": "💡 Consejos Técnicos para el Profesional:",
        "advice_desc": "Se recomienda intensificar el entrenamiento pliométrico para potenciar el salto vertical y corregir los errores de posicionamiento extraídos por el análisis de video por IA."
    },
    "🇵🇹 Português": {
        "title": "🏃 Seção de Jogadores Seniores (Mais de 20 anos)", 
        "price": "💰 Preço de assinatura: $30/Mês para acesso anatômico, tático e médico completo", 
        "live_cam_lbl": "🎥 Ativar Câmera ao Vivo do Celular (Rastreamento físico e exibição de dados AR na quadra):",
        "upload_lbl": "📥 Ou Carregar Vídeo Gravado (Restauração automática de pouca luz e gravações desfocadas):",
        "process_live": "⚡ Processando transmissão ao vivo, rastreamento de esqueleto motor e métricas AR instantâneas...",
        "process_file": "🔄 Restaurando o arquivo de vídeo gravado e gerando o painel de análise profunda de desempenho...",
        "gdpr_warn": "🔒 Protocolo de Proteção GDPR Ativo: Desfoque digital de rosto habilitado. Seus dados de desempenho, médicos e psicológicos são privados até que uma oferta formal seja feita.",
        "stats_title": "📋 Painel Integrado de Análises de Desempenho e Prontidão Profissional",
        "comp_lbl": "🔄 Sistema de Comparação Aberto com o nosso Banco de Dados de 15 Estrelas Globais e Goleiros:",
        "comp_active": "🔄 Correspondência tática ativa com a estrela mundial selecionada:",
        "weak_lbl": "⚠️ Percentual de Pontos Fracos e Falhas de Desempenho Identificados:",
        "weak_desc": "15% (Leve deficiência em segundas bolas aéreas e impulsão muscular).",
