import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def getPlot(uriPath, title):
    response = requests.get(f'https://www.thetvdb.com{uriPath}')
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', { 'data-title' : title })

    return str(div.p.string).strip()

def getPlotUri(cell):
    a = cell.find('a')

    return a['href']

def getTheTVDBSoup(location):
    response = requests.get(location)
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def getTitle(cell):
    a = cell.find('a')

    return str(a.string).strip()

def getXmlTree(titleValue, plotValue):
    episodedetails = ET.Element('episodedetails')
    title = ET.SubElement(episodedetails, 'title')
    title.text = titleValue
    plot = ET.SubElement(episodedetails, 'plot')
    plot.text = plotValue

    return ET.ElementTree(episodedetails)

def yieldEpisodeData(soupTable):
    rows = soupTable.tbody.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        title = getTitle(cells[1])
        plotUri = getPlotUri(cells[1])
        plot = getPlot(plotUri, title)

        yield {
            'episode' : str(cells[0].string).strip(),
            'title': title,
            'plotUri': plotUri,
            'plot': plot
        }

def writeXml(locationTemplate, fileName, xmlTree):
    fileName = f'{locationTemplate} {fileName}.nfo'
    xmlTree.write(fileName, encoding='utf-8')
