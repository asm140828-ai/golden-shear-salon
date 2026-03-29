import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الأساسية
st.set_page_config(layout="wide", page_title="صالون المقص الذهبي", page_icon="✂️")

# 2. إضافة بعض التنسيقات لمحاكاة الوضع الداكن (Dark Mode)
st.markdown("""
<style>
    .stApp { background-color: #121212; color: #FFFFFF; }
</style>
""", unsafe_allow_html=True)

st.title("✂️ واجهة تصميم صالون المقص الذهبي")

# 3. تقسيم الواجهة إلى 3 أعمدة (يسار، وسط، يمين)
col1, col2, col3 = st.columns([1, 2.5, 1])

# --- العمود الأيسر: مكتبة الأثاث ---
with col1:
    st.subheader("🛋️ مكتبة الأثاث")
    st.button("➕ كرسي مخملي (Velvet Chair)")
    st.button("➕ مغسلة شعر (Backwash Station)")
    st.button("➕ ثريا كريستال (Chandelier)")
    st.button("➕ طاولة أظافر (Nail Desk)")

# --- العمود الأوسط: منطقة التصميم وسير العمل ---
with col2:
    st.subheader("🖼️ العرض ثلاثي الأبعاد (3D Viewport)")
    # في بايثون، لا يمكننا وضع محرر 3D كامل بسهولة، لذا سنضع رسالة توضيحية أو صورة
    st.info("مساحة عرض التصميم ثلاثي الأبعاد (تتطلب دمج WebGL في التطبيق النهائي)")
    
    st.write("---")
    st.subheader("⏳ سير العمل (Project Workflow)")
    st.progress(0.4) # محاكاة شريط التقدم عند مرحلة 3D Modeling
    st.write("**المرحلة الحالية:** النمذجة ثلاثية الأبعاد (3D Modeling)")
    st.write("**أدوار الفريق:** سارة (مصممة)، أليكس (3D)، جون (مشتريات)")

# --- العمود الأيمن: جدول الكميات والمساعد الذكي ---
with col3:
    st.subheader("📋 جدول الكميات (BOQ)")
    
    # إنشاء جدول الكميات المماثل للصورة
    data = {
        "العنصر": ["كرسي صالون ذهبي", "محطة مرايا", "مكتب استقبال"],
        "الكمية": [8, 10, 1],
        "المواصفات": ["تشطيب ذهبي", "إضاءة LED", "رخام ونحاس"],
        "الحالة": ["تم الوضع", "مؤكد", "جاري البحث"],
        "التكلفة": ["$450", "$1200", "$2800"]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True)
    
    st.write("---")
    st.subheader("🤖 المساعد (Assistant)")
    st.chat_message("assistant").write("مرحباً! كيف يمكنني مساعدتك في تصميم صالونك اليوم؟")
    user_input = st.chat_input("اكتب رسالتك...")
    if user_input:
        st.chat_message("user").write(user_input)
