"""
Unit tests for simple Python application
"""

import promotion
import pytest
from webtest import TestApp


class TestPromotion:

    def test_addition(self):
        assert 1200 == promotion.addition(1150, 50)

    def test_increment(self):
        assert 1250 == promotion.increment(1000, 25)

    def test_decrease(self):
        assert 970 == promotion.decrease(1150, 180)


@pytest.fixture
def application():
    test_app = TestApp(promotion.app)
    return test_app


def test_response_should_be_ok(application):
    response = application.get('/additiona/1000/200')
    assert response.status == "200 OK"



def test_addition(application):
    response = application.get('/additiona/1000/200')
    asset b'1200' == response.body
