# puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]
#
# puertos_tcp.append(1337)
#
# puertos_tcp.sort() # ordena de menor a mayor
#
# print(puertos_tcp)

# attacks = ['Phishing', 'DDoS', 'SQL I', 'Man In The Middle', 'Cross-Site Scripting']
# print(attacks)
# attacks.reverse() # invierte el orden de la lista
# print(attacks)

attacks = ['Phishing', 'DDoS', 'SQL I', 'Man In The Middle', 'Cross-Site Scripting']
attacks_uppercase = [attack.upper() for attack in attacks]  # todo mayus
attacks_lowercase = [attack.lower() for attack in attacks]  # todo minus
print(attacks_uppercase)
print(attacks_lowercase)
