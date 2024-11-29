from dotenv import load_dotenv
import http.client, urllib.parse, os, json, requests
from datetime import date, timedelta

load_dotenv()

# Get UF News Data
def get_uf_news_data():
    tmw = (date.today() + timedelta(days=1)).strftime('%Y%m%d')
    url = f'https://ufl.lwcal.com/live/calendar/view/day/date/{tmw}?user_tz=America%2FDetroit&template_vars=id,latitude,longitude,location,time,href,image_raw,title_link,summary,until,is_canceled,is_online,image_src,repeats,is_multi_day,is_first_multi_day,multi_day_span,tag_classes,category_classes,has_map&syntax=%3Cwidget%20type%3D%22events_calendar%22%3E%3Carg%20id%3D%22mini_cal_heat_map%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22thumb_width%22%3E200%3C%2Farg%3E%3Carg%20id%3D%22thumb_height%22%3E200%3C%2Farg%3E%3Carg%20id%3D%22hide_repeats%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_groups%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_locations%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_tags%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22use_tag_classes%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22exclude_group%22%3EAdmin%3C%2Farg%3E%3Carg%20id%3D%22exclude_tag%22%3Eclosed%20event%3C%2Farg%3E%3C%2Fwidget%3E'

    response = requests.get(url)
    events = response.json().get('events', [])
    return events

# Get News Data
def get_news_data():
    news_conn = http.client.HTTPConnection('api.mediastack.com')
    news_params = urllib.parse.urlencode({
        'access_key': os.getenv('MEDIASTACK_API_KEY'),
        'countries': 'us',
        'categories': 'general',
        'sort': 'published_desc',
        'languages': 'en',
        'limit': 10,
        })
    news_conn.request('GET', '/v1/news?{}'.format(news_params))
    news_result = news_conn.getresponse()
    news_data = news_result.read()
    return news_data

# Get Stock Data
def get_stock_data():
    today = str(date.today())
    if date(int(today[0:3]), int(today[5:6]), int(today[8:9])).weekday() < 4:
        stock_conn = http.client.HTTPConnection("api.marketstack.com")
        stock_params = urllib.parse.urlencode({
            'access_key': os.getenv('MARKETSTACK_API_KEY'),
            'symbols': 'VTI',
            'date_from': f'{today}',
            'date_to': f'{today}',
            })
        stock_conn.request('GET', '/v1/eod?{}'.format(stock_params))
        stock_result = stock_conn.getresponse()
        stock_data = stock_result.read()
        return stock_data
    else:
        return False

# Get Weather Data
def get_weather_data():
    weather_conn = http.client.HTTPConnection("api.weatherstack.com")
    weather_params = urllib.parse.urlencode({
        'access_key': os.getenv('WEATHERSTACK_API_KEY'),
        'query': '38.8462,-77.306374',
        'units': 'f',
        })
    weather_conn.request('GET', '/v1/current?{}'.format(weather_params))
    weather_result = weather_conn.getresponse()
    weather_data = weather_result.read()
    return weather_data

def main():
    uf = get_uf_news_data()
    news = get_news_data()
    stock = get_stock_data()
    weather = get_weather_data()
    
if __name__ == '__main__':
    main()
    

