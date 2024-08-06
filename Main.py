import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid import GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder



def data_upload():
    df = pd.read_csv("Imoveis_DF_01_11_2018.csv", sep=';',on_bad_lines='warn')
    return df

df = data_upload()

#st.header('Este é o Streamlit Default Dataframe')
#st.dataframe(data=df)
#st.info(len(df))

_funct = st.sidebar.radio(label="Functions", options=['Display','Highlight'])

st.header('Este é o AgGrid Table')
gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=True, groupable=True)

if _funct == 'Display':
    sel_mode = st.radio('Selection Type', options=['single','multiple'])
    gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
    gridoptions = gd.build()
    grid_table = AgGrid(df,gridOptions=gridoptions,
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        height=500,
                        allow_unsafe_jscode=True,
                        theme='alpine')
    sel_row = grid_table["selected_rows"]
    st.write(sel_row)


AgGrid(df)
st.info(len(df))

