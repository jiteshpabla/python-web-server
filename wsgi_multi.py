# Made by Jitesh, Vaibhav and Priyam for - OSSP Lab, JIIT; April-May 2017

import socket
import StringIO
import sys

import os
import time

#from cgi import parse_qs, escape


stop_server = False


class WSGIServer(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1


    def __init__(self, server_address):
        # Create a listening socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        # Allow to reuse the same address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Activate
        listen_socket.listen(self.request_queue_size)
        # Get server host name and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by Web framework/Web application
        self.headers_set = []


    def set_app(self, application):
        self.application = application


    def serve_forever(self):
        listen_socket = self.listen_socket
        print('Parent PID (PPID): {pid}\n'.format(pid=os.getpid()))

        while True:

            if stop_server == True:
                break

            self.client_connection, client_address = listen_socket.accept()

            #forking into child and parent processes
            pid1 = os.fork()
            
            if pid1 == 0:  # child
                #print "aaaaaaaa", pid1, "aaaaaaa"
                listen_socket.close()  # close child copy
                self.handle_one_request()
                #self.client_connection.close()
                print ("child {pid} exits".format(pid=os.getpid()))
                os._exit(0)  # child exits here

            elif pid1!= 0:  # parent
                print "parent process continues"
                self.client_connection.close()  # close parent copy and loop over

        '''
        while True:
            # New client connection
            self.client_connection, client_address = listen_socket.accept()
            # Handle one request and close the client connection. Then
            # loop over to wait for another client connection
            self.handle_one_request()
        '''


    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        #print request_data


        print(
            'Child PID: {pid}. Parent PID {ppid}'.format(
                pid=os.getpid(),
                ppid=os.getppid(),
            )
        )

        # Print formatted request data a la 'curl -v'
        '''
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))
        '''

        self.parse_request(request_data)

        # Construct environment dictionary using request data
        env = self.get_environ()

        # calls our application callable and gets
        # back a result that will become HTTP response body
        result = self.application(env, self.start_response)

        # Construct a response and send it back to the client
        self.finish_response(result)


    def parse_request(self, text):
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line into components
        (self.request_method,  # GET
         self.path,            # /hello
         self.request_version  # HTTP/1.1
         ) = request_line.split()


    def get_environ(self):
        env = {}


        # Required WSGI variables
        env['wsgi.version']      = (1, 0)

        env['wsgi.url_scheme']   = 'http'

        env['wsgi.input']        = StringIO.StringIO(self.request_data)

        env['wsgi.errors']       = sys.stderr

        env['wsgi.multithread']  = False
        env['wsgi.multiprocess'] = True
        env['wsgi.run_once']     = False

        # Required CGI variables
        env['REQUEST_METHOD']    = self.request_method    # GET

        str1 = self.path
        flag1 = str1.find('?')

        if flag1==-1:
            env['PATH_INFO']         = self.path
        else:
            ind1 = str1.index('?')
            env['PATH_INFO']         = str1[:ind1]        # /hello

            env['QUERY_STRING']      = str1[ind1+1:]

        env['SERVER_NAME']       = self.server_name       # localhost
        env['SERVER_PORT']       = str(self.server_port)  # 8888


        return env


    def start_response(self, status, response_headers, exc_info=None):
        # Add necessary server headers
        server_headers = [
            ('Date', 'Tue, 31 Mar 2015 12:54:48 GMT'),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]

        # return self.finish_response


    def finish_response(self, result):
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response += '\r\n'
            for data in result:
                response += data
            # Print formatted response data a la 'curl -v'
            '''
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            '''
            self.client_connection.sendall(response)
        finally:
            
            self.client_connection.close()
            time.sleep(15)



def make_server(server_address, application):
    server = WSGIServer(server_address)
    server.set_app(application)
    return server


def main_fn(app_name, port_name):
    slash_index = app_name.rfind('/')
    app_name = app_name[slash_index+1:]
    app_path = app_name[:-3]+":app"
    '''
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    '''
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(('', port_name), application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=port_name))
    httpd.serve_forever()


def stop_server_fn():
    global stop_server
    stop_server = True


#SERVER_ADDRESS = (HOST, PORT) = '', 8888


if __name__ == '__main__':
    SERVER_ADDRESS = (HOST, PORT) = '', 8888
    if len(sys.argv) < 2:
        sys.exit('Provide a WSGI application object as module:callable')
    app_path = sys.argv[1]
    module, application = app_path.split(':')
    module = __import__(module)
    application = getattr(module, application)
    httpd = make_server(SERVER_ADDRESS, application)
    print('WSGIServer: Serving HTTP on port {port} ...\n'.format(port=PORT))
    httpd.serve_forever()