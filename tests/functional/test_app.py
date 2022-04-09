detail_page_html = """
<head>
    <meta charset="UTF-8">
    <title>App Detail</title>
</head>
<body>
<h3>Name</h3>
<p>Lord</p>

<h3>Version</h3>
<p>2.1.1</p>

<h3>Release Date</h3>
<p>2020.01.02</p>

<h3>Number of Downloads</h3>
<p>7M Downloads</p>

<h3>Description</h3>
<p>Game app</p>
</body>
</html>
"""


def test_should_display_landing_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Welcome to Aptoide Crawler</h1>" in response.data


def test_should_display_detail_screen(client):
    response = client.post('/search', data={'url': 'https://lords-mobile.en.aptoide.com/app'})
    assert response.status_code == 200
    assert b"<title>App Detail</title>" in response.data
