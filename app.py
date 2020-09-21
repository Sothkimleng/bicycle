from bottle import route, run

@route('/')
def main():
    return "Hellow world"

run(host="localhost", port=9000, debug=True, reloader=True)
