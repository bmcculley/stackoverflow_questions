# Question 35804751

[This question](http://stackoverflow.com/q/35804751/1585957) was about using Python Selenium to grab dynamically loaded content. I put this together as an example/proof of concept to show that it is possible. There are a few different ways of do this. This one by default is very simple, since I hard coded to have jQuery load more content at 15 seconds I hard coded the python script to sleep 18 seconds and then grab the page source again. In the real world things don't work this way, so more error handling and a better way of detecting dynamic content would be necessary.

### Running

To run this example, you'll need python installed on  your system.

It also requires Python Selenium ([Installation directions can be found here.](http://selenium-python.readthedocs.org/installation.html))

If you haven't already, download the source found here.

Navigate into the html directory and start a simple http server instance

`python -m SimpleHTTPServer`

Open http://localhost:8000 to make sure that it's working.

In a separate terminal window, navigate to the base directory of this question where `example.py` is located and run it `python example.py`

It will print the page source twice, once before the new content is loaded and once after.