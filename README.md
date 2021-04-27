# Getting To Philosophy

`getting_to_philosophy.py` is a python script that fetches a wikipedia page and follows the first link in the main text until you reach the page for Philosophy. The script prints out the path taken to get to the Philosophy page as well as the total number of hops.

Find more information about “Getting to Philosophy” at http://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy

### Getting Started

Requirements:
 - python 3 or later
 - `beautifulsoup`
 - `requests`

Run `pip install -r requirements.txt` to download all required python libraries.

### Running the script

Run the script with the following command:

`python getting_to_philosophy.py STARTING_LINK`

where `STARTING_LINK` has the form `"https://en.wikipedia.org/wiki/Epistemology"`

### Testing

Run the unit tests with the following command:

`python test_getting_to_philosophy.py`

#### Assumptions
- Do not hop to URLs within brackets or parentheses.
- Do not hop to URLs that are italicized. 

#### Sources

https://www.w3schools.com/python/ref_requests_get.asp
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
https://stackoverflow.com/questions/49251344/python-requests-and-beautifulsoup4-gethref-returning-absolute-address-when
https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
https://stackoverflow.com/questions/24134343/suppress-print-output-in-unittests
https://www.tutorialspoint.com/unittest_framework/unittest_framework_quick_guide.htm
