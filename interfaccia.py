import streamlit as st

import time
import sqlite3


# Configura la pagina con titolo e icona
st.set_page_config(page_title="Bar Accademia", page_icon=":cocktail:", layout="wide",)

# Configura il database
# Inclusione dei CSS e dei collegamenti ai framework
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .navbar {
            background-color: #007BFF;
            overflow: hidden;
            padding: 10px 0;
        }
        .navbar ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: space-around;
        }
        .navbar ul li {
            float: left;
        }
        .navbar ul li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }
        .navbar ul li a:hover {
            background-color: #0056b3;
            color: white;
        }
        .order-list {
            list-style-type: none;
            padding: 0;
        }
        .order-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #ddd;
        }
        .order-icon {
            font-size: 24px;
            margin-right: 10px;
        }
        .order-details {
            flex-grow: 1;
        }
        .order-total {
            font-weight: bold;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #007BFF;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/framework7/5.7.12/css/framework7.bundle.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/framework7/5.7.12/css/framework7.bundle.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
    <style type="text/css">
        /* Inserisci qui i tuoi stili personalizzati */
        body {
            font-family: 'Roboto', sans-serif;
        }
        .page-content {
            padding: 20px;
        }
        .block-title {
            font-size: 24px;
            font-weight: bold;
        }
        .item-title {
            font-size: 20px;
        }
        .item-subtitle {
            font-size: 16px;
            color: gray;
        }
        .item-text {
            font-size: 14px;
        }
        .text-color-black {
            color: black;
        }
        .total {
            font-weight: bold;
        }
    </style>
    
""", unsafe_allow_html=True)
# Navbar HTML
navbar = """
<nav class="navbar">
    <ul>
        <li style="color:white; font-size:30px"><b>L'Accademia</b></li>
    </ul>
</nav>
<script>
    function selectPage(page) {
        var parent = window.parent;
        parent.postMessage(page, '*');
    }
</script>
"""

# Mostra la navbar
st.markdown(navbar, unsafe_allow_html=True)

conn = sqlite3.connect('BarAccademia/db.sqlite3')
c = conn.cursor()

# Funzione per ottenere gli oggetti dal database
def get_objects(one=False):
    if not one:
        c.execute('SELECT id, data, n_scontrino, cliente, prodotto FROM ElencoOrdini_ordine ORDER BY id DESC')
    else:
        c.execute('SELECT id, data, n_scontrino, cliente, prodotto FROM ElencoOrdini_ordine ORDER BY id DESC LIMIT 1')
    
    return c.fetchall()




st.markdown(
    """
    <style>
    .title {
        color:rgb(47,89,182);  /* Modifica i valori RGB a tuo piacimento */
    }
    /* Allinea il contenuto a sinistra */
    .css-18e3th9 {
        text-align: left;
        max-width: 100%;
    }
    /* Rimuovi il padding */
    .css-1d391kg {
        padding: 0;
    }
    /* Imposta il body a tutto schermo */
    body {
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Usa HTML nel titolo per applicare la classe CSS




    
if "close_modal" not in st.session_state:
    st.session_state.close_modal = False
    


obj = get_objects()
first_run=False

write_container = st.empty()


while True:
    if "latest_id" not in st.session_state:
        st.session_state.latest_id = obj[0][0] if obj else None
        write_container.title("Nessuno scontrino presente")
    obj= get_objects(one=True)
    test=obj[0][0] if obj else -1
    if st.session_state.latest_id == test and first_run==False:
        write_container.empty()
        write_container.title("Scontrini recenti")
        obj = get_objects()
        if len(obj) >= 100:
            obj=obj[:100]

        
        order_list = ""
        for i,order in enumerate(obj):
                order_list += f"""<li>
                    <div class="order-details">
                        <div class="order-title" style="font-size: 30px;"><b>Scontrino N° {order[0]} -- {order[3]}</b></div>
                        <div class="order-date" style="font-size: 30px;"><b>{order[1]}</b></div>
                        <div class="order-client" style="font-size: 30px;"><b>{order[4]}</b></div>
                    </div>
                </li>
                """
        
        write_container.markdown(f"<ul class='order-list'>{order_list}</ul>", unsafe_allow_html=True)
        
        first_run=True
    elif st.session_state.latest_id != test and test!=-1:
        write_container.empty()
        markdown = f"""# <span style="color:rgb(47,89,182); font-size: 80px;">Ricevuta di Acquisto</span>

**<span style="color:black;font-size: 50px;">Data: {obj[0][1]} </span>**
----
**<span style="color:black;font-size: 50px;">Cliente: {obj[0][3]}</span>**
---
**<span style="color:black;font-size: 50px;">Prodotto: {obj[0][4]} </span>**
---
**<span style="color:black;font-size: 50px;">Numero Scontrino: {obj[0][2]} </span>**
---


""" 
        write_container.markdown(markdown, unsafe_allow_html=True)
        time.sleep(15)
        first_run=False
        st.session_state.latest_id = obj[0][0]
        
        
        
    
        
    

        
            
            
    
