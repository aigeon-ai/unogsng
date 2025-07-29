import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/unogs/api/unogsng'

mcp = FastMCP('unogsng')

@mcp.tool()
def genres() -> dict: 
    '''Returns a list of Netflix genres'''
    url = 'https://unogsng.p.rapidapi.com/genres'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries() -> dict: 
    '''Returns list of available Netflix countries (includes uNoGS country id)'''
    url = 'https://unogsng.p.rapidapi.com/countries'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def people(netflixid: Annotated[Union[int, float, None], Field(description='A Netflix title ID Default: 70021641')] = None,
           offset: Annotated[Union[int, float, None], Field(description='Starting Number of results (Default is 0) Default: 0')] = None,
           name: Annotated[Union[str, None], Field(description='A persons name First Last or Both')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Limit of returned items default/max 100 Default: 0')] = None) -> dict: 
    '''Search for Netflix People by name (returns person id for searches)'''
    url = 'https://unogsng.p.rapidapi.com/people'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
        'offset': offset,
        'name': name,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def deleted(limit: Annotated[Union[str, None], Field(description='')] = None,
            offset: Annotated[Union[str, None], Field(description='')] = None,
            countrylist: Annotated[Union[str, None], Field(description="list of uNoGS country ID's separated by a ,")] = None,
            date: Annotated[Union[str, datetime, None], Field(description='returns anything deleted after this date')] = None,
            netflixid: Annotated[Union[str, None], Field(description='Netflix Title ID')] = None) -> dict: 
    '''Returns all title which have been deleted meeting a limited criteria'''
    url = 'https://unogsng.p.rapidapi.com/titlesdel'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
        'countrylist': countrylist,
        'date': date,
        'netflixid': netflixid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(newdate: Annotated[Union[str, datetime, None], Field(description='returns all titles with a new date greater than this')] = None,
           genrelist: Annotated[Union[str, None], Field(description="list of Netflix genre id's (see genre endpoint for list)")] = None,
           type: Annotated[Union[str, None], Field(description='movie or series')] = None,
           start_year: Annotated[Union[int, float, None], Field(description='A 4 digit year Default: 1972')] = None,
           orderby: Annotated[Union[str, None], Field(description='orderby string (date,dateDesc,rating,title,type,runtime,filmyear,filmyearDesc)')] = None,
           audiosubtitle_andor: Annotated[Union[str, None], Field(description='and/or for audio and subtitles')] = None,
           start_rating: Annotated[Union[str, None], Field(description='imdb rating 0-10')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Limit of returned items default/max 100 Default: 100')] = None,
           end_rating: Annotated[Union[int, float, None], Field(description='imdb rating 0-10 Default: 0')] = None,
           subtitle: Annotated[Union[str, None], Field(description='A valid language type')] = None,
           countrylist: Annotated[Union[str, None], Field(description="list of uNoGS country ID's (from country endpoint) leave blank for all country search")] = None,
           query: Annotated[Union[str, None], Field(description='any string you want to search (fulltext against the title)')] = None,
           audio: Annotated[Union[str, None], Field(description='A valid language type')] = None,
           country_andorunique: Annotated[Union[str, None], Field(description='')] = None,
           offset: Annotated[Union[int, float, None], Field(description='Starting Number of results (Default is 0) Default: 0')] = None,
           end_year: Annotated[Union[int, float, None], Field(description='A 4 digit year Default: 2019')] = None) -> dict: 
    '''Search for Netflix titles based on a variety of parameters'''
    url = 'https://unogsng.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'newdate': newdate,
        'genrelist': genrelist,
        'type': type,
        'start_year': start_year,
        'orderby': orderby,
        'audiosubtitle_andor': audiosubtitle_andor,
        'start_rating': start_rating,
        'limit': limit,
        'end_rating': end_rating,
        'subtitle': subtitle,
        'countrylist': countrylist,
        'query': query,
        'audio': audio,
        'country_andorunique': country_andorunique,
        'offset': offset,
        'end_year': end_year,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def images(netflixid: Annotated[Union[int, float], Field(description='Netflix Title ID Default: 81037848')],
           offset: Annotated[Union[int, float, None], Field(description='Starting Number of results (Default is 0) Default: 3')] = None,
           limit: Annotated[Union[int, float, None], Field(description='Limit of returned items default/max 100 Default: 2')] = None) -> dict: 
    '''Pull all the images associated with a particular title'''
    url = 'https://unogsng.p.rapidapi.com/images'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_countries(netflixid: Annotated[Union[int, float], Field(description='Netflix ID Default: 81043135')]) -> dict: 
    '''Get all countries associated with a particular Netflix ID'''
    url = 'https://unogsng.p.rapidapi.com/titlecountries'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_genres(netflixid: Annotated[Union[int, float], Field(description='Netflix ID Default: 81043135')]) -> dict: 
    '''Get all genres associated with a particular Netflix ID'''
    url = 'https://unogsng.p.rapidapi.com/titlegenres'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_details(netflixid: Annotated[Union[int, float, None], Field(description='A Netflix specific ID Default: 81043135')] = None,
                  imdbid: Annotated[Union[str, None], Field(description='An IMDB ID')] = None) -> dict: 
    '''Specific information for a given Netflix title'''
    url = 'https://unogsng.p.rapidapi.com/title'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
        'imdbid': imdbid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def expiring(countrylist: Annotated[str, Field(description='List of uNoGS country IDs separated by a ,')],
             offset: Annotated[Union[int, float, None], Field(description='Starting Number of results (Default is 0) Default: 0')] = None,
             limit: Annotated[Union[int, float, None], Field(description='Limit of returned items default/max 100 Default: 0')] = None) -> dict: 
    '''Get list of expiring titles'''
    url = 'https://unogsng.p.rapidapi.com/expiring'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'countrylist': countrylist,
        'offset': offset,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def episodes(netflixid: Annotated[Union[int, float, None], Field(description='A Netflix title ID Default: 70153392')] = None,
             episodeid: Annotated[Union[int, float, None], Field(description='Default: 70150654')] = None,
             seasonid: Annotated[Union[int, float, None], Field(description='Default: 70051768')] = None) -> dict: 
    '''Search for Netflix People by name (returns person id for searches)'''
    url = 'https://unogsng.p.rapidapi.com/episodes'
    headers = {'x-rapidapi-host': 'unogsng.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'netflixid': netflixid,
        'episodeid': episodeid,
        'seasonid': seasonid,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    mcp.run(transport="stdio")
