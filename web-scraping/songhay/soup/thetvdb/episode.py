from datetime import datetime
import songhay.utilities.soup as bs

def getEpisodeData(uriPath):
    soup = bs.getSoup(f'https://www.thetvdb.com{uriPath}')
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