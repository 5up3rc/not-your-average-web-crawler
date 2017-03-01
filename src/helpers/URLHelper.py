# MIT License
# 
# Copyright (c) 2017 Tijme Gommers
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from urllib.parse import urljoin, urlparse, parse_qsl

class URLHelper:

    @staticmethod
    def make_absolute(host, relative):
        if relative.startswith("http://") or relative.startswith("https://"):
            return relative

        parsed_host = urlparse(host)

        if relative.startswith("//"):
            return parsed_host.scheme + ":" + relative

        return urljoin(host, relative)

    @staticmethod
    def are_urls_similar(url1, url2):
        parsed_url1 = urlparse(url1)
        parsed_url2 = urlparse(url2)

        if parsed_url1.netloc != parsed_url2.netloc:
            return False

        if parsed_url1.path != parsed_url2.path:
            return False

        dict_url1 = dict(parse_qsl(parsed_url1.query))
        dict_url2 = dict(parse_qsl(parsed_url2.query))

        return dict_url1.keys() == dict_url2.keys()