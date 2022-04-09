from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup

from app_info import AppInformation


@pytest.fixture
def app_info():
    return AppInformation(name="Lords Mobile",
                          release_date="2021-02-10",
                          version="2.1.0",
                          download="2M Downloads",
                          description="Gaming application")


@pytest.fixture
def beautiful_soup():
    return Mock(BeautifulSoup)


@pytest.fixture()
def app():
    from app import app
    app.config.update({
        "TESTING": True,
        "SECRET_KEY": "TEST"
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
