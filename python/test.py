import sys
import datetime

def application(environ,start_response):
        status = '200 OK'
        lines = [
                '<html>',
                '       <body>',
                '               <title>Test-wsgi page forfys</title>',
                '               <div style="width: 100%; font-size:40px;',
                '               font-weight: bold; text-align:center;">',
                '               Welcome to mod_wsgi TestPage','<br>Python:{pv:s}',
                '               <br>Date:{ts:s}',
                '       </div>',
                '       </body>',
                '</html>']
        html= '\n'.join(lines).format(pv=str(sys.version_info),
                                                                ts=str(datetime.datetime.now()),)
        response_header = [('Content-type','text/html')]
        start_response(status,response_header)
        return [bytes(html, 'utf-8')]
if __name__ == '__main__':
        application({},print)