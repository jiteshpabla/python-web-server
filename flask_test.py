from flask import Flask
from flask import Response, request
flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        '''<!DOCTYPE html>
<html lang="en">
 
<head>
    <title>Python Flask Bucket List App</title>
 
 
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
 
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
 
 
</head>
 
<body>
 
    <div class="container">
        <div class="header">
            <nav>
                <ul class="nav nav-pills pull-right">
                    <li role="presentation" class="active"><a href="#">Home</a>
                    </li>
                    <li role="presentation"><a href="#">Sign In</a>
                    </li>
                    <li role="presentation"><a href="showsignup">Sign Up</a>
                    </li>
                </ul>
            </nav>
            <h3 class="text-muted">Python Flask App</h3>
        </div>
 
        <div class="jumbotron">
            <h1>Bucket List App</h1>
            <p class="lead"></p>
            <p><a class="btn btn-lg btn-success" href="showsignup" role="button">Sign up today</a>
            </p>
        </div>
 
        <div class="row marketing">
            <div class="col-lg-6">
                <h4>Bucket List</h4>
                <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>
 
                <h4>Bucket List</h4>
                <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>
 
                <h4>Bucket List</h4>
                <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
            </div>
 
            <div class="col-lg-6">
                <h4>Bucket List</h4>
                <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>
 
                <h4>Bucket List</h4>
                <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>
 
                <h4>Bucket List</h4>
                <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
            </div>
        </div>
 
        <footer class="footer">
            <p>&copy; Company 2015</p>
        </footer>
 
    </div>
</body>
 
</html>''',
        mimetype='text/html'
    )

@flask_app.route('/showsignup')
def showsignup():
    return Response(
        '''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Python Flask Bucket List App</title>
 
    
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
 
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
    <link href="../static/signup.css" rel="stylesheet">
    
  </head>
 
  <body>
 
    <div class="container">
      <div class="header">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" ><a href="main">Home</a></li>
            <li role="presentation"><a href="#">Sign In</a></li>
            <li role="presentation" class="active"><a href="#">Sign Up</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">Python Flask App</h3>
      </div>
 
      <div class="jumbotron">
        <h1>Bucket List App</h1>
        <form class="form-signin" action="/signup" method="GET">
        <label for="inputName" class="sr-only">Name</label>
        <input type="name" name="inputName" id="inputName" class="form-control" placeholder="Name" required autofocus>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input type="email" name="inputEmail" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input type="password" name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required>


        <!---<p><a class="btn btn-lg btn-success" href="signup" role="button">Sign up!!!!</a>
            </p>-->

         
        <input id="btnSignUp" class="btn btn-lg btn-primary btn-block" type="submit">
      </form>
      </div>
 
       
 
      <footer class="footer">
        <p>&copy; Company 2015</p>
      </footer>
 
    </div>
  </body>
</html>''',
        mimetype='text/html'
    )



@flask_app.route('/signup',methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':
      print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
 
    # read the posted values from the UI

    print request
    '''
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    
    print _name, _email, _password
    '''

    _name = request.args.get('inputName', '')
    _email = request.args.get('inputEmail', '')
    _password = request.args.get('inputPassword', '')

    print "naaame:", _name

    file = open("datafile.txt", "a+")
    file.write(_name+" "+_email+" "+_password+"\n\n")

    return Response('''<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Python Flask Bucket List App</title>
 
    
    <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
 
    <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
    <link href="../static/signup.css" rel="stylesheet">
    
  </head>
 
  <body>
 
    <div class="container">
      <div class="header">
        <nav>
          <ul class="nav nav-pills pull-right">
            <li role="presentation" ><a href="main">Home</a></li>
            <li role="presentation"><a href="#">Sign In</a></li>
            <li role="presentation" class="active"><a href="#">Sign Up</a></li>
          </ul>
        </nav>
        <h3 class="text-muted">Python Flask App</h3>
      </div>
 
      <div class="jumbotron">
        <h1>Bucket List App</h1>
        <h3>Your data has been recorded!</h3>

      </div>
 
       
 
      <footer class="footer">
        <p>&copy; Company 2015</p>
      </footer>
 
    </div>
  </body>
</html>''', mimetype='text/html')



app = flask_app.wsgi_app