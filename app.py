
from flask import Flask,render_template,jsonify
app=Flask(__name__)


JOBS=[ {"id":"1",
        "title":"Data Analyst",
        "location":"Bengaluru,India",
        "salary":"Rs. 10,00,000"},
     
       {"id":"2",
         "title":"Data Scintist",
         "location":"Pune, India",
         "salary":"Rs. 15,00,000"},

       {"id":"3",
        "title":"Software Engineer",
        "location":"London, UK",
        "salary":"$ 1,50,000"},

       {"id":"4",
        "title":"Backend Engineer",
        "location":"Florida, USA",
        "salary":"$ 1,20,000"
        },
      {"id":"5",
        "title":"Front-End Developer",
        "location":"Mascow, RUSSIA",
        "salary":"$ 1,35,000"
        }

      ]


@app.route("/")
def greet():
  return render_template('home.html',jobs=JOBS)


@app.route("/jobs")
def show():
  return jsonify(JOBS)
  



if __name__==("__main__"):
   app.run(host="0.0.0.0",debug=True)
