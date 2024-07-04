# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.surplus_forecast_api import SurplusForecastApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSurplusForecastApi(unittest.TestCase):
    """SurplusForecastApi unit test stubs"""

    def setUp(self):
        self.api = SurplusForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast_surplus_daily_evolution_get(self):
        """Test case for forecast_surplus_daily_evolution_get

        Evolution daily surplus forecast (OCNMFD)  # noqa: E501
        """
        pass

    def test_forecast_surplus_daily_get(self):
        """Test case for forecast_surplus_daily_get

        Daily surplus forecast (OCNMFD)  # noqa: E501
        """
        pass

    def test_forecast_surplus_daily_history_get(self):
        """Test case for forecast_surplus_daily_history_get

        Historical daily surplus forecast (OCNMFD)  # noqa: E501
        """
        pass

    def test_forecast_surplus_weekly_evolution_get(self):
        """Test case for forecast_surplus_weekly_evolution_get

        Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)  # noqa: E501
        """
        pass

    def test_forecast_surplus_weekly_get(self):
        """Test case for forecast_surplus_weekly_get

        Weekly surplus forecast (OCNMFW, OCNMF3Y)  # noqa: E501
        """
        pass

    def test_forecast_surplus_weekly_history_get(self):
        """Test case for forecast_surplus_weekly_history_get

        Historical weekly surplus forecast (OCNMFW, OCNMF3Y)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
