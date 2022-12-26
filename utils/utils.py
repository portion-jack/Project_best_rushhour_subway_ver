import os
def createFolder(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        pass

createFolder('data')
createFolder('data/final_data')
createFolder('private')

"""
private/_private_.py
def app_key():
    return your_api_key

https://openapi.sk.com/content/API
"""