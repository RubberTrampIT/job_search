import requests

response = requests.get('https://www.google.com/search?q=100%25+remote+information+security+jobs+-clearance+-calls&sxsrf=AOaemvIFXudynTDUaDx-GHxpBsydosvwkA:1639247670478&source=hp&ei=Nu-0YcrhGKanqtsP3depoAE&iflsig=ALs-wAMAAAAAYbT9Rnq1NgSsuFPJUmwtHV4lsp5g1i-U&ibp=htl;jobs&sa=X&ved=2ahUKEwj255i7sdz0AhVelGoFHdz5AxAQudcGKAJ6BAgKECw')

print HttpResponse(response.text)
