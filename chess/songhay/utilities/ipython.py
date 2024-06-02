from IPython import display

def display_html_from_list(htmlList: "list[str]"):
    '''
        Uses IPython.display.HTML to display a list of HTML strings.

        This is useful for folks who do not see the usefulness
        of approaches based on HBox (see “The VBox and HBox helpers”
        [https://ipywidgets.readthedocs.io/en/7.6.3/examples/Widget%20Styling.html#The-VBox-and-HBox-helpers]).
    '''

    html = list()
    for htmlFragment in htmlList:
        html.append(htmlFragment)

    return display.HTML(''.join(html))
