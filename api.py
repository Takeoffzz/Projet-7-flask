from flask import Flask, request, render_template

from df import recuperer_score_par_ID

app = Flask(__name__, template_folder='template')

# main API
@app.route("/score_client", methods=['POST'])
def index():
    return "<h1>API P7 DS </h1>"

@app.route("/recherche", methods=['GET', 'POST'])
def recherche():
    if request.method == "POST":
        donnes = request.form
        id = donnes.get('id')
        score = recuperer_score_par_ID(id)
    else:
        
        score = None
    return render_template("recherche.html", score_id=score)
