import streamlit as st

st.sidebar.title("Kullanıcı Girişleri")

#Kullanıcı Girişleri

yas_Baslangic = st.sidebar.number_input("Şu anki Yaşınız:" , min_value=18, max_value=65)
yas_Bitis = st.sidebar.number_input("Hedef Yaşınızı Girin", min_value=18, max_value=65)

aylik_Birikim = st.sidebar.number_input("Aylık Birikiminizi Girin: ", value=0)

daire_Fiyati = st.sidebar.number_input("Dailerin Fiyatı: ", value=0)

pesinat_Yuzdesi = st.sidebar.number_input("Peşinat Yüzdesi (%) : ", value=0)

kira_Getirisi = st.sidebar.number_input("Aylık Kira Getiriniz :", value=0)

kredi_Suresi = st.sidebar.number_input("Kredi Süreniz (Yıl): ", value=0)

gecen_Yil = yas_Bitis - yas_Baslangic

btn = st.sidebar.button("Hesapla")
solnot = st.sidebar.text("NOT: Eflasyon Ve Faiz Dikkate Alınmıyacaktır !!!")

#Başlangıc Parametreleri

toplam_birikim = 0
toplam_daire_sayisi = 0
toplam_kira_getirisi = 0

st.title("Birikim Hesapları")

if btn:
    if yas_Baslangic==0 or yas_Bitis==0 or aylik_Birikim or daire_Fiyati==0 or pesinat_Yuzdesi==0 or kira_Getirisi==0:
        st.sidebar.error("Lütfen Tüm Alanları Doldurunuz!!! ")


    else:
        pesinat = (daire_Fiyati * pesinat_Yuzdesi) /100
        kredi_Taksiti = (daire_Fiyati - pesinat) / (kredi_Suresi * 12)

        yas = yas_Baslangic
        while yas < yas_Bitis:
            toplam_birikim += aylik_Birikim + 12 #Bir  yıl birikim
            yas += 1

            #Eğer birikim peşinatı karşılıyorsa daireyi alır
            if toplam_birikim >= pesinat:
                toplam_birikim -= pesinat #Peşinatı öde
                toplam_daire_sayisi += 1  #Yeni daire alındı
                toplam_birikim += kira_Getirisi * 12 # Kiradan Gelen Yıllık Gelir
                toplam_birikim -= kredi_Taksiti * 12 # Her Yıl Kredi

    st.success("Birikim İşlemleriniz Hesaplanmıştır !!")

    st.write(f"Aylık Birikim: {aylik_Birikim} Tl")
    st.write(f"Geçen Yıl: {gecen_Yil} ")
    st.write(f"Toplam Daire Sayısı: {toplam_daire_sayisi} ")
    st.write(f"Toplam Yıllık Kira Geliri: {toplam_daire_sayisi * kira_Getirisi} TL ")
