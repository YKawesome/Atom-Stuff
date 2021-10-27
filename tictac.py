import http.client

conn = http.client.HTTPSConnection("stujo-tic-tac-toe-stujo-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c6b3a8746emsh2cb9c94890c14e4p12e129jsn014c66feb6b2",
    'x-rapidapi-host': "stujo-tic-tac-toe-stujo-v1.p.rapidapi.com"
    }

conn.request("GET", "/----X----/X", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
