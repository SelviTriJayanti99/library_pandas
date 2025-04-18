from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Data Anime: Judul, Genre, Tahun Rilis, Studio
    data = {
        "Judul": ["Naruto", "Attack on Titan", "My Hero Academia", "One Piece", "Demon Slayer"],
        "Genre": ["Action, Adventure", "Action, Fantasy", "Action, Superhero", "Adventure, Fantasy", "Action, Supernatural"],
        "Tahun Rilis": [2002, 2013, 2016, 1999, 2019],
        "Studio": ["Studio Pierrot", "WIT Studio", "Bones", "Toei Animation", "ufotable"]
    }
    df = pd.DataFrame(data)

    # Convert DataFrame ke HTML tabel
    table_html = df.to_html(classes='data', index=False)

    return render_template("index.html", table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
