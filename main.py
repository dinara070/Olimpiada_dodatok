import streamlit as st
import pandas as pd

# 1. Налаштування сторінки
st.set_page_config(
    page_title="Yasinskyi Geometry Olympiad",
    page_icon="📐",
    layout="centered"
)

# 2. МОВНИЙ СЛОВНИК
texts = {
    "UA": {
        "title": "Геометрична олімпіада імені В'ячеслава Ясінського",
        "menu_about": "Про олімпіаду",
        "menu_archive": "Архів задач",
        "menu_results": "Результати",
        "menu_contacts": "Контакти",
        "about_header": "Про олімпіаду",
        "about_text": "Геометрична олімпіада імені В'ячеслава Ясінського — це щорічне змагання, яке об'єднує поціновувачів геометричних задач. Олімпіада названа на честь видатного українського вчителя.",
        "archive_header": "Архів задач та розв'язків",
        "download_prob": "Умови задач (PDF)",
        "download_sol": "Розв'язання (PDF)",
        "contact_text": "З питань співпраці пишіть на:",
        "error_file": "Файли для цього року ще не завантажені в папку archive."
    },
    "EN": {
        "title": "Yasinskyi Geometry Olympiad",
        "menu_about": "About",
        "menu_archive": "Archive",
        "menu_results": "Results",
        "menu_contacts": "Contacts",
        "about_header": "About the Olympiad",
        "about_text": "The Yasinskyi Geometry Olympiad is an annual competition for geometry lovers, named after the famous Ukrainian teacher Vyacheslav Yasinskyi.",
        "archive_header": "Problems & Solutions Archive",
        "download_prob": "Problems (PDF)",
        "download_sol": "Solutions (PDF)",
        "contact_text": "For cooperation, contact us at:",
        "error_file": "Files for this year have not been uploaded to the archive folder yet."
    }
}

# 3. БІЧНА ПАНЕЛЬ (НАВІГАЦІЯ)
st.sidebar.image("https://yasinskyi-geometry-olympiad.com/img/yasinskyi_photo.jpg", caption="В.А. Ясінський")
lang = st.sidebar.radio("Language / Мова", ["UA", "EN"])
t = texts[lang]

menu = st.sidebar.selectbox("Меню", [t["menu_about"], t["menu_archive"], t["menu_results"], t["menu_contacts"]])

# 4. ГОЛОВНИЙ КОНТЕНТ

if menu == t["menu_about"]:
    st.title(t["title"])
    st.header(t["about_header"])
    st.write(t["about_text"])
    
    st.info("📌 **Формат:** 5 задач, 4 години. **Учасники:** 8-11 класи.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Рік заснування", "2017")
    with col2:
        st.metric("Наступна олімпіада", "Листопад 2026")

elif menu == t["menu_archive"]:
    st.header(t["archive_header"])
    
    # Список років (можна додавати нові)
    years = [2025, 2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017]
    selected_year = st.selectbox("Оберіть рік / Select year", years)
    
    st.subheader(f"Рік {selected_year}")
    
    # Шляхи до файлів у папці archive (структура: archive/2024/problems_ua.pdf)
    path_prob = f"archive/{selected_year}/problems_ua.pdf"
    path_sol = f"archive/{selected_year}/solutions_ua.pdf"
    
    col_a, col_b = st.columns(2)
    
    try:
        # Спроба відкрити та створити кнопку для умов
        with col_a:
            with open(path_prob, "rb") as f:
                st.download_button(t["download_prob"], data=f, file_name=f"Yasinskyi_{selected_year}_prob.pdf")
        
        # Спроба відкрити та створити кнопку для розв'язків
        with col_b:
            with open(path_sol, "rb") as f:
                st.download_button(t["download_sol"], data=f, file_name=f"Yasinskyi_{selected_year}_sol.pdf")
                
    except FileNotFoundError:
        st.error(t["error_file"])
        st.info(f"Очікувані шляхи: \n- {path_prob} \n- {path_sol}")

elif menu == t["menu_results"]:
    st.header(t["menu_results"])
    st.write("Статистика попередніх років:")
    
    data = {
        "Рік": [2025, 2024, 2023, 2022, 2021],
        "Учасників": [139, 58, 100, 145, 169],
        "Країн": [7, 6, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    st.table(df)

elif menu == t["menu_contacts"]:
    st.header(t["menu_contacts"])
    st.write(t["contact_text"])
    st.code("yasinskyi.geometry.olympiad@gmail.com")
    st.write("Ми завжди шукаємо оригінальні авторські задачі!")

# 5. ФУТЕР
st.markdown("---")
st.caption("© 2026 Yasinskyi Geometry Olympiad Mirror")
