from utils import *

status_codes = [200, 404, 500, 201, 403, "oops", "nil"]

# for code in status_codes:
#     response = evaluate_build(code)
#     # print(response)
#     print(response["status"], response["result"])


def evaluate_build(status_code):
    if not isinstance(status_code, int):
        return {"error": "Invalid input"}


version = 15.0

if version >= 14.0:
    if version >= 16.0:
        print("Latest")
    else:
        print("Supported but not latest")