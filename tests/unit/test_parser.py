from unittest.mock import Mock, patch
from bs4 import PageElement

from parser import *


def test_parse_should_return_app_information(app_info, beautiful_soup):
    def get_value(tag, attrs):
        css_class_value = {
            APP_DESCRIPTION_CSS_CLASS: app_info.description,
            APP_VERSION_CSS_CLASS: app_info.version,
            APP_NUMBER_OF_DOWNLOADS_CSS_CLASS: app_info.download,
            APP_RELEASE_DATE_CSS_CLASS: app_info.release_date
        }
        element = Mock(PageElement)
        setattr(element, "text", css_class_value.get(attrs.get('class')))
        return [element]

    mock_page_element = Mock(PageElement)
    setattr(mock_page_element, "text", app_info.name)

    beautiful_soup.find.return_value = mock_page_element
    beautiful_soup.find_all.side_effect = get_value

    parsed_app_info = parse(beautiful_soup)
    assert app_info == parsed_app_info


@patch('parser.logging.error')
def test_parse_should_raise_exception(mock_log, beautiful_soup):
    beautiful_soup.find_all.return_value = []
    parse(soup=beautiful_soup)
    mock_log.assert_called()
