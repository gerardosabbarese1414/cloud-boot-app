import streamlit as st

def scegli_materiale():
    st.subheader("Scegli il materiale del gioiello:")
    materiali = ["Oro", "Argento", "Platino"]
    scelta_materiale = st.selectbox("Seleziona il materiale", materiali)
    return scelta_materiale.lower()


def scegli_gemme():
    gemme_disponibili = ["Diamante", "Rubino", "Smeraldo", "Zaffiro"]

    st.subheader("Scegli le gemme da inserire nel gioiello:")
    gemme_selezionate = st.multiselect("Seleziona le gemme", gemme_disponibili)
    return [gemma.lower() for gemma in gemme_selezionate]


def crea_gioiello():
    materiale = scegli_materiale()
    gemme = scegli_gemme()

    st.success("Il tuo gioiello personalizzato è pronto!")
    st.write("Materiale:", materiale)
    st.write("Gemme:", ", ".join(gemme))

