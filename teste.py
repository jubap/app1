import requests


resp = requests.get('http://bkapp.devedp.com.br:6080/hom/v2/catalog/api/catalog/product/get?BkNumber=22121&productId=d6210f1a-e48b-4f41-a774-486fa7ed68f9')
if resp.status_code != 200:
    raise print ('GET /tasks/ {}'.format(resp.status_code))
print ('inicio do loop')
ret = resp.json()
ret2 = ret['data']
for value in ret2.values():
    print(value )  
