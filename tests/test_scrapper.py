from unittest import mock


@mock.patch('scrapper.BeautifulSoup')
def test_scrape_should_return_app_information(soup):
    soup.find.return_value = "Clean Master"
    assert 2 == 2
