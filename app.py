from flask import Flask, render_template, jsonify

app = Flask(__name__)

Books = [
  {
    'id' : 1,
    'title' : 'Python - The complete reference',
    'author' : 'Martin C.Brown',
    'year' : '2018',
  },
{
  'id' : 2,
  'title' :'Core Java - An integrated uproach',
  'author' : 'Dr. R. Nageswara Rao',
  'year' : '2016',
},
{
  'id' : 3,
  'title' :' Object oriented programming with C++',
  'author' :'E Balaguruswamy',
  'year' :'2020',
},
{
  'id' : 4,
  'title' : 'SQL- The Ultimate beginners guide ',
  'author' :'Brandon Cooper',
  'year' :'2019',
}
]


@app.route("/")
def hello():
  return render_template('home.html', books=Books)
  
@app.route("/api/books")
def list_books():
  return jsonify(Books)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
