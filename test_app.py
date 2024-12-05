import pytest
from dash.testing.application_runners import import_app
import chromedriver_autoinstaller

# Automatically install the appropriate chromedriver
chromedriver_autoinstaller.install()

@pytest.fixture
def app_runner():
    return import_app('dash_app2')

def test_header_is_present(app_runner, dash_duo):
    dash_duo.start_server(app_runner)
    header = dash_duo.find_element("h1").text
    assert "Soul Foods Pink Morsel Sales Visualizer" in header

def test_region_picker_is_present(app_runner, dash_duo):
    dash_duo.start_server(app_runner)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker.is_displayed()

def test_visualization_is_present(app_runner, dash_duo):
    dash_duo.start_server(app_runner)
    chart = dash_duo.find_element("#sales-line-chart")
    assert chart.is_displayed()
