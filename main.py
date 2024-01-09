import requests
json={"app_client_id":"7760676789310629","app_secret":"RWHREDMVWJDHYFZO0CM83MHF","secret_key":"B9PT47e2j3JGwsswHAzHaU5ssyzoqHsIYFHLjtZYQhlqV8U7eIkF5VIYluyrGwugVv7g1dWRcbSnoCzk10gq961GdzfpUD7INYZiS0wR8K1lrbVwkMjvqi"}
url = 'https://online.sbis.ru/oauth/service/'
response = requests.post(url, json=json)
response.encoding = 'utf-8'
print(response.text)