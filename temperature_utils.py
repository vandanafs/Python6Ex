from typing import Iterable, Tuple


from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    #'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
    #'{:2.2%}'.format(((fahrenheit_temp-32)/1.8000))
    print(round(((fahrenheit_temp-32)/1.8000),2))
    return  round(((fahrenheit_temp-32)/1.8000),2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    return int(celsius_temp*1.8000 +32.00)


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    output_tuple=[]
    for i in temperatures :
          if input_unit_of_measurement == 'f' :
             output_tuple.append(i,convert_to_celsius(i))
          elif input_unit_of_measurement == 'c':
             output_tuple.append(i,convert_to_fahrenheit(i))
          else:
             return tuple()
    return tuple(output_tuple)
