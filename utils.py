def classify_engineer(years):
    if years < 3:
        return "Junior"
    elif years < 6:
        return "Mid"
    else:
        return "Senior"


#Trial - fail
# def evaluate_build(status_code):
#     if status_code == 200:
#         print("Build Successful")
#     elif status_code:
#         for i in range(400-499):
#             print("Client Error")
#     elif status_code:
#         for i in range(500-599):
#             print("Server Error")
#     else:
#         print("Unknown Status")

#Correction
def evaluate_build(status_code):
    if status_code == 200:
        return "Build Successful"
    elif 400 <= status_code <= 499:
        return "Client Error"
    elif 500 <= status_code <= 599:
        return "Server Error"
    else:
        return "Unknown Status"
    

#Function Returning Dictionary
def evaluate_build(status_code):
    if status_code == 200:
        return {"status": status_code, "result": "Success"}
    elif 400 <= status_code <= 499:
        return {"status": status_code, "result": "Client Error"}
    elif 500 <= status_code <= 599:
        return {"status": status_code, "result": "Server Error"}
    else:
        return {"status": status_code, "result": "Unknown"}
