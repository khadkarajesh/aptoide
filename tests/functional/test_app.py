def test_should_display_landing_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Welcome to Aptoide Crawler</h1>" in response.data


def test_should_display_detail_screen(client):
    response = client.post('/search', data={'url': 'https://lords-mobile.en.aptoide.com/app'})
    assert response.status_code == 200
    assert b"<title>App Detail</title>" in response.data
