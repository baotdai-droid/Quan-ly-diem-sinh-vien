import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ứng dụng Quản lý Điểm Sinh Viên")

# Dữ liệu gốc
data = {
    'Họ và tên': ['Duy', 'Bình', 'Lê', 'Dung', 'Hoàng', 'Hoa', 'Vũ', 'Đạt', 'Nam', 'Nhi'],
    'Điểm chuyên cần': [9.0, 8.5, 10.0, 7.5, 9.5, 8.0, 6.5, 9.0, 10.0, 8.5],
    'Điểm giữa kỳ': [7.5, 8.0, 8.5, 6.0, 9.0, 7.0, 5.5, 8.5, 9.5, 7.5],
    'Điểm cuối kỳ': [8.0, 8.5, 9.0, 6.5, 9.5, 7.5, 6.0, 8.0, 9.0, 8.0]
}
df = pd.DataFrame(data)

# Tính điểm tổng kết
df['Tong_ket'] = (
    0.2 * df['Điểm chuyên cần'] +
    0.3 * df['Điểm giữa kỳ'] +
    0.5 * df['Điểm cuối kỳ']
)

# Hàm xếp loại
def xep_loai(score):
    if score >= 8.5:
        return 'Giỏi'
    elif score >= 7.0:
        return 'Khá'
    elif score >= 5.0:
        return 'Trung bình'
    else:
        return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# Hiển thị giao diện trên Streamlit
st.subheader("1. Bảng điểm chi tiết và xếp loại")
st.dataframe(df)

st.subheader("2. Thống kê chung")
col1, col2, col3, col4 = st.columns(4)
col1.metric("ĐTB lớp", round(df['Tong_ket'].mean(), 2))
col2.metric("Cao nhất", df['Tong_ket'].max())
col3.metric("Thấp nhất", df['Tong_ket'].min())
col4.metric("Số SV đạt (>=5)", int((df['Tong_ket'] >= 5.0).sum()))

st.subheader("3. Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(df['Họ và tên'], df['Tong_ket'], color='skyblue', edgecolor='black')
ax.set_title('Biểu đồ điểm tổng kết của sinh viên')
ax.set_xlabel('Tên sinh viên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=30)
st.pyplot(fig)
