from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [{
  'id': 1,
  'title': 'Ayurveda Consultation - INPERSON',
  'location': 'In-person',
  'price': '$120/hour'
}, {
  'id': 2,
  'title': 'FOLLOW-UP:Ayurveda Consultation INPERSON',
  'location': 'In-person',
  'price': '3 months: $75, 3-6 months: $90'
}, {
  'id': 3,
  'title': 'Ayurveda Consultation - ONLINE',
  'location': 'VIRTUAL ONLINE',
  'price': '$120/hour'
}, {
  'id': 4,
  'title': 'FOLLOW-UP:Ayurveda Consultation ONLINE',
  'location': 'VIRTUAL ONLINE',
  'price': '$75/30 minutes'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', services=SERVICES)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
