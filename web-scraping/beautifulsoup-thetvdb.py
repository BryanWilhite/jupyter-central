from os import name
import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from datetime import datetime

def getEpisodeDetailsXmlTree(titleValue, plotValue):
    episodedetails = ET.Element('episodedetails')
    title = ET.SubElement(episodedetails, 'title')
    title.text = titleValue
    plot = ET.SubElement(episodedetails, 'plot')
    plot.text = plotValue

    return ET.ElementTree(episodedetails)

def getEpisodePlot(uriPath, title):
    response = requests.get(f'https://www.thetvdb.com{uriPath}')
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', { 'data-title' : title })

    return str(div.p.string).strip()

def getEpisodePlotUri(cell):
    a = cell.find('a')

    return a['href']

def getEpisodeTitle(cell):
    a = cell.find('a')

    return a.string.strip()

def getEpisodeYear(cell):
    div = cell.select_one('div')
    date = datetime.strptime(div.string, '%B %d, %Y')

    return str(date.year)

def getSeriesPlot(soup):
    div = soup.select_one('div#translations > div[data-language="eng"]')

    return div.p.string.strip()

def getSeriesTitle(soup):
    h1 = soup.select_one('h1#series_title')

    return h1.string.strip()

def getSoup(location):
    response = requests.get(location)
    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def getTVShowXmlTree(seriesData):
    tvshow = ET.Element('tvshow')
    for item in seriesData['uniqueids']:
        type = item['type']
        attrib = dict(
            type=type,
            default=str(type == 'imdb').lower()
        )
        uniqueid = ET.SubElement(tvshow, 'uniqueid', attrib=attrib)
        uniqueid.text = item['uniqueid']
    title = ET.SubElement(tvshow, 'title')
    title.text = seriesData['title']
    sorttitle = ET.SubElement(tvshow, 'sorttitle')
    sorttitle.text = re.sub('^[Tt]he ', '', str(seriesData['title']))
    plot = ET.SubElement(tvshow, 'plot')
    plot.text = seriesData['plot']
    # thumb elements:
    for item in [i for i in seriesData['thumbs'] if i['aspect'] != 'fanart']:
        attrib = dict(aspect=item['aspect'])
        season_key = 'season'
        season = item[season_key]
        if(season != None):
            attrib['type'] = season_key
            attrib[season_key] = str(season)
        thumb = ET.SubElement(tvshow, 'thumb', attrib=attrib)
        thumb.text = item['src']
    # fanart element:
    fanart = ET.SubElement(tvshow, 'fanart')
    for item in [i for i in seriesData['thumbs'] if i['aspect'] == 'fanart']:
        attrib = dict(dim=item['dim'])
        thumb = ET.SubElement(fanart, 'thumb', attrib=attrib)
        thumb.text = item['src']
    # genre elements:
    for g in seriesData['genres']:
        genre = ET.SubElement(tvshow, 'genre')
        genre.text = g
    # actor elements:
    for a in seriesData['actors']:
        actor = ET.SubElement(tvshow, 'actor')
        key = 'name'
        name = ET.SubElement(actor, key)
        name.text = a[key]
        key = 'role'
        role = ET.SubElement(actor, key)
        role.text = a[key]
        thumb = ET.SubElement(actor, 'thumb')
        thumb.text = a['src']

    return ET.ElementTree(tvshow)

def yieldEpisodeData(soupTable):
    rows = soupTable.tbody.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        title = getEpisodeTitle(cells[1])
        plotUri = getEpisodePlotUri(cells[1])
        plot = getEpisodePlot(plotUri, title)
        year = getEpisodeYear(cells[2])

        yield {
            'episode' : str(cells[0].string).strip(),
            'title': title,
            'plotUri': plotUri,
            'plot': plot,
            'year': year
        }

def yieldSeriesBasicInfo(soup):
    li_elements = soup.select('div#series_basic_info > ul > li')
    for li in li_elements:
        key = li.select_one('strong').string.strip()
        values = [span.string.strip() for span in li.select('span')]

        yield (key, values)

def yieldTVShowActors(soup):
    h2 = soup.select_one('h2')
    div = h2.find_next_sibling('div')
    a_elements = div.select('a')
    for a in a_elements:
        values = list(a.select_one('div > h3').stripped_strings)
        img = a.select_one('img')
        values.append(img['src'])
        values[1] = re.sub('^as ', '', str(values[1]))

        yield {
            'name': values[0],
            'role': values[1],
            'src': values[2]
        }

def writeEpisodeDetailsXml(locationTemplate, episode, year, xmlTree):
    fileName = f'{locationTemplate} ({year}) {episode}.nfo'
    xmlTree.write(fileName, encoding='utf-8', xml_declaration=True)
