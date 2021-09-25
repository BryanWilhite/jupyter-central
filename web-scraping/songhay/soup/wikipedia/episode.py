from datetime import datetime
import songhay.utilities.soup as bs

def getEpisodePlot(row):
    plot = ' '.join(list(row.next_sibling.stripped_strings))

    return plot.replace(' ,', ',').replace(' .', '.').replace("\'", "'")

def getEpisodeTitle(cell):
    title = str(list(cell.stripped_strings)[0]).replace('"', '')

    return title

def getEpisodeYear(cell):
    s = (list(cell.stripped_strings)[0]).replace('\xa0', ' ')
    if(len(s) < 4):
        return ''
    date = datetime.strptime(s, '%B %d, %Y')

    return str(date.year)

def yieldEpisodeData(soupTable):
    rows = soupTable.tbody.select('tr.vevent')
    for row in rows:
        th = row.select_one('th')
        cells = row.find_all('td')
        title = getEpisodeTitle(cells[1])
        plot = getEpisodePlot(row)
        year = getEpisodeYear(cells[6])

        yield {
            'episode': th.string.strip(),
            'title': title,
            'plot': plot,
            'year': year
        }
