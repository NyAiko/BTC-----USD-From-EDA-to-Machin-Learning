import numpy as np
import datetime
def create_windowed_values(price,window_size=29):
    price = price.values
    X = []
    y = []
    for i in range(len(price)-window_size+1):
        window = price[i:i+window_size]
        X.append(window[:-1])
        y.append(window[-1])
    X = np.array(X)
    y = np.array(y)
    return X,y

def predict_next_days(model,n_days = 20,window_size=29):
    data = pd.read_csv("data.csv")
    today = datetime.date.today().strftime("%Y-%m-%d")
    last_prices = data['Close'][-(window_size-1):].values
    first_pred_input = last_prices.reshape(1,-1)
    input_price = []
    predictions = []
    for j in range(n_days):
        print(j)
        predicted = model.predict(first_pred_input)
        predictions.append(predicted)
        for values in last_prices[1:]:
            input_price.append(values)
        input_price.append(predicted)
        predictions.append(predicted)
        first_pred_input = np.array(input_price).reshape(1,-1)
        input_price = []
    return predictions 