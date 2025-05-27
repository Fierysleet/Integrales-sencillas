import streamlit as st
from sympy import symbols, sympify, integrate

# Título
st.title("Calculadora de Integrales")

# Input del usuario
funcion_input = st.text_input("Ingresa la función a integrar (en x):", value="x**2")

# Límites de integración (opcional)
limite_inferior = st.text_input("Límite inferior (opcional):", value="")
limite_superior = st.text_input("Límite superior (opcional):", value="")

# Símbolo de variable
x = symbols('x')

try:
    funcion = sympify(funcion_input)

    if limite_inferior and limite_superior:
        resultado = integrate(funcion, (x, float(limite_inferior), float(limite_superior)))
        st.success(f"La integral definida de {funcion_input} de {limite_inferior} a {limite_superior} es: {resultado}")
    else:
        resultado = integrate(funcion, x)
        st.success(f"La integral indefinida de {funcion_input} es: {resultado} + C")
except Exception as e:
    st.error(f"Error al procesar la función: {e}")
