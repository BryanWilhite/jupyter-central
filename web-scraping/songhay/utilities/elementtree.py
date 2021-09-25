import songhay.utilities.re as re
import xml.etree.ElementTree as ET

def getEpisodeDetailsXmlTree(titleValue, plotValue):
    episodedetails = ET.Element('episodedetails')
    title = ET.SubElement(episodedetails, 'title')
    title.text = titleValue
    plot = ET.SubElement(episodedetails, 'plot')
    plot.text = plotValue

    return ET.ElementTree(episodedetails)

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
    sorttitle.text = re.getSortTitle(str(seriesData['title']))
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
