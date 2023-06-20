import pickle
def save_model(model,file_name):
    pickl = {'model':model}	
    pickle.dump(pickl,open(file_name,"wb"))
    print("--ML Model saved--")
def load_model(file_name):
    with open(file_name,'rb') as pickled:
        model_dict = pickle.load(pickled)
        model = model_dict['model']
        print("--ML Model Loaded")
        return model