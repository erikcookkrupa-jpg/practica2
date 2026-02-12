import streamlit as st

# -------------------------------
# MI EXAMEN DE CULTURA GENERAL
# Hecho por mí 
# -------------------------------

# Aquí guardo todas las preguntas
preguntas = [
    {
        "texto": "1. ¿Cuál es el planeta más cercano al Sol?",
        "opciones": ["Venus", "Marte", "Mercurio", "Júpiter"],
        "correcta": "Mercurio"
    },
    {
        "texto": "2. ¿Quién pintó la Mona Lisa?",
        "opciones": ["Picasso", "Van Gogh", "Leonardo da Vinci", "Dalí"],
        "correcta": "Leonardo da Vinci"
    },
    {
        "texto": "3. ¿En qué continente está Egipto?",
        "opciones": ["Asia", "África", "Europa", "América"],
        "correcta": "África"
    },
    {
        "texto": "4. ¿Cuánto es 7 x 8?",
        "opciones": ["54", "56", "64", "48"],
        "correcta": "56"
    },
    {
        "texto": "5. ¿Cuál es el océano más grande del mundo?",
        "opciones": ["Atlántico", "Índico", "Pacífico", "Ártico"],
        "correcta": "Pacífico"
    },
    {
        "texto": "6. ¿Qué gas necesitamos para respirar?",
        "opciones": ["Oxígeno", "Hidrógeno", "Nitrógeno", "Dióxido de carbono"],
        "correcta": "Oxígeno"
    },
    {
        "texto": "7. ¿Quién escribió Don Quijote de la Mancha?",
        "opciones": ["Federico García Lorca", "Miguel de Cervantes", "Lope de Vega", "Antonio Machado"],
        "correcta": "Miguel de Cervantes"
    },
    {
        "texto": "8. ¿Cuál es el río más largo del mundo?",
        "opciones": ["Amazonas", "Nilo", "Ebro", "Misisipi"],
        "correcta": "Nilo"
    },
    {
        "texto": "9. ¿Cuántos continentes hay en el mundo?",
        "opciones": ["5", "6", "7", "8"],
        "correcta": "7"
    },
    {
        "texto": "10. ¿Qué instrumento tiene teclas blancas y negras?",
        "opciones": ["Guitarra", "Flauta", "Piano", "Violín"],
        "correcta": "Piano"
    }
]

# Título
st.title(" Examen de cultura general - 3º ESO")
st.write("Responde a las 10 preguntas y pulsa el botón para ver tu nota final.")

# Formulario (para que no se recargue todo cada vez)
with st.form("formulario_examen"):

    respuestas_usuario = []

    for pregunta in preguntas:
        st.subheader(pregunta["texto"])
        eleccion = st.radio("Elige una opción:", pregunta["opciones"], key=pregunta["texto"])
        respuestas_usuario.append(eleccion)
        st.write("---")

    boton_enviar = st.form_submit_button("Entregar examen")

# Corrección
if boton_enviar:
    aciertos = 0
    total = len(preguntas)

    for i in range(total):
        if respuestas_usuario[i] == preguntas[i]["correcta"]:
            aciertos += 1

    nota = (aciertos / total) * 10

    st.divider()
    st.header(f"Tu nota final es: {round(nota,2)} / 10")

    if nota >= 5:
        st.success(f"¡Has aprobado muy bien! Has tenido {aciertos} aciertos.")
        st.balloons()
    else:
        st.error(f"Has suspendido. Has tenido {aciertos} aciertos. ¡Estudia mas y se el futuro de tu familia")

