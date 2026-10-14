import streamlit as st
import time

st.set_page_config(layout="wide")

# جلب اللغة المحددة من الجلسة وضمان المزامنة التامة مع الصفحة الرئيسية
selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

# 1️⃣ القاموس المركزي المترجم بالكامل للغات الست لباقة الكشافين والتعاقدات
P3_TXT = {
    "🇸🇦 العربية": {
        "title": "🔍 لوحة تحكم الكشافين ووكلاء الأندية المعتمدين وسوق صفقات الانتقال الموحد", 
        "price": "💰 ثمن الاشتراك: 50 دولار شهرياً للوصول الكامل وقنوات التعاقد والشراء الفوري", 
        "commission": "🚨 عمولة المنصة الثابتة: يتم اقتطاع عمولة من 5% إلى 10% تلقائياً من القيمة المالية الإجمالية عند إتمام صفقات البيع النهائي أو الإعارة المؤقتة لحفظ حقوق المكوّن ومنع تخطي المنصة.",
        "market_title": "🚀 بورصة الانتقالات والصفقات الحية الموحدة (القسم الأول + القسم الثاني)",
        "filter_age": "فلترة فرز وتصفح مجموعات اللاعبين حسب الفئة السنية والمركز:",
        "filter_contract": "تصفح البورصة حسب نوع العقد التجاري المطلوب:",
        "btn_negotiate": "💼 بدء تفاوض رسمي وشراء العقد فوراً",
        "negotiate_success": "⚖️ امتثال المعاملات وعقود الانتقال وحماية الـ GDPR: تم فتح قناة المفاوضات الرسمية المشفرة بنجاح مع كشافة النادي المالك، وسيتم حساب واقتطاع حقوق التكوين والتضامن وعمولة المنصة آلياً فور توقيع الأطراف لضمان حقوق المكوّن المالي.",
        "alert_title": "📌 تنبيه إداري وأمني للكشافين والوكلاء (GDPR Shield):",
        "alert_desc": "وجوه كافة اللاعبين والحراس في القسمين الأول والثاني تظهر بعنصر التغبيش الرقمي التلقائي التام حماية للمعطيات الشخصية الدولية. يتم فك التغبيش رقمياً وبشكل رسمي بمجرد تقديم النادي أو الوكيل لعرض مالي جدي وبدء قنوات الشراء والتعاقد المشفرة الموضحة لضمان وتوثيق عمولة المنصة وحقوق المكوّن.",
        "f_all_p": "كل اللاعبين في المنظومة (فوق 16 سنة)", "f_p1": "القسم الأول: الناشئون المتاحون (فوق 16 سنة وإلى حدود 20 سنة)", "f_p2": "القسم الثاني: اللاعبون الكبار سينيور",
        "f_all_c": "كل عقود صفقات اللاعبين", "f_sale": "معروض للبيع النهائي (For Sale)", "f_loan": "متاح للإعارة المؤقتة (For Loan)",
        "th_id": "رمز اللاعب المشفر (ID)", "th_section": "القسم المستهدف", "th_status": "حالة العقد والطلب في البورصة", "th_star": "أقرب تشبيه عالمي مطابق", "th_value": "القيمة السوقية التقريبية", "th_blur": "عنصر التغبيش وحماية المعطيات"
    },
    "English": {
        "title": "🔍 Certified Scouts & Club Agents Dashboard & Transfer Market", 
        "price": "💰 Subscription Price: $50/Month for Full Access & Instant Purchase/Contract Channels", 
        "commission": "🚨 Platform Transaction Fee: A 5% to 10% commission is automatically deducted from the total value of any completed Sale or Loan transaction to secure developer rights.",
        "market_title": "🚀 Open Scouting Engine & Global Unified Live Transfer Market",
        "filter_age": "Filter players by age category and position:",
        "filter_contract": "Browse market by required commercial contract type:",
        "btn_negotiate": "💼 Start Official Negotiation & Buy Contract Instantly",
        "negotiate_success": "⚖️ Transaction Compliance & GDPR Protection: Encrypted official negotiation channel opened successfully with the owning club. Solidarity mechanisms and platform commission calculated automatically upon signing.",
        "alert_title": "📌 Security Alert for Certified Scouts & Agents (GDPR Shield):",
        "alert_desc": "All player and goalkeeper faces display automatic digital blurring for global data protection. Unblurring is processed officially once a formal financial bid is submitted through the purchase channel to secure platform fees and developer rights.",
        "f_all_p": "All Players in System (Over 16 Only)", "f_p1": "Section 1: Available Youth (16 to 20 Years Old)", "f_p2": "Section 2: Senior Professional Players",
        "f_all_c": "All Contract Types", "f_sale": "For Sale (Permanent)", "f_loan": "For Loan (Temporary)",
        "th_id": "Encrypted Player ID", "th_section": "Target Section", "th_status": "Market Status", "th_star": "Closest Matched Global Star", "th_value": "Estimated Market Value", "th_blur": "GDPR Blurring Status"
    },
    "Français": {
        "title": "🔍 Tableau de Bord des Recruteurs & Agents de Clubs (Marché des Transferts)", 
        "price": "💰 Tarif d'abonnement : 50$/Mois pour Accès Total & Canaux d'Achat/Contrat Instantanés", 
        "commission": "🚨 Commission de la plateforme : Une commission de 5% à 10% est prélevée automatiquement sur toute transaction de Vente ou de Prêt pour garantir les droits du formateur.",
        "market_title": "🚀 Bourse des Transferts Mondiale Unifiée & Contrats en Direct",
        "filter_age": "Filtrer les groupes de joueurs par catégorie d'âge :",
        "filter_contract": "Parcourir la bourse par type de contrat commercial requis :",
        "btn_negotiate": "💼 Lancer la négociation officielle & Acheter le contrat",
        "negotiate_success": "⚖️ Conformité & Protection GDPR: Canal chiffré ouvert avec le club propriétaire. Calcul automatique des mécanismes de solidarité et des commissions de plateforme.",
        "alert_title": "📌 Alerte de Sécurité pour les Recruteurs et Agents (GDPR Shield) :",
        "alert_desc": "Les visages de tous les joueurs et gardiens sont floutés automatiquement pour la protection des données. Le défloutage officiel s'active dès soumission d'une offre financière formelle via le canal d'achat.",
        "f_all_p": "Tous les joueurs du système (Plus de 16 ans uniquement)", "f_p1": "Section 1: Jeunes Disponibles (16 à 20 ans)", "f_p2": "Section 2: Joueurs Seniors Professionnels",
        "f_all_c": "Tous les types de contrat", "f_sale": "For Sale (Vente)", "f_loan": "For Loan (Prêt)",
        "th_id": "ID Joueur Chiffré", "th_section": "Section Cible", "th_status": "Statut du Marché", "th_star": "Star Mondiale la plus proche", "th_value": "Valeur Marchande Estimée", "th_blur": "Statut de Floutage GDPR"
    },
    "Italiano": {
        "title": "🔍 Pannello di Controllo Scout, Agenti di Club e Mercato Trasferimenti", 
        "price": "💰 Prezzo di abbonamento: $50/Mese per l'accesso completo e canali di acquisto istantaneo", 
        "commission": "🚨 Commissione della Piattaforma: Verrà applicata automaticamente una commissione dal 5% al 10% per garantire i diritti di formazione e impedire l'aggiramento del sistema.",
        "market_title": "🚀 Mercato Trasferimenti Globale Unificato & Trattative in Tempo Reale",
        "filter_age": "Filtra i gruppi di giocatori per categoria di età e ruolo:",
        "filter_contract": "Sfoglia il mercato in base al tipo di contrato richiesto:",
        "btn_negotiate": "💼 Avvia Trattativa Ufficiale e Acquista Contratto",
        "negotiate_success": "⚖️ Conformità delle transazioni e protezione GDPR: Canale crittografato aperto con il club. Il contributo di solidarietà e la commissione vengono calcolati automaticamente.",
        "alert_title": "📌 Avviso di Sicurezza per Scout e Agenti (GDPR Shield):",
        "alert_desc": "I volti di giocatori e portieri sono oscurati automaticamente. L'oscuramento viene rimosso ufficialmente non appena viene inviata un'offerta finanziaria seria attraverso il canale di acquisto.",
        "f_all_p": "Tutti i giocatori nel sistema (Solo sopra i 16 anni)", "f_p1": "Sezione 1: Giovani Disponibili (16-20 anni)", "f_p2": "Sezione 2: Giocatori Senior Professionisti",
        "f_all_c": "Tutti i contratti", "f_sale": "In Vendita (Permanente)", "f_loan": "In Prestito (Temporaneo)",
        "th_id": "ID Giocatore Crittografato", "th_section": "Sezione Target", "th_status": "Stato di Mercato", "th_star": "Stella Mondiale più vicina", "th_value": "Valore di Mercato Stimato", "th_blur": "Stato di Oscuramento GDPR"
    },
    "Español": {
        "title": "🔍 Panel de Control de Cazatalentos, Agentes de Clubes y Mercado de Fichajes", 
        "price": "💰 Precio de suscripción: $50/Mes para acceso completo y canales de compra directa", 
        "commission": "🚨 Comisión de la Plataforma: Se deduce automáticamente una comisión del 5% al 10% del valor total para asegurar los derechos de formación del club de origen.",
        "market_title": "🚀 Bolsa Global Unificada de Fichajes & Negociación Contractual",
        "filter_age": "Filtrar grupos de jugadores por categoría de edad y posición:",
        "filter_contract": "Explorar el mercado según el tipo de contrato comercial requerido:",
        "btn_negotiate": "💼 Iniciar Negociación Oficial y Comprar Contrato Directamente",
        "negotiate_success": "⚖️ GDPR y Cumplimiento Comercial: Canal de negociación encriptado abierto con el club propietario. Comisiones y derechos de formación calculados automáticamente.",
        "alert_title": "📌 Alerta de Seguridad para Cazatalentos y Agentes (GDPR Shield):",
        "alert_desc": "Los rostros de los jugadores en las secciones 1 y 2 están difuminados por protección de datos. El sistema procesa el desbloqueo al enviar una propuesta financiera formal a través del botón de compra.",
        "f_all_p": "Todos los jugadores (Mayores de 16 años únicamente)", "f_p1": "Sección 1: Juveniles Disponibles (16 a 20 años)", "f_p2": "Sección 2: Jugadores Seniors Profesionales",
        "f_all_c": "Todos los contratos", "f_sale": "En Venta (For Sale)", "f_loan": "Disponible para Cesión (For Loan)",
        "th_id": "ID Jugador Encriptado", "th_section": "Sección de Destino", "th_status": "Estado contractual", "th_star": "Estrella Global más cercana", "th_value": "Valor de Mercado Estimado", "th_blur": "Estado de Difuminado GDPR"
    },
