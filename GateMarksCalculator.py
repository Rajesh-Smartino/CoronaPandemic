import pandas as pd

link = "https://cdn.digialm.com//per/g01/pub/585/touchstone/AssessmentQPHTMLMode1//GATE1965/GATE1965S4D2886/15814214030628319/EC20S47318135_GATE1965S4D2886E1.html"
initFile = pd.read_html(link)
dfFile = pd.DataFrame(initFile)
print(initFile)
dfFile = dfFile.dropna()
CSVFile = dfFile.to_csv("demo.csv")

