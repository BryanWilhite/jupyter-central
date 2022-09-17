import songhay.utilities.re as re
import songhay.utilities.soup as bs

def getSeriesPlot(soup):
    div = soup.select_one('div#translations > div[data-language="eng"]')

    return div.p.string.strip()

def getSeriesTitle(soup):
    h1 = soup.select_one('h1#series_title')

    return h1.string.strip().replace(':', ' -')

def yieldSeriesBasicInfo(soup):
    li_elements = soup.select('div#series_basic_info > ul > li')
    for li in li_elements:
        key = li.select_one('strong').string.strip()
        values = [span.string.strip() for span in li.select('span') if not span.string is None]

        yield (key, values)

def yieldSeriesActors(soup):
    h2 = soup.select_one('h2')
    div = h2.find_next_sibling('div')
    return yieldSeriesActorsFromElementChildren(div)

def yieldSeriesActorsFromElementChildren(parentElement):
    a_elements = parentElement.select('a')
    for a in a_elements:
        values = list(a.select_one('div > h3').stripped_strings)

        values[1] = re.trimStart('as ', str(values[1]))

        img = a.select_one('img')

        img_key = 'src'
        if not 'src' in img.attrs.keys():
            img_key = 'data-src'

        if len(values) > 2:
            values[2] = img[img_key]
        else:
            values.append(img[img_key])

        yield {
            'name': values[0],
            'role': values[1],
            'src': values[2]
        }

def yieldSeriesActorsFromSeparatePage(uriPath):
    soup = bs.getSoup(f'https://www.thetvdb.com{uriPath}')
    div = soup.select_one('div.row.thumbnail-mousey')
    return yieldSeriesActorsFromElementChildren(div)
