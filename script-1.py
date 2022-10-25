# import requests
import pip._vendor.requests


name = input("your name =")
print("your name is", name)
print("hi iamz zai  my anme is zain")
print("new code sihere and ready for comit")
r = pip._vendor.requests.get("https://metaasolution.com")
print(r.status_code)
