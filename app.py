import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# #1 Tạo DataFrame
# =========================
data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em",
        "Vo Thi Giang",
        "Dang Van Hung",
        "Bui Thi Lan",
        "Do Van Minh",
        "Nguyen Thi Ngoc"
    ],
    "Chuyen_can": [9.0, 8.0, 7.5, 9.5, 6.5, 8.5, 7.0, 9.0, 5.5, 8.0],
    "Giua_ky": [8.5, 7.5, 8.0, 9.0, 6.0, 8.0, 7.0, 8.5, 5.0, 7.5],
    "Cuoi_ky": [9.0, 8.0, 8.5, 9.5, 6.5, 8.5, 7.5, 9.0, 5.5, 8.0]
}

df = pd.DataFrame(data)

# =========================
# #2 Tính điểm tổng kết
# =========================
df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
)

df["Tong_ket"] = df["Tong_ket"].round(2)

# =========================
# #3 Xếp loại
# =========================
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7.0:
        return "Khá"
    elif diem >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# =========================
# #4 Thống kê
# =========================
diem_trung_binh = df["Tong_ket"].mean()
sinh_vien_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sinh_vien_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
so_sinh_vien_dat = (df["Tong_ket"] >= 5).sum()

# =========================
# Giao diện Web App
# =========================
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Hiển thị bảng
st.header("Bảng điểm 10 sinh viên")

st.dataframe(
    df[
        [
            "Ho_ten",
            "Chuyen_can",
            "Giua_ky",
            "Cuoi_ky",
            "Tong_ket",
            "Xep_loai"
        ]
    ],
    use_container_width=True
)

# Thống kê
st.header("Thống kê kết quả lớp học")

st.write(
    f"**Điểm tổng kết trung bình:** {diem_trung_binh:.2f}"
)

st.write(
    f"**Sinh viên có điểm cao nhất:** "
    f"{sinh_vien_cao_nhat['Ho_ten']} - "
    f"{sinh_vien_cao_nhat['Tong_ket']:.2f} điểm"
)

st.write(
    f"**Sinh viên có điểm thấp nhất:** "
    f"{sinh_vien_thap_nhat['Ho_ten']} - "
    f"{sinh_vien_thap_nhat['Tong_ket']:.2f} điểm"
)

st.write(
    f"**Số sinh viên đạt:** {so_sinh_vien_dat} sinh viên"
)

# Tra cứu sinh viên
st.header("Tra cứu thông tin sinh viên")

danh_sach_sv = df["Ho_ten"].tolist()

sv_duoc_chon = st.selectbox(
    "Chọn sinh viên:",
    danh_sach_sv
)

thong_tin_sv = df[
    df["Ho_ten"] == sv_duoc_chon
].iloc[0]

st.write("### Thông tin chi tiết")

st.write(f"**Họ tên:** {thong_tin_sv['Ho_ten']}")
st.write(f"**Điểm chuyên cần:** {thong_tin_sv['Chuyen_can']}")
st.write(f"**Điểm giữa kỳ:** {thong_tin_sv['Giua_ky']}")
st.write(f"**Điểm cuối kỳ:** {thong_tin_sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {thong_tin_sv['Tong_ket']}")
st.write(f"**Xếp loại:** {thong_tin_sv['Xep_loai']}")

# Biểu đồ
st.header("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(
    df["Ho_ten"],
    df["Tong_ket"]
)

ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ và tên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

# Thông tin người thực hiện
st.markdown("---")

st.markdown(
    """
    <p style="font-size:12px; text-align:center;">
    Người thực hiện: Nguyễn Như Vinh - STT: 58<br>
    MSSV: ĐIỀN MSSV CỦA BẠN
    </p>
    """,
    unsafe_allow_html=True
)