import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

def az_search(title, artist):
    API.artist = artist
    API.title = title

    API.getLyrics(save=True, ext='lrc')
    return API.lyrics