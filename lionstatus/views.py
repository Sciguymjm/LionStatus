import collections
import time
from pyramid.view import view_config
import requests
from BeautifulSoup import BeautifulSoup


@view_config(route_name='status', renderer='json')
def get_status(request):
    sites = {'Steam Community': 'http://steamcommunity.com/', 'Google': 'https://www.google.com/',
             'IFTTT': 'https://ifttt.com/', 'Reddit': 'https://www.reddit.com/', 'Twitter': 'https://twitter.com/',
             'Bazaar.TF': 'http://bazaar.tf/', 'Backpack.TF': 'http://backpack.tf/', 'Trade.TF': 'http://www.trade.tf/',
             'Ring.TF': 'http://ring.tf/', 'Facebook': 'https://www.facebook.com/',
             'Instagram': 'http://instagram.com/',
             'GCUFSD': 'http://www.gardencity.k12.ny.us/site/default.aspx?PageID=1'}
    result = {}
    for site in sites.keys():
        r = None
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"}
        try:
            r = requests.head(sites[site], timeout=5, headers=headers)
        except requests.exceptions.Timeout:
            result[site] = [site, '',
                            '', 504, 'Site Timed Out', '<i class="fa fa-circle" style="color:red"></i>']
            continue
        except:
            continue
        if r.status_code == 302 or r.status_code == 301:
            print 'FIX:' + site + ' -> ' + r.headers['Location']
        soup = BeautifulSoup(r.text)
        icon = soup.find("link", {'rel': "shortcut icon"})
        description = soup.find("meta", {"name": "description"})
        status = 'green' if r.status_code == 200 else 'red'
        title = soup.title
        result[sites[site]] = [site, r.status_code, r.reason,
                               '<i class="fa fa-circle" style="color:' + status + '"></i>',
                               r.elapsed.total_seconds() * 1000, time.strftime('%I:%M%p on %b %d, %Y')]
    return collections.OrderedDict(
        sorted(result.items(), key=lambda (k, v): (v[0], k)))  # ' 1:36PM EST on Oct 18, 2010')


@view_config(route_name='main', renderer="templates\index.mako")
def main(request):
    return {}