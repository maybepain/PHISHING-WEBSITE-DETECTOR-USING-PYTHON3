import mechine

def extracter(url):
    urllength=len(url)
    validurl=1 if "." in url else 0
    atsymbol=1 if "@" in url else 0
    sensitive= sum(word in url for word in ["login","secure","bank"])
    pathlength=len(url.split("/")) - 3
    ishttps=1 if "https" in url else 0
    dotcount=url.count(".")
    hyphencount=url.count("-")
    andcount=url.count("and")
    orcount=url.count("or")
    wwwcount=url.count("www")
    comcount=url.count("com")
    underscorecount=url.count("_")





    return urllength,validurl,sensitive,pathlength,atsymbol,ishttps,dotcount,hyphencount,andcount,orcount,wwwcount,comcount,underscorecount


user="https://www.banklogin.com"
checking=extracter(user)
df_input = mechine.pd.DataFrame([checking], columns=mechine.x.columns)
result=mechine.model.predict(df_input)

if result[0]==0:
    print("SAFE")
else:
    print("NOT SAFE")