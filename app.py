import streamlit as st
import qrcode

st.sidebar.title('QR code 생성하기')


qr_data = st.sidebar.text_area('글을 입력하세요 (공백 포함 1000자 이내)')
create_button = st.sidebar.button("QR code 생성")

if create_button:
    qr_img = qrcode.make(qr_data)
    delim = ','
#    st.text('이미지 크기:' + delim.join(qr_img.size))
 
    save_path = 'qr.png'
    qr_img.save(save_path)
    st.image(save_path)

    # 성공 문구 
    st.sidebar.success("생성됨!")
