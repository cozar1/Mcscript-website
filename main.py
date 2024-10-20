from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
database = "database.db"

@app.route('/')
def home():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    mods = cursor.execute('''
SELECT mods.mod_name, genre.genre_name, studio.studio_name, views, downloads, likes, mods.id, tags.tag_name
FROM mods 
JOIN genre ON mods.genre_id = genre.id
JOIN tags ON mods.tag_id = tags.id
JOIN studio On mods.studio_id = studio.id;
''')

    mods = cursor.fetchall()
    for i in range(len(mods)):
        mods[i] = {
            "mod_name": mods[i][0],
            "genre_name": mods[i][1],
            "studio_name": mods[i][2],
            "views": mods[i][3],
            "downloads": mods[i][4],
            "likes": mods[i][5],
            "id": mods[i][6],
            "genre": mods[i][7]
        }

    return render_template('mods.html', mods=mods)


@app.route('/mod/<int:id>')
def Mod(id):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    mods = cursor.execute('''
SELECT mods.mod_name, genre.genre_name, studio.studio_name, views, downloads, likes, mods.id
FROM mods 
JOIN genre ON mods.genre_id = genre.id
JOIN studio On mods.studio_id = studio.id
WHERE mods.id = ?
''', (id,))

    mods = cursor.fetchall()
    mods = mods[0]
    mods = {
        "mod_name": mods[0],
        "genre_name": mods[1],
        "studio_name": mods[2],
        "views": mods[3],
        "downloads": mods[4],
        "likes": mods[5],
        "mod_id": mods[6]
    }

    return render_template("mod.html", mod=mods)

@app.route('/resource_packs')
def Resource_Packs():
    return render_template("resource_packs.html")

if __name__ == "__main__":
    app.run(debug=True)