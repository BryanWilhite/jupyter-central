from bs4 import BeautifulSoup
import songhay.utilities.requests as req

def getSoup(location):
    html = req.getHtml(location)
    soup = BeautifulSoup(html, 'html.parser')

    return soup
