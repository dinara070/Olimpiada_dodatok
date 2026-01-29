import streamlit as st
import pandas as pd

# 1. Налаштування сторінки
st.set_page_config(
    page_title="Yasinskyi Geometry Olympiad",
    page_icon="📐",
    layout="centered"
)

# 2. МОВНИЙ СЛОВНИК (Розширений)
texts = {
    "UA": {
        "title": "Геометрична олімпіада імені В'ячеслава Ясінського",
        "menu_about": "Про олімпіаду",
        "menu_current": "Олімпіада 2026",
        "menu_archive": "Архів задач",
        "menu_results": "Результати",
        "menu_contacts": "Контакти",
        "about_yasinskyi": "В'ячеслав Ясінський — видатний український вчитель математики, майстер створення красивих олімпіадних задач. Олімпіада названа на його честь.",
        "rules_header": "Формат та правила",
        "rules_text": """
        * **Цільова аудиторія:** учні 8–11 класів.
        * **Кількість задач:** 5 авторських геометричних задач.
        * **Тривалість:** 4 години.
        * **Оцінювання:** кожна задача від 0 до 7 балів.
        """,
        "current_header": "Олімпіада 2026",
        "calendar": "📅 **Дата проведення:** Листопад 2026 року (уточнюється).",
        "registration_info": "Попередня реєстрація не потрібна. У день олімпіади тут з'явиться форма для надсилання розв'язків у форматі PDF.",
        "form_fields": "📝 **Поля форми:** ПІБ, e-mail, Країна, Місто, Школа, Клас.",
        "download_prob": "Умови задач (PDF)",
        "download_sol": "Розв'язання (PDF)",
        "archive_header": "Архів задач та розв'язків (2017–2025)",
        "contact_text": "Ми завжди шукаємо оригінальні геометричні задачі! Пишіть нам на:",
        "error_file": "Файли для цього року ще не завантажені в папку archive."
    },
    "EN": {
        "title": "Yasinskyi Geometry Olympiad",
        "menu_about": "About",
        "menu_current": "Olympiad 2026",
        "menu_archive": "Archive",
        "menu_results": "Results",
        "menu_contacts": "Contacts",
        "about_yasinskyi": "Vyacheslav Yasinskyi was a prominent Ukrainian mathematics teacher, a master of creating beautiful olympiad problems.",
        "rules_header": "Format and Rules",
        "rules_text": """
        * **Target audience:** students of grades 8–11.
        * **Number of problems:** 5 original geometry problems.
        * **Duration:** 4 hours.
        * **Scoring:** each problem is worth 0–7 points.
        """,
        "current_header": "Olympiad 2026",
        "calendar": "📅 **Date:** November 2026 (to be confirmed).",
        "registration_info": "Pre-registration is not required. A submission form for PDF solutions will be available on this page on the day of the Olympiad.",
        "form_fields": "📝 **Form fields:** Full name, E-mail, Country, City, School, Grade.",
        "download_prob": "Problems (PDF)",
        "download_sol": "Solutions (PDF)",
        "archive_header": "Problems & Solutions Archive (2017–2025)",
        "contact_text": "We are always looking for original geometry problems! Contact us at:",
        "error_file": "Files for this year have not been uploaded to the archive folder yet."
    }
}

# 3. БІЧНА ПАНЕЛЬ
st.sidebar.image("https://yasinskyi-geometry-olympiad.com/img/yasinskyi_photo.jpg", caption="В.А. Ясінський")
lang = st.sidebar.radio("Language / Мова", ["UA", "EN"])
t = texts[lang]

menu = st.sidebar.selectbox("Навігація", [
    t["menu_about"], 
    t["menu_current"], 
    t["menu_archive"], 
    t["menu_results"], 
    t["menu_contacts"]
])

# 4. ГОЛОВНИЙ КОНТЕНТ

if menu == t["menu_about"]:
    st.title(t["title"])
    st.write(f"### {t['about_yasinskyi']}")
    st.markdown("---")
    st.subheader(t["rules_header"])
    st.markdown(t["rules_text"])
    st.info("💡 Складність задач відповідає рівню національних олімпіад.")

elif menu == t["menu_current"]:
    st.header(t["current_header"])
    st.write(t["calendar"])
    st.write("### Реєстрація та подача робіт")
    st.success(t["registration_info"])
    st.markdown(t["form_fields"])
    st.warning("⚠️ Розв'язки приймаються лише у форматі PDF.")

elif menu == t["menu_archive"]:
    st.header(t["archive_header"])
    years = [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017]
    selected_year = st.selectbox("Оберіть рік / Select year", years)
    
    st.subheader(f"Рік {selected_year}")
    
    # Спроба додати дві мови для файлів у майбутньому
    path_prob = f"archive/{selected_year}/problems_ua.pdf"
    path_sol = f"archive/{selected_year}/solutions_ua.pdf"
    
    col_a, col_b = st.columns(2)
    try:
        with col_a:
            with open(path_prob, "rb") as f:
                st.download_button(t["download_prob"], data=f, file_name=f"Yasinskyi_{selected_year}_prob.pdf")
        with col_b:
            with open(path_sol, "rb") as f:
                st.download_button(t["download_sol"], data=f, file_name=f"Yasinskyi_{selected_year}_sol.pdf")
    except FileNotFoundError:
        st.error(t["error_file"])

elif menu == t["menu_results"]:
    st.header(t["menu_results"])
    st.write("📊 Статистика та результати попередніх років:")
    
    data = {
        "Рік (Year)": [2025, 2024, 2023, 2022, 2021, 2020],
        "Учасники (Participants)": [139, 58, 100, 145, 169, 136],
        "Країни (Countries)": [7, 6, 3, 2, 1, 1]
    }
    st.table(pd.DataFrame(data))
    st.caption("Детальні списки переможців доступні в PDF файлах архіву.")

elif menu == t["menu_contacts"]:
    st.header(t["menu_contacts"])
    st.write(t["contact_text"])
    st.code("yasinskyi.geometry.olympiad@gmail.com")
    st.markdown("""
    **Ми запрошуємо до співпраці:**
    * Математиків та педагогів.
    * Авторів геометричних задач.
    * Організаторів національних математичних змагань.
    """)

# 5. ФУТЕР
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey;'>© 2026 Yasinskyi Geometry Olympiad Mirror</div>", unsafe_allow_html=True)
