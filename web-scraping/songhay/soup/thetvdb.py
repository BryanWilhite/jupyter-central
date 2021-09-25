from os import name
from bs4 import BeautifulSoup
from datetime import datetime
import songhay.utilities.re as re
import songhay.utilities.requests as req

def getEpisodeData(uriPath):
    html = req.getHtml(f'https://www.thetvdb.com{uriPath}')
    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.select_one('h1.translated_title')
    div = soup.select_one('div#translations > div[data-language="eng"]')

    return {
        'title': h1.string.strip(),
        'plot': div.p.string.strip()
    }

def getEpisodeDataUri(cell):
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
    html = req.getHtml(location)
    soup = BeautifulSoup(html, 'html.parser')

    return soup

def yieldEpisodeData(soupTable):
    rows = soupTable.tbody.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        title = getEpisodeTitle(cells[1])
        year = getEpisodeYear(cells[2])
        episode_data_uri = getEpisodeDataUri(cells[1])
        episode_data = getEpisodeData(episode_data_uri)
        if(title != episode_data['title']):
            title = episode_data['title']

        yield {
            'episode' : str(cells[0].string).strip(),
            'title': title,
            'plot': episode_data['plot'],
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
        values[1] = re.trimStart('as ', str(values[1]))

        yield {
            'name': values[0],
            'role': values[1],
            'src': values[2]
        }

def writeEpisodeDetailsXml(locationTemplate, episode, year, xmlTree):
    fileName = f'{locationTemplate} ({year}) {episode}.nfo'
    xmlTree.write(fileName, encoding='utf-8', xml_declaration=True)
