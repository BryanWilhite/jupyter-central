import songhay.utilities.re as re
import xml.etree.ElementTree as ET

def getEpisodeDetailsXmlTree(titleValue, plotValue):
    episodedetails = ET.Element('episodedetails')
    title = ET.SubElement(episodedetails, 'title')
    title.text = titleValue
    plot = ET.SubElement(episodedetails, 'plot')
    plot.text = plotValue

    return ET.ElementTree(episodedetails)

def getMovieXmlTree(movieData):
    movie = ET.Element('movie')
    for item in movieData['uniqueids']:
        type = item['type']
        attrib = dict(
            type=type,
            default=str(type == 'imdb').lower()
        )
        uniqueid = ET.SubElement(movie, 'uniqueid', attrib=attrib)
        uniqueid.text = item['uniqueid']
    title = ET.SubElement(movie, 'title')
    title.text = movieData['title']
    sorttitle = ET.SubElement(movie, 'sorttitle')
    sorttitle.text = re.getSortTitle(str(movieData['title']))
    plot = ET.SubElement(movie, 'plot')
    plot.text = movieData['plot']
    # genre element:
    genre = ET.SubElement(movie, 'genre')
    genre.text =  movieData['genre']
    # country element:
    country = ET.SubElement(movie, 'country')
    country.text =  movieData['country']
    # director element:
    director = ET.SubElement(movie, 'director')
    director.text =  movieData['director']
    # year element:
    year = ET.SubElement(movie, 'year')
    year.text =  movieData['year']
    # actor elements:
    for a in movieData['actors']:
        actor = ET.SubElement(movie, 'actor')
        key = 'name'
        name = ET.SubElement(actor, key)
        name.text = a[key]
        key = 'role'
        role = ET.SubElement(actor, key)
        role.text = a[key]
        thumb = ET.SubElement(actor, 'thumb')
        thumb.text = a['src']

    return ET.ElementTree(movie)

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

def writeEpisodeDetailsXml(locationTemplate, episode, year, xmlTree):
    fileName = f'{locationTemplate} ({year}) {episode}.nfo'
    xmlTree.write(fileName, encoding='utf-8', xml_declaration=True)
