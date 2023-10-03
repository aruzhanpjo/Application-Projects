
import requests

#getting HTTPS request from a wesbite
data = requests.get("http://thisisasite.net/")



#code: will retrieve url of a website
data.url


"""
to retrieve status code of a website:

100-199 - info codes; 
200-299 - success codes;
300-399 - redirect codes;
400-499 - client error codes;
500-599 - server error codes;
"""
data.status_code

#retrieve headers of a website
data.headers

#retrieve content of a website in bytes for a machine readable format (starts with b)
data.content

#retrieve content of a website in unicode for a human readable format (no b)
data.text




from bs4 import BeautifulSoup
#brining in HTML code with beautiful soup
soup = BeautifulSoup(data.text)
#print(soup.prettify())

#find first matching tag
soup.find("title")

#find all matching tags
soup.find_all("title")

#find business number
print(soup.find("span", class_ = "phone").text)

#find all feautured testimonials
feautred_testimonial = soup.find_all("div", class_ = "quote")
for x in feautred_testimonial:
    print(x.text)
    
    
#finding all staff members
staff = soup.find_all("div", class_ = "info col-xs-8 col-xs-offset-2 col-sm-7 col-sm-offset-0 col-md-6 col-lg-8")
for s in staff:
    print(s.text)


#finding all links on the website. pound sign (#) means it is a link to the same page we pulled url from
links = soup.find_all("a") 
for l in links:
    print(l.text, l.get("href"))

#export HTML code into a text file
with open("wisdomVet.txt", "w") as f:
    f.write(soup.prettify())