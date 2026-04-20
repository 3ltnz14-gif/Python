class india():
    def capital(self):
        return "Delhi"
    def language(self):
        return "Hindi"
    def type(self):
        return "Parliamentary"

class america():
    def capital(self):
        return "Washington D.C"
    def language(self):
        return "American English"
    def type(self):
        return "Federal Republic"
    
ind = india()
usa = america()

for country in (ind, usa):
    print(country.capital())
    print(country.language())
    print(country.type())