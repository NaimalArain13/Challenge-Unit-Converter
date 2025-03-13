def conversion_unit(value, from_unit, to_unit, conversion_list):
    if from_unit not in conversion_list or to_unit not in conversion_list:
        return "Invalid Conversion"

    base_value = value / conversion_list[from_unit]
    
    converted_value = base_value * conversion_list[to_unit]
    
    return round(converted_value, 4)



def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid Conversion"
    
    