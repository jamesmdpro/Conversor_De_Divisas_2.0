
from conversor import Conversor
from data_handler import get_exchange_rate
from input_handler import get_user_input
from output_handler import show_result

user_input = get_user_input()
exchange_rate = get_exchange_rate(user_input)


if user_input is not None:
    conversor = Conversor(user_input["cantidad"], user_input["cantidad"], user_input["cantidad"],
                          user_input["cantidad"], exchange_rate)

    if user_input["conversion"] == 1:
        result = conversor.convert_to_dollars()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} pesos Colombianos equivalen a {result} dólares.")

    elif user_input["conversion"] == 3:
        result = conversor.convert_to_dollarsMXN()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} pesos Mexicanos equivalen a {result} dólares.")

    elif user_input["conversion"] == 5:
        result = conversor.convert_to_dollarsPEN()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} Soles equivalen a {result} dólares.")

    elif user_input["conversion"] == 2:
        result = conversor.convert_to_pesos()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} dólares equivalen a {result} pesos colombianos. ")

    elif user_input["conversion"] == 4:
        result = conversor.convert_to_pesosMXN()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} dólares equivalen a {result} pesos Mexicanos. ")

    else:
        result = conversor.convert_to_pesosPEN()
        result = round(result, 1)
        show_result(f"{user_input['cantidad']} dólares equivalen a {result} pesos Mexicanos. ")
