import markdown
from flask import Flask, render_template

#convertir le fichier md en fichier html

def generation_html(nom_du_fichier):

    print("Génération de la page Html ...")

    try :
        fichier = "Md/"+nom_du_fichier
    except :
        print("Le fichier n existe pas . Recommencer")


    with open(fichier, "r") as fichier_md:
        contenu_md = fichier_md.read()

    contenu_html = markdown.markdown(contenu_md)

    with open("Output/index.html", "w") as fichier_html:
        fichier_html.write(contenu_html)

    print("Génération terminée !")


nom_fichier = "mon_fichier"+".md"
chemin = "Md/"+nom_fichier

generation_html(nom_fichier)

#création du serveur local pour affichage du fichier html généré avec css et template

app = Flask(__name__)
app.static_folder = 'static'


#affichage du fichier markdown convertit en html
@app.route('/')
def index():
    
    with open('Output/index.html', 'r') as fichier:
        content = fichier.read()

    return render_template('base.html', 
           content=content,
           title="Projet Tutoré"
           )

#affichage du fichier markdown de base
@app.route('/md')
def md():

    global nom_fichier 

    with open('Md/'+nom_fichier,'r') as fichier :
        content=fichier.read()
    
    return render_template('md.html',content=content)

#affichage du fichier html de base
@app.route('/html')
def html():

    with open('Output/index.html','r') as fichier :
        content=fichier.read()
    
    return render_template('html.html',content=content)

if __name__ == '__main__':
    app.run()





