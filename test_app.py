from pink_morsel_visualizer import app

# Test header exists
def test_header_present(dash_duo):

    dash_duo.start_server(app)

    header = dash_duo.find_element("#dashboard-header")

    assert header.text == "Soul Foods Pink Morsel Sales Dashboard"


# Test graph exists
def test_graph_present(dash_duo):

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")

    assert graph is not None


# Test region picker exists
def test_region_picker_present(dash_duo):

    dash_duo.start_server(app)

    picker = dash_duo.find_element("#region-picker")

    assert picker is not None