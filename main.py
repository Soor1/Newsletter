from dotenv import load_dotenv
import http.client, urllib.parse, os, json, requests
from datetime import date, timedelta

load_dotenv()


# Get tomorrow's date
# tmw = (date.today() + timedelta(days=1)).strftime('%Y%m%d')

# # Construct the full URL using HTTPS
# url = f'https://ufl.lwcal.com/live/calendar/view/day/date/{tmw}?user_tz=America%2FDetroit&template_vars=id,latitude,longitude,location,time,href,image_raw,title_link,summary,until,is_canceled,is_online,image_src,repeats,is_multi_day,is_first_multi_day,multi_day_span,tag_classes,category_classes,has_map&syntax=%3Cwidget%20type%3D%22events_calendar%22%3E%3Carg%20id%3D%22mini_cal_heat_map%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22thumb_width%22%3E200%3C%2Farg%3E%3Carg%20id%3D%22thumb_height%22%3E200%3C%2Farg%3E%3Carg%20id%3D%22hide_repeats%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_groups%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_locations%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22show_tags%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22use_tag_classes%22%3Etrue%3C%2Farg%3E%3Carg%20id%3D%22exclude_group%22%3EAdmin%3C%2Farg%3E%3Carg%20id%3D%22exclude_tag%22%3Eclosed%20event%3C%2Farg%3E%3C%2Fwidget%3E'

# # Send the GET request
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     json_response = response.json()
    
#     # Assuming the events are inside the "events" key
#     events = json_response.get('events', [])
#     print(events)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")


# Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     json_response = response.json()
#     print(json_response)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")

# Get News Data
# news_conn = http.client.HTTPConnection('api.mediastack.com')
# news_params = urllib.parse.urlencode({
#     'access_key': os.getenv('MEDIASTACK_API_KEY'),
#     'countries': 'us',
#     'categories': 'general',
#     'sort': 'published_desc',
#     'languages': 'en',
#     'limit': 10,
#     })
# news_conn.request('GET', '/v1/news?{}'.format(news_params))
# news_result = news_conn.getresponse()
# news_data = news_result.read()

# Get Stock Data
stock_conn = http.client.HTTPConnection("api.marketstack.com")
weather_params = urllib.parse.urlencode({
    'access_key': os.getenv('WEATHERSTACK_API_KEY'),
    'query': '38.8462,-77.306374',
    'units': 'f',
    })
weather_conn.request('GET', '/v1/eod?{}'.format(weather_params))
weather_result = weather_conn.getresponse()
weather_data = weather_result.read()

# Get Weather Data
# weather_conn = http.client.HTTPConnection("api.weatherstack.com")
# weather_params = urllib.parse.urlencode({
#     'access_key': os.getenv('WEATHERSTACK_API_KEY'),
#     'query': '38.8462,-77.306374',
#     'units': 'f',
#     })
# weather_conn.request('GET', '/v1/current?{}'.format(weather_params))
# weather_result = weather_conn.getresponse()
# weather_data = weather_result.read()
