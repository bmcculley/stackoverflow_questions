# Question 35736910

[This question](http://stackoverflow.com/q/35736910/1585957) was about using Python3 and Selenium to grab page content. After that they needed a way to grab data from a specific column in a table. The question was about a banking site, so the actual markup of the page may be different but this should give a pretty good example of how to handle getting the necessary data by passing the page source to Beautiful Soup and then parsing it out.

### Running

To run this example, you'll need python installed on  your system.

It also requires:
 * Python Selenium ([Installation directions can be found here.](http://selenium-python.readthedocs.org/installation.html))
 * [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

If you would like to run the `build_page.py` script you'll also need to install [Jinja2](http://jinja.pocoo.org/docs/dev/).

If you haven't already, download the source [found here](https://github.com/bmcculley/stackoverflow_questions).

Navigate to the base directory of this repository and start a simple http server instance

`python -m SimpleHTTPServer`

Open http://localhost:8000/35736910/html/ to make sure that it's working.

In a separate terminal window, navigate to the base directory of this question where `example.py` is located and run it `python example.py`

It will parse and print out the desired data from the all the rows.