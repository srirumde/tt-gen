import google.generativeai as genai

genai.configure(api_key="AIzaSyBqnSi1_stHQamA3cJphqcIz0sErSIFljo")
models = genai.list_models()
for model in models:
    print(model.name)
