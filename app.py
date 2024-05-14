import streamlit as st
#import numpy as np
#import plotly.express as px
import pandas as pd
#import dtale as dt
#import plotly.graph_objects as go

#df = pd.read_csv("C:/Users/HP/Desktop/use-5/Use-case-5/Jadarat_data.csv")

st.title("  كيف تبحث عن فرصه عمل في السعودية؟ \n")

st.write("في أول يوم لي بعد حفل تخرّجي وتحقيق هدف التخرج، أصبح لدي هدف آخر وهو البحث عن فرصة عمل لكي أتطور مهنياً ومعرفياً، ولكي أحقق أحلامي في أن أصبح عنصرًا فعّالًا في المجتمع وأن أساعد في تحقيق رؤية موطني لعام 2023. لذلك، قمت بالانضمام إلى منصة جدارات")
st.write("وهي المنصة الموحدة للتوظيف ترافقك في رحلة البحث عن وظيفة، من لحظة البحث، إيجاد وظيفة مناسبة، إجراء مقابلات حتى تحصل على عرض وظيفي")
st.write("وعند تصفح المنصة وجدت مجموعه من البينات. توفر مجموعة البيانات معلومات عن إعلانات الوظائف في المملكة العربية السعودية من برنامج جدارات، بما في ذلك")
st.write("تفاصيل الشركة - وصف الوظيفة - المؤهلات المطلوبة - المهام الوظيفية - الراتب - تفاصيل العقد - سنوات الخبرة المطلوبة - مدينة وغيرها")



st.write("\n ")

st.write("في البداية اردت معرفة اكثر مدينة تحتوي على فرص وظيفية وكما هو موضح في الرسم البياني، فإن مدينة الرياض هي المنطقة الأكثر توظيفاً")




file_path = 'najla.png'
st.image(file_path, caption='اكثر المدن توفر في فرص العمل', use_column_width=True)


st.write(" \n ")

st.write("ومن خلال تحليل البيانات الموجودة في المنصة اتضح ان فرص العمل الاكثر تكون لحديثي التخرج وذلك بسبب احتياج السوق الى حديثي التخرج")

file_path = 'nn.png'
st.image(file_path, caption='اكثر المدن توفر في فرص العمل', use_column_width=True)


st.write("من خلال تحليل البيانات السابقه اتضح ان مدينه الرياض لديها اكثر فرص وظيفية وتستقطب حديثي التخرج وذلك بسبب ان الموظف حديث التخرج لديه خلفيه علميه حديثه وهذا يكون كاستثمار للمنظمة")