import songhay.utilities.re as re

def getSeriesPlot(soup):
    div = soup.select_one('div#translations > div[data-language="eng"]')

    return div.p.string.strip()

def getSeriesTitle(soup):
    h1 = soup.select_one('h1#series_title')

    return h1.string.strip()

def yieldSeriesBasicInfo(soup):
    li_elements = soup.select('div#series_basic_info > ul > li')
    for li in li_elements:
        key = li.select_one('strong').string.strip()
        values = [span.string.strip() for span in li.select('span')]

        yield (key, values)

def yieldSeriesActors(soup):
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
