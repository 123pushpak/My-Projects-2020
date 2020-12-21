import phonenumbers
from test import phonenumber
from phonenumbers import geocoder
ch_num = phonenumbers.parse(phonenumber,"CH")
print(geocoder.description_for_number(ch_num,"en"))
from phonenumbers import carrier
service_number = phonenumbers.parse(phonenumber,"RO")
print(carrier.name_for_number(service_number, "en"))
