import json
import pickle
import numpy as np

__model = None
__data = None
__location = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def load_saved_file():
    print("loading saved file ... start")
    global __data
    global __location
    global __model

    with open("./files/columns.json", 'r') as f:
        content = json.load(f)
        __data = content['data_columns']
        __location = __data[3:]
    
    if __model is None:
        with open("./files/house_pred_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved file...done")
    
    
def get_location_name():
    return __location

def get_data():
    return __data

if __name__ == "__main__":
    load_saved_file()
    # print(get_location_name())
    # print(get_data())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location