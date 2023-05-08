from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


@app.route('/')
@app.route('/Home')
def home():
    return render_template('check_url.html')


@app.route('/check_paywall', methods=['GET'])
def check_paywall():
    url = request.args.get('url')
    second_url = url
    second_url = 'https://12ft.io/proxy?q=' + str(url)
    print(url)
    print(second_url)
    response = requests.get(url)
    second_response = requests.get(second_url)

    soup = BeautifulSoup(response.text, 'html.parser')
    second_soup = BeautifulSoup(response.text, 'html.parser')

    first_paywall = False
    second_paywall = False

    subscribe_forms = soup.find_all('form', {'action': lambda x: x and ('subscribe' in x or 'log in' in x or 'sign in' in x)})
    subscribe_links = soup.find_all('a', {'href': lambda x: x and ('subscribe' in x or 'log in' in x or 'sign in' in x)})
    if subscribe_forms or subscribe_links:
        first_paywall = True

    subscribe_forms_2 = second_soup.find_all('form', {'action': lambda x: x and ('subscribe' in x or 'log in' in x or 'sign in' in x)})
    subscribe_links_2 = second_soup.find_all('a', {'href': lambda x: x and ('subscribe' in x or 'log in' in x or 'sign in' in x)})
    if subscribe_forms_2 or subscribe_links_2:
        second_paywall = True

    if not first_paywall:
        return "No paywall detected"
    elif first_paywall or second_paywall:
        return "Paywall was removed by 12ft.io"
    elif first_paywall and second_paywall:
        return "Paywall was detected and can't be removed by 12ft.io"


if __name__ == "__main__":
    app.run(debug=True)
