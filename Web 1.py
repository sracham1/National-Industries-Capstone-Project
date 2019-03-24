from bs4 import BeautifulSoup
import requests
import mysql.connector
import re


cnx = mysql.connector.connect(user='root', password='dellxpssql', host='127.0.0.1', database='nib')
search=requests.utils.quote('markers, Sewing, Stainless Steel, 6-1/2" Length')
URL = 'https://www.google.com/search?hl=en&tbm=shop&ei=eY2KXPmPMOyx0PEP85m80As&q='+search+'+&oq='+search+'+&gs_l=psy-ab.3...93350.93350.0.93941.1.1.0.0.0.0.180.180.0j1.1.0....0...1c.1.64.psy-ab..0.0.0....0.Q1ijcKJ6qVE'
a = requests.get(URL, headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"})



soup = BeautifulSoup(a.text, 'html.parser')
divs = soup.findAll("div", { "class" : "A8OWCb" })
divs1 = soup.findAll("div", { "class" : "MCpGKc" })
convert=re.compile(r'\'')



for div,div1 in zip(divs,divs1):
    product = div1.find("a")
    price = div.find("b")  
#    print(product.text)
    product1=convert.sub('\'\'',product.text)
#    print('\n')
    cursor = cnx.cursor()
    query=("INSERT INTO commercial (product_name,price) VALUES (\'%s\',\'%s\')"%(product1,price.text[1:]))
#    print(query)
    cursor.execute(query)
    cnx.commit()
    cursor.close()

cnx.close()

