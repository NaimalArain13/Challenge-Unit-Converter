import streamlit as st
import conversion 
import conversion_rates

#title
st.title("Unit Converter ➗ ❌")

conversion_type = st.selectbox("Select the type of conversion: ", ["Length", "Weight", "Temperature","Time","Area","Speed"])

if conversion_type == "Length":
    from_unit = st.selectbox("From", list(conversion_rates.length_conversion.keys()))
    to_unit = st.selectbox("To", list(conversion_rates.length_conversion.keys()))
    value = st.number_input("Enter value", min_value=0.0 , format="%.2f")
    if st.button("Convert"):
        result = conversion.conversion_unit(value, from_unit, to_unit, conversion_rates.length_conversion)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
        
elif conversion_type == "Weight":
    from_unit = st.selectbox("From", list(conversion_rates.weight_conversion.keys()))
    to_unit = st.selectbox("To", list(conversion_rates.weight_conversion.keys()))
    value = st.number_input("Enter value", min_value=0.0 , format="%.2f")
    if st.button("Convert"):
        result = conversion.conversion_unit(value, from_unit, to_unit, conversion_rates.weight_conversion)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
        
elif conversion_type == "Area":
    from_unit = st.selectbox("From", list(conversion_rates.area_conversion.keys()))
    to_unit = st.selectbox("To", list(conversion_rates.area_conversion.keys()))
    value = st.number_input("Enter value", min_value=0.0 , format="%.2f")
    if st.button("Convert"):
        result = conversion.conversion_unit(value, from_unit, to_unit, conversion_rates.area_conversion)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
        
elif conversion_type == "Speed":
    from_unit = st.selectbox("From", list(conversion_rates.speed_conversion.keys()))
    to_unit = st.selectbox("To", list(conversion_rates.speed_conversion.keys()))
    value = st.number_input("Enter value", min_value=0.0 , format="%.2f")
    if st.button("Convert"):
        result = conversion.conversion_unit(value, from_unit, to_unit, conversion_rates.speed_conversion)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
        
elif conversion_type == "Time":
    from_unit = st.selectbox("From", list(conversion_rates.time_conversion.keys()))
    to_unit = st.selectbox("To", list(conversion_rates.time_conversion.keys()))
    value = st.number_input("Enter value", min_value=0.0 , format="%.2f")
    if st.button("Convert"):
        result = conversion.conversion_unit(value, from_unit, to_unit, conversion_rates.time_conversion)
        st.success(f"{value} {from_unit} = {result} {to_unit}")
        
elif conversion_type == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter value", min_value=0.0 , format="%.4f")
    if st.button("Convert"):
        result = conversion.convert_temperature(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")


st.write("Build by GIAIC Student ❤ Naimal Salahuddin")