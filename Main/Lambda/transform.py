import  pickle
import ast
from xgboost import XGBRegressor

def map_brand_to_numeric(brand):
    if brand == 'Maxfone':
        return 1
    elif brand == 'Infinix':
        return 2
    elif brand == 'Freeyond':
        return 3
    elif brand == 'XIAOMI':
        return 4
    elif brand == 'Tecno':
        return 5
    elif brand == 'Oppo':
        return 6
    elif brand == 'Nokia':
        return 7
    elif brand == 'Samsung':
        return 8
    elif brand == 'Huawei':
        return 9
    elif brand == 'Vivo':
        return 10
    elif brand == 'Realme':
        return 11
    elif brand == 'Sowhat':
        return 12
    elif brand == 'Apple':
        return 13
    else :
        return 14



def map_sim_type_to_numeric(sim_type):

    if sim_type == 'Dual':
        return 1
    elif sim_type =='Single':
        return 2
    else:
        return 3


def map_numeric_to_brand(number):
    if number == 1:
        return 'Maxfone'
    elif number == 2:
        return 'Infinix'
    elif number == 3:
        return 'Freeyond'
    elif number == 4:
        return 'XIAOMI'
    elif number == 5:
        return 'Tecno'
    elif number == 6:
        return 'Oppo'
    elif number == 7:
        return 'Nokia'
    elif number == 8:
        return 'Samsung'
    elif number == 9:
        return 'Huawei'
    elif number == 10:
        return 'Vivo'
    elif number == 11:
        return 'Realme'
    elif number == 12:
        return 'Sowhat'
    elif number == 13:
        return 'Apple'
    else:
        return 'Unknown'


def map_numeric_to_sim_type(number):
    if number == 1:
        return 'Dual'
    elif number == 2:
        return 'Single'
    else:
        return 'Unknown'







def transformation(original_list):

    model = pickle.load(open('ML_operations/xgb_model.pkl', 'rb'))

    print(original_list)
    original_list = ast.literal_eval(original_list)

    print(original_list)

    new_list = [
        map_brand_to_numeric(original_list[1]),  # Brand name
        float(original_list[3]),  # Screen size
        float(original_list[4]),  # RAM
        float(original_list[5]),  # Storage
        map_sim_type_to_numeric(original_list[7]),  # sim type
        float(original_list[8])  # Battery capacity
    ]
    print(new_list)

    price = model.predict([new_list])


    new_list[0] = map_numeric_to_brand(float(new_list[0]))
    new_list[4] = map_numeric_to_sim_type(float(new_list[4]))

    print(new_list)

    new_list.extend(price)

    return new_list


