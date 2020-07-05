import requests

# response_bcc = "500"

# print(requests.status_codes)
# print(response_bcc.status_code)
# print(response_bcc.headers)
# print(type(response_bcc.headers))

#def check_response_code():
# if response_bcc.status_code == "200":
#     print("great! still alive")
# elif response_bcc.status_code == "400":
#       print("page you are looking for is unavailable")
# else:
#       print("OOPs something went wrong")

class web_status_checker:
    #response_bcc = str(requests.get("https://www.bbc.co.uk/"))

    def __init__(self):
        self.status = " checking status code"

    def check_response_code_with_requests(self):
        response_bcc = str(requests.get("https://www.bbc.co.uk/"))

        if response_bcc:
           return response_bcc + " great! still alive"
        elif response_bcc:
             return response_bcc + "page you are looking for is unavailable"
        else:
             return "OOPs something went wrong"
        return response_bcc

check_status_code = web_status_checker()

# print(check_status_code.response_bcc)
# print(check_status_code.check_response_code_with_requests())