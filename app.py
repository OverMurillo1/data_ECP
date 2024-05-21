import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title='ECP - 2023', layout='wide', initial_sidebar_state='collapsed', page_icon='🖱️')
st.header('Encuesta de Cultura Política - ECP - 2023', divider="rainbow")

datos = pd.read_csv('Elecciones_partidos.csv')
datos.head(10)

col1, col2 = st.columns(2)

with col1:
    P5369Group = datos.groupby('P5369').agg({'P5369':'count'})
    P5369Group.columns = ['Cantidad']
    fig, ax = plt.subplots(figsize=(10, 5))
    etiquetas = ('Si','No','No sabe/No informa')
    color = ['#bb8fce','#7fb3d5','#a3e4d7']
    container = ax.barh(etiquetas, P5369Group['Cantidad'], color=color)
    ax.bar_label(container)
    st.subheader('1. ¿Estaba usted inscrito(a) para votar en las elecciones presidenciales de 2022?')
    plt.xticks(visible=False)

    st.pyplot(fig)


with col2:
    code_0 = '''
        P5369Group = datos.groupby('P5369').agg({'P5369':'count'})
        P5369Group.columns = ['Cantidad']
        fig, ax = plt.subplots(figsize=(10, 5))
        etiquetas = ('Si','No','No sabe/No informa')
        color = ['#bb8fce','#7fb3d5','#a3e4d7']
        container = ax.barh(etiquetas, P5369Group['Cantidad'], color=color)
        ax.bar_label(container)
        st.subheader('1. ¿Estaba usted inscrito(a) para votar en las elecciones presidenciales de 2022?')
        plt.xticks(visible=False)

        st.pyplot(fig)    
    '''
    st.code(code_0, language='python')

st.divider()

P5370S1_A = datos['P5370S1'].value_counts().reset_index(name='Cantidad_A')
P5370S2_B = datos['P5370S2'].value_counts().reset_index(name='Cantidad_B')
P5370S3_C = datos['P5370S3'].value_counts().reset_index(name='Cantidad_C')
P5370S4_D = datos['P5370S4'].value_counts().reset_index(name='Cantidad_D')
P5370S5_E = datos['P5370S5'].value_counts().reset_index(name='Cantidad_E')
P5370S6_F = datos['P5370S6'].value_counts().reset_index(name='Cantidad_F')
P5370S7_G = datos['P5370S7'].value_counts().reset_index(name='Cantidad_G')
P5370S8_H = datos['P5370S8'].value_counts().reset_index(name='Cantidad_H')
P5370S9_I = datos['P5370S9'].value_counts().reset_index(name='Cantidad_I')
P5370S10_J = datos['P5370S10'].value_counts().reset_index(name='Cantidad_J')

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(1,10, figsize=(25,5), )
etiquetas = ('Si','No')
color = ['#bb8fce','#7fb3d5']

st.subheader('2. Por qué razones usted no estaba inscrito(a) para votar en las elecciones presidenciales de 2022')

ax1.set_title('a. Falta de Cedula', fontsize=6.5)
container = ax1.bar(etiquetas, P5370S1_A['Cantidad_A'], color=color)
ax1.bar_label(container)
ax1.yaxis.set_visible(False)

ax2.set_title('b. Desconocía dónde y cómo registrarse', fontsize=6.5)
container = ax2.bar(etiquetas, P5370S2_B['Cantidad_B'], color=color)
ax2.bar_label(container)
ax2.yaxis.set_visible(False)

ax3.set_title('c. Desconocía que tenía que inscribir la cédula', fontsize=6.5)
container = ax3.bar(etiquetas, P5370S3_C['Cantidad_C'], color=color)
ax3.bar_label(container)
ax3.yaxis.set_visible(False)

ax4.set_title('d. Estuvo fuera del país', fontsize=6.5)
container = ax4.bar(etiquetas, P5370S4_D['Cantidad_D'], color=color)
ax4.bar_label(container)
ax4.yaxis.set_visible(False)

ax5.set_title('e. Estuvo enfermo, o tiene una discapacidad', fontsize=6.5)
container = ax5.bar(etiquetas, P5370S5_E['Cantidad_E'], color=color)
ax5.bar_label(container)
ax5.yaxis.set_visible(False)

ax6.set_title('f. No cumplió con los plazos de registro.', fontsize=6.5)
container = ax6.bar(etiquetas, P5370S6_F['Cantidad_F'], color=color)
ax6.bar_label(container)
ax6.yaxis.set_visible(False)

ax7.set_title('g. Porque es extranjero', fontsize=6.5)
container = ax7.bar(etiquetas, P5370S7_G['Cantidad_G'], color=color)
ax7.bar_label(container)
ax7.yaxis.set_visible(False)

ax8.set_title('h. Porque había perdido sus derechos políticos', fontsize=6.5)
container = ax8.bar(etiquetas, P5370S8_H['Cantidad_H'], color=color)
ax8.bar_label(container)
ax8.yaxis.set_visible(False)

ax9.set_title('i. Desinterés', fontsize=6.5)
container = ax9.bar(etiquetas, P5370S9_I['Cantidad_I'], color=color)
ax9.bar_label(container)
ax9.yaxis.set_visible(False)

ax10.set_title('j. Otra razón', fontsize=6.5)
container = ax10.bar(etiquetas, P5370S10_J['Cantidad_J'], color=color)
ax10.bar_label(container)
ax10.yaxis.set_visible(False)

st.pyplot(fig)

st.divider()

code_1 = '''
    P5370S1_A = datos['P5370S1'].value_counts().reset_index(name='Cantidad_A')
    P5370S2_B = datos['P5370S2'].value_counts().reset_index(name='Cantidad_B')
    P5370S3_C = datos['P5370S3'].value_counts().reset_index(name='Cantidad_C')
    P5370S4_D = datos['P5370S4'].value_counts().reset_index(name='Cantidad_D')
    P5370S5_E = datos['P5370S5'].value_counts().reset_index(name='Cantidad_E')
    P5370S6_F = datos['P5370S6'].value_counts().reset_index(name='Cantidad_F')
    P5370S7_G = datos['P5370S7'].value_counts().reset_index(name='Cantidad_G')
    P5370S8_H = datos['P5370S8'].value_counts().reset_index(name='Cantidad_H')
    P5370S9_I = datos['P5370S9'].value_counts().reset_index(name='Cantidad_I')
    P5370S10_J = datos['P5370S10'].value_counts().reset_index(name='Cantidad_J')

    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10) = plt.subplots(1,10, figsize=(25,5), )
    etiquetas = ('Si','No')
    color = ['#bb8fce','#7fb3d5']

    st.subheader('2. Por qué razones usted no estaba inscrito(a) para votar en las elecciones presidenciales de 2022')

    ax1.set_title('a. Falta de Cedula', fontsize=6.5)
    container = ax1.bar(etiquetas, P5370S1_A['Cantidad_A'], color=color)
    ax1.bar_label(container)
    ax1.yaxis.set_visible(False)

    ax2.set_title('b. Desconocía dónde y cómo registrarse', fontsize=6.5)
    container = ax2.bar(etiquetas, P5370S2_B['Cantidad_B'], color=color)
    ax2.bar_label(container)
    ax2.yaxis.set_visible(False)

    ax3.set_title('c. Desconocía que tenía que inscribir la cédula', fontsize=6.5)
    container = ax3.bar(etiquetas, P5370S3_C['Cantidad_C'], color=color)
    ax3.bar_label(container)
    ax3.yaxis.set_visible(False)

    ax4.set_title('d. Estuvo fuera del país', fontsize=6.5)
    container = ax4.bar(etiquetas, P5370S4_D['Cantidad_D'], color=color)
    ax4.bar_label(container)
    ax4.yaxis.set_visible(False)

    ax5.set_title('e. Estuvo enfermo, o tiene una discapacidad', fontsize=6.5)
    container = ax5.bar(etiquetas, P5370S5_E['Cantidad_E'], color=color)
    ax5.bar_label(container)
    ax5.yaxis.set_visible(False)

    ax6.set_title('f. No cumplió con los plazos de registro.', fontsize=6.5)
    container = ax6.bar(etiquetas, P5370S6_F['Cantidad_F'], color=color)
    ax6.bar_label(container)
    ax6.yaxis.set_visible(False)

    ax7.set_title('g. Porque es extranjero', fontsize=6.5)
    container = ax7.bar(etiquetas, P5370S7_G['Cantidad_G'], color=color)
    ax7.bar_label(container)
    ax7.yaxis.set_visible(False)

    ax8.set_title('h. Porque había perdido sus derechos políticos', fontsize=6.5)
    container = ax8.bar(etiquetas, P5370S8_H['Cantidad_H'], color=color)
    ax8.bar_label(container)
    ax8.yaxis.set_visible(False)

    ax9.set_title('i. Desinterés', fontsize=6.5)
    container = ax9.bar(etiquetas, P5370S9_I['Cantidad_I'], color=color)
    ax9.bar_label(container)
    ax9.yaxis.set_visible(False)

    ax10.set_title('j. Otra razón', fontsize=6.5)
    container = ax10.bar(etiquetas, P5370S10_J['Cantidad_J'], color=color)
    ax10.bar_label(container)
    ax10.yaxis.set_visible(False)

    st.pyplot(fig)
    '''
st.code(code_1, language='python')


st.divider()

col3, col4 = st.columns(2)

with col3:
    P6933Group = datos.groupby('P6933').agg({'P6933':'count'})
    P6933Group.columns = ['Cantidad']

    fig, ax = plt.subplots(figsize=(10, 5))
    etiquetas = ('Si','No','No sabe/No informa')
    color = ['#bb8fce','#7fb3d5','#a3e4d7']

    st.subheader('3. ¿Votó usted en las elecciones presidenciales de 2022?')
    container = ax.pie(labels=etiquetas, x=P6933Group['Cantidad'], autopct='%1.1f%%', colors=color)
    ax.legend(title='Porcentaje')
    st.pyplot(fig)

with col4:
    code_2 = '''
        P6933Group = datos.groupby('P6933').agg({'P6933':'count'})
        P6933Group.columns = ['Cantidad']

        fig, ax = plt.subplots(figsize=(10, 5))
        etiquetas = ('Si','No','No sabe/No informa')
        color = ['#bb8fce','#7fb3d5','#a3e4d7']

        st.subheader('3. ¿Votó usted en las elecciones presidenciales de 2022?')
        container = ax.pie(labels=etiquetas, x=P6933Group['Cantidad'], autopct='%1.1f%%', colors=color)
        ax.legend(title='Porcentaje')
        st.pyplot(fig)
    '''
    st.code(code_2, language='python')

st.divider()

Filtered_Columns =  datos[['P5336S1','P5336S6','P5336S7','P5336S8','P5336S10','P5336S11','P5336S13','P5336S14','P5336S15','P5336S17','P5336S19','P5336S20','P5336S22','P5336S23','P5336S12']]
resultados = []

for col in Filtered_Columns:
        temp_df = Filtered_Columns.groupby(col).agg({col: 'count'})
        temp_df.columns = ['Cantidad']
        temp_df = temp_df.reset_index()
        df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
        cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
        resultados.append({'Preguntas': col, 'Cantidad': cantidad})
        df_final = pd.DataFrame(resultados)

st.subheader('4. Por qué razones usted no votó en las elecciones presidenciales de 2022:')
etiquetas = (
            'a.Tenía menos de 18 años',
            'b. Los políticos son corruptos',
            'c. Los partidos o movimientos políticos no representan a los ciudadanos',
            'd. Los candidatos prometen y no cumplen',
            'e. Falta de credibilidad en el proceso electoral (en las diferentes etapas)',
            'f. Desinterés',
            'g. Inseguridad (por temor/miedo)',
            'h. Falta de puestos de votación',
            'i. Dificultad de acceso a los  puestos de votación (distancia, transporte, condiciones precarias de las vías, etc.)',
            'j. Costos de transporte en que se incurre para registrarse o para votar',
            'k. Desinformación de como votar (falta de pedagogía electoral)',
            'l. Problemas con la cédula (se le perdió, se la robaron, se la escondieron)',
            'm. Tenía que trabajar',
            'n. Tiene una discapacidad o estuvo enfermo(a), y no contó con las condiciones y/o la asistencia necesarias para poder votar',
            'o. Otra'
            )

fig, ax = plt.subplots(figsize=(15, 6))
ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'])

plt.xlabel('')
plt.ylabel('Cantidad')
plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o'], rotation=0)
plt.legend(ax, etiquetas, title="Razones", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig)

code_3 = '''
    Filtered_Columns =  datos[['P5336S1','P5336S6','P5336S7','P5336S8','P5336S10','P5336S11','P5336S13','P5336S14','P5336S15','P5336S17','P5336S19','P5336S20','P5336S22','P5336S23','P5336S12']]
    resultados = []

    for col in Filtered_Columns:
            temp_df = Filtered_Columns.groupby(col).agg({col: 'count'})
            temp_df.columns = ['Cantidad']
            temp_df = temp_df.reset_index()
            df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
            cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
            resultados.append({'Preguntas': col, 'Cantidad': cantidad})
            df_final = pd.DataFrame(resultados)

    st.subheader('4. Por qué razones usted no votó en las elecciones presidenciales de 2022:')
    etiquetas = (
                'a.Tenía menos de 18 años',
                'b. Los políticos son corruptos',
                'c. Los partidos o movimientos políticos no representan a los ciudadanos',
                'd. Los candidatos prometen y no cumplen',
                'e. Falta de credibilidad en el proceso electoral (en las diferentes etapas)',
                'f. Desinterés',
                'g. Inseguridad (por temor/miedo)',
                'h. Falta de puestos de votación',
                'i. Dificultad de acceso a los  puestos de votación (distancia, transporte, condiciones precarias de las vías, etc.)',
                'j. Costos de transporte en que se incurre para registrarse o para votar',
                'k. Desinformación de como votar (falta de pedagogía electoral)',
                'l. Problemas con la cédula (se le perdió, se la robaron, se la escondieron)',
                'm. Tenía que trabajar',
                'n. Tiene una discapacidad o estuvo enfermo(a), y no contó con las condiciones y/o la asistencia necesarias para poder votar',
                'o. Otra'
                )

    fig, ax = plt.subplots(figsize=(15, 6))
    ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'])

  plt.xlabel('')
    plt.ylabel('Cantidad')
    plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o'], rotation=0)
    plt.legend(ax, etiquetas, title="Razones", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
    '''
st.code(code_3, language='python')
st.divider()

Columnas_Filtradas = datos[['P5337S1','P5337S2','P5337S3','P5337S4','P5337S5','P5337S6','P5337S8','P5337S7']]
resultados = []

for col in Columnas_Filtradas:
        temp_df = Columnas_Filtradas.groupby(col).agg({col: 'count'})
        temp_df.columns = ['Cantidad']
        temp_df = temp_df.reset_index()
        df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
        cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
        resultados.append({'Preguntas': col, 'Cantidad': cantidad})
        df_final = pd.DataFrame(resultados)
    
st.subheader('5. Cuáles fueron las razones por las que usted votó en las elecciones presidenciales de 2022:')
etiquetas = (
            'a. Por costumbre',
            'b. Para que la situación del país mejore',
            'c. Para ejercer el derecho y el deber ciudadano a opinar y participar',
            'd. Por apoyar a un candidato(a) específico(a)',
            'e. Para protestar contra los corruptos',
            'f. Porque le dieron o prometieron algo a cambio del voto',
            'g. Por presiones de otros',
            'h. Otra razón'
        )

colores = ['#bb8fce', '#d1a6dd', '#e7bde9', '#794984', '#f0d1f2', '#f8e4fb', '#a578b5', '#8f609c']
fig, ax = plt.subplots(figsize=(15, 6))
ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'], color=colores)

plt.xlabel('')
plt.ylabel('Cantidad')
plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], rotation=0)
plt.legend(ax, etiquetas, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig)

code_4 = '''
    Columnas_Filtradas = datos[['P5337S1','P5337S2','P5337S3','P5337S4','P5337S5','P5337S6','P5337S8','P5337S7']]
    resultados = []

    for col in Columnas_Filtradas:
            temp_df = Columnas_Filtradas.groupby(col).agg({col: 'count'})
            temp_df.columns = ['Cantidad']
            temp_df = temp_df.reset_index()
            df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
            cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
            resultados.append({'Preguntas': col, 'Cantidad': cantidad})
            df_final = pd.DataFrame(resultados)
        
    st.subheader('5. Cuáles fueron las razones por las que usted votó en las elecciones presidenciales de 2022:')
    etiquetas = (
                'a. Por costumbre',
                'b. Para que la situación del país mejore',
                'c. Para ejercer el derecho y el deber ciudadano a opinar y participar',
                'd. Por apoyar a un candidato(a) específico(a)',
                'e. Para protestar contra los corruptos',
                'f. Porque le dieron o prometieron algo a cambio del voto',
                'g. Por presiones de otros',
                'h. Otra razón'
            )

    colores = ['#bb8fce', '#d1a6dd', '#e7bde9', '#794984', '#f0d1f2', '#f8e4fb', '#a578b5', '#8f609c']
    fig, ax = plt.subplots(figsize=(15, 6))
    ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'], color=colores)

    plt.xlabel('')
    plt.ylabel('Cantidad')
    plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], rotation=0)
    plt.legend(ax, etiquetas, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
'''
st.code(code_4, language='python')

st.divider()

columns_filter = datos[['P5338S1','P5338S2','P5338S3','P5338S4','P5338S5','P5338S7','P5338S8','P5338S10','P5338S11','P5338S6']]
resultados = []

for col in columns_filter:
        temp_df = columns_filter.groupby(col).agg({col: 'count'})
        temp_df.columns = ['Cantidad']
        temp_df = temp_df.reset_index()
        df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
        cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
        resultados.append({'Preguntas': col, 'Cantidad': cantidad})
        df_final = pd.DataFrame(resultados)

st.subheader('6. Usted tuvo alguna de las siguientes dificultades al momento de votar en las elecciones presidenciales del 2022:')
etiquetas = (
        'a. Se le hizo difícil utilizar el tarjetón electoral',
        'b. Olvidó el número de su candidato(a)',
        'c. Se le dificultó encontrar el logo del partido o movimiento político',
        'd. Los jurados de votación no le dieron suficientes indicaciones',
        'e. Su cédula no apareció en las listas de la Registraduría',
        'f. Se le dificultó entender el tarjetón por encontrarse en un idioma diferente al propio',
        'g. Dificultad para transportarse a la mesa de votación',
        'h. Las filas para votar eran demasiado largas',
        'i. Hubo violencia en, o alrededor de las mesas de votación',
        'j. Otra'   
)

fig, ax = plt.subplots(figsize=(15, 6))
ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'])

plt.xlabel('')
plt.ylabel('Cantidad')
plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'], rotation=0)
plt.legend(ax, etiquetas, title="Razones", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
st.pyplot(fig)

st.divider()
code_5 = '''
    columns_filter = datos[['P5338S1','P5338S2','P5338S3','P5338S4','P5338S5','P5338S7','P5338S8','P5338S10','P5338S11','P5338S6']]
    resultados = []

    for col in columns_filter:
            temp_df = columns_filter.groupby(col).agg({col: 'count'})
            temp_df.columns = ['Cantidad']
            temp_df = temp_df.reset_index()
            df_temporal = temp_df[temp_df[col] == 1].copy()  # Hacer una copia explícita
            cantidad = df_temporal['Cantidad'].sum()  # Sumar las cantidades
            resultados.append({'Preguntas': col, 'Cantidad': cantidad})
            df_final = pd.DataFrame(resultados)

    st.subheader('6. Usted tuvo alguna de las siguientes dificultades al momento de votar en las elecciones presidenciales del 2022:')
    etiquetas = (
            'a. Se le hizo difícil utilizar el tarjetón electoral',
            'b. Olvidó el número de su candidato(a)',
            'c. Se le dificultó encontrar el logo del partido o movimiento político',
            'd. Los jurados de votación no le dieron suficientes indicaciones',
            'e. Su cédula no apareció en las listas de la Registraduría',
            'f. Se le dificultó entender el tarjetón por encontrarse en un idioma diferente al propio',
            'g. Dificultad para transportarse a la mesa de votación',
            'h. Las filas para votar eran demasiado largas',
            'i. Hubo violencia en, o alrededor de las mesas de votación',
            'j. Otra'   
    )

    fig, ax = plt.subplots(figsize=(15, 6))
    ax = plt.bar(df_final['Preguntas'], df_final['Cantidad'])

    plt.xlabel('')
    plt.ylabel('Cantidad')
    plt.xticks(ticks=range(len(df_final['Preguntas'])), labels=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j'], rotation=0)
    plt.legend(ax, etiquetas, title="Razones", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    st.pyplot(fig)
'''
st.code(code_5, language='python')
st.divider()

col4, col5 = st.columns(2)

with col4:
    st.subheader('7. ¿Qué tan seguro(a) se sintió cuando fue a votar en las elecciones presidenciales de 2022?')
    P5371 = datos.groupby('P5371').agg({'P5371':'count'})
    P5371.columns = ['Cantidad']
    fig, ax = plt.subplots(figsize=(10,5))
    etiquetas = ('1. Muy inseguro(a)',
                        '2. Inseguro(a)',
                        '3. Ni seguro(a) ni inseguro(a)',
                        '4. Seguro(a)',
                        '5. Muy seguro(a)',
                        '98. No sabe',
                        '99. No informa'
        )
    container = ax.bar(etiquetas, P5371['Cantidad'])
    ax.bar_label(container)
    plt.xticks(rotation=90)
    plt.yticks(visible=False)
    st.pyplot(fig)

with col5:
    code_6 = '''
            st.subheader('7. ¿Qué tan seguro(a) se sintió cuando fue a votar en las elecciones presidenciales de 2022?')
            P5371 = datos.groupby('P5371').agg({'P5371':'count'})
            P5371.columns = ['Cantidad']
            fig, ax = plt.subplots(figsize=(10,5))
            etiquetas = ('1. Muy inseguro(a)',
                            '2. Inseguro(a)',
                            '3. Ni seguro(a) ni inseguro(a)',
                            '4. Seguro(a)',
                            '5. Muy seguro(a)',
                            '98. No sabe',
                            '99. No informa'
            )
            container = ax.bar(etiquetas, P5371['Cantidad'])
            ax.bar_label(container)
            plt.xticks(rotation=90)
            plt.yticks(visible=False)
            st.pyplot(fig)
    '''
    st.code(code_6, language='python')
st.divider()

col6, col7 = st.columns(2)

with col6:
    st.subheader('8. ¿Qué tan seguro se siente al participar en actividades relacionadas con elecciones?')
    P5372 = datos.groupby('P5372').agg({'P5372':'count'})
    P5372.columns = ['Cantidad']
    fig, ax = plt.subplots(figsize=(10,5))
    etiquetas = ('1. Muy inseguro(a)',
                        '2. Inseguro(a)',
                        '3. Ni seguro(a) ni inseguro(a)',
                        '4. Seguro(a)',
                        '5. Muy seguro(a)',
                        '98. No sabe',
                        '99. No informa'
        )
    container = ax.bar(etiquetas, P5372['Cantidad'])
    ax.bar_label(container)
    plt.xticks(rotation=90)
    plt.yticks(visible=False)
    st.pyplot(fig)

with col7:
    code_7 = '''
        st.subheader('8. ¿Qué tan seguro se siente al participar en actividades relacionadas con elecciones?')
        P5372 = datos.groupby('P5372').agg({'P5372':'count'})
        P5372.columns = ['Cantidad']
        fig, ax = plt.subplots(figsize=(10,5))
        etiquetas = ('1. Muy inseguro(a)',
                        '2. Inseguro(a)',
                        '3. Ni seguro(a) ni inseguro(a)',
                        '4. Seguro(a)',
                        '5. Muy seguro(a)',
                        '98. No sabe',
                        '99. No informa'
        )
        container = ax.bar(etiquetas, P5372['Cantidad'])
        ax.bar_label(container)
        plt.xticks(rotation=90)
        plt.yticks(visible=False)
        st.pyplot(fig)
    '''
    st.code(code_7, language='python')
st.divider()

col8, col9, col10 = st.columns(3)

P5339S1_1 = datos.groupby('P5339S1').agg({'P5339S1':'count'})
P5339S1_1.columns = ['Cantidad']
P5339S3_1 = datos.groupby('P5339S3').agg({'P5339S3':'count'})
P5339S3_1.columns = ['Cantidad']
P5339S2_1 = datos.groupby('P5339S2').agg({'P5339S2':'count'})
P5339S2_1.columns = ['Cantidad']


with col8:
    st.subheader('9. Considera usted que el proceso de conteo de votos es transparente:')
    st.text('a. En su municipio')
    fig, ax = plt.subplots(figsize=(10,5))
    etiquetas = (
        '1. Sí',
        '2. No',
        '98. No sabe',
        '99. No informa' )
    container = ax.bar(etiquetas, P5339S1_1['Cantidad'])
    ax.bar_label(container)
    plt.xticks(rotation=0)
    plt.yticks(visible=False)
    st.pyplot(fig)
with col9:
    st.text('b. En su departamento')
    fig, ax = plt.subplots(figsize=(10,5))
    etiquetas = (
        '1. Sí',
        '2. No',
        '98. No sabe',
        '99. No informa' )
    container = ax.bar(etiquetas, P5339S3_1['Cantidad'])
    ax.bar_label(container)
    plt.xticks(rotation=0)
    plt.yticks(visible=False)
    st.pyplot(fig)
with col10:
    st.text('c. En el resto de Colombia')
    fig, ax = plt.subplots(figsize=(10,5))
    etiquetas = (
            '1. Sí',
            '2. No',
            '98. No sabe',
            '99. No informa' )
    container = ax.bar(etiquetas, P5339S2_1['Cantidad'])
    ax.bar_label(container)
    plt.xticks(rotation=0)
    plt.yticks(visible=False)
    plt.show()
    st.pyplot(fig)
    
code_8 = '''
        P5339S1_1 = datos.groupby('P5339S1').agg({'P5339S1':'count'})
        P5339S1_1.columns = ['Cantidad']
        P5339S3_1 = datos.groupby('P5339S3').agg({'P5339S3':'count'})
        P5339S3_1.columns = ['Cantidad']
        P5339S2_1 = datos.groupby('P5339S2').agg({'P5339S2':'count'})
        P5339S2_1.columns = ['Cantidad']
        
        st.subheader('9. Considera usted que el proceso de conteo de votos es transparente:')
        st.text('a. En su municipio')
        fig, ax = plt.subplots(figsize=(10,5))
        etiquetas = (
            '1. Sí',
            '2. No',
            '98. No sabe',
            '99. No informa' )
        container = ax.bar(etiquetas, P5339S1_1['Cantidad'])
        ax.bar_label(container)
        plt.xticks(rotation=0)
        plt.yticks(visible=False)
        st.pyplot(fig)
    '''
st.code(code_8, language='python')
st.divider()

col11, col12 = st.columns(2)

with col11:
    P5328Group = datos.groupby('P5328').agg({'P5328': 'count'})
    P5328Group.columns = ['Cantidad']
    P5328Group = P5328Group.reset_index()

    etiquetas = {
        1: 'Izquierda',
        2: 'Izquierda',
        3: 'Izquierda',
        4: 'Centro Izquierda',
        5: 'Centro',
        6: 'Centro',
        7: 'Centro derecha',
        8: 'Derecha',
        9: 'Derecha',
        10: 'Derecha',
        98: 'No Sabe',
        99: 'No Informa'
    }

    st.subheader('10. Las personas cuando piensan en política utilizan los términos izquierda y derecha. En una escala de 1 a 10  donde 1 significa izquierda y 10 significa derecha ¿dónde se ubicaría usted?')
    
    P5328Group['Etiqueta'] = P5328Group['P5328'].map(etiquetas)
    fig, ax = plt.subplots(figsize=(10,5))
    ax = plt.barh(P5328Group['Etiqueta'], P5328Group['Cantidad'], color=['#bb8fce', '#7fb3d5', '#a3e4d7', '#d5dbdb', '#f5b7b1'])
    plt.xlabel('Cantidad')
    plt.ylabel('Posiciones Políticas')
    plt.title('Distribución de Posiciones Políticas')

    for bar in ax:
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.0f}', va='center')

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)
    
with col12:
    code_9 = '''
        P5328Group = datos.groupby('P5328').agg({'P5328': 'count'})
        P5328Group.columns = ['Cantidad']
        P5328Group = P5328Group.reset_index()

        etiquetas = {
            1: 'Izquierda',
            2: 'Izquierda',
            3: 'Izquierda',
            4: 'Centro Izquierda',
            5: 'Centro',
            6: 'Centro',
            7: 'Centro derecha',
            8: 'Derecha',
            9: 'Derecha',
            10: 'Derecha',
            98: 'No Sabe',
            99: 'No Informa'
        }

        P5328Group['Etiqueta'] = P5328Group['P5328'].map(etiquetas)

        fig, ax = plt.subplots(figsize=(10,5))
        ax = plt.barh(P5328Group['Etiqueta'], P5328Group['Cantidad'], color=['#bb8fce', '#7fb3d5', '#a3e4d7', '#d5dbdb', '#f5b7b1'])
        plt.xlabel('Cantidad')
        plt.ylabel('Posiciones Políticas')
        plt.title('Distribución de Posiciones Políticas')

        for bar in ax:
            plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{bar.get_width():.0f}', va='center')

        plt.grid(axis='x', linestyle='--', alpha=0.7)
        plt.tight_layout()
        st.pyplot(fig)
    '''
st.code(code_8, language='python')