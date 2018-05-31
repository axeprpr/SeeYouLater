from bottle import *
from nanorm import *
import json,uuid

##### DATABASE ####
set_db_name("nanorm.db")
auto_commit_open()

class Link(Model):
    name = CharField(64)
    url = CharField(255)
    desc = CharField(255)


class Auth(Model):
    user = CharField(64)
    password = CharField(64)


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

##### LINK AREA ####
@get('/link')
def list_link():
    links = Link.query().all()
    return json.dumps([ {"name": link.name, "url": link.url, "desc": link.desc} for link in links ])

@post('/link')
def add_link():
    link_obj = Link()
    try:
        link_obj.name = request.forms.get('name')
        link_obj.url = request.forms.get('url')
        link_obj.desc = request.forms.get('desc')
        link_obj.save() 
    except:
        pass

@error(404)
def error404(error):
    return '<h1>Nothing here.</h1>'

@post('/auth/')
def password(action):
    pass

@delete('/link/<link_id>')
def delete_link():
    pass

@route('/')
@route('/<filename>')
def server_static(filename="index.html"):
    return static_file(filename, root='./')

run(host='0.0.0.0',port=8080)