from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField
from wtforms.validators import InputRequired, Length
from flask import Flask, request, redirect, render_template, url_for
from google import get_doctors_by_local


app = Flask(__name__)
app.config["SECRET_KEY"] = "YOUR SECRET KEY"


OCCUPATIONS = [
	("Acupuntura Médica"),
	("Alergia e Imunologia Pediátrica"),
	("Anestesiologia"),
	("Angiologia"),
	("Angiorradiologia e Cirurgia Endovascular"),
	("Cancerologia"),
	("Cardiologia"),
	("Cardiologia Pediátrica"),
	("Cirurgia Cardiovascular"),
	("Cirurgia da Mão"),
	("Cirurgia de Cabeça e Pescoço"),
	("Cirurgia do Aparelho Digestivo"),
	("Cirurgia Geral"),
	("Cirurgia Pediátrica"),
	("Cirurgia Plástica"),
	("Cirurgia Torácica"),
	("Cirurgia Vascular"),
	("Cirurgia Videolaparoscópica"),
	("Clínica Médica"),
	("Coloproctologia"),
	("Dermatologia"),
	("Ecocardiografia Pediátrica"),
	("Endocrinologia e Metabologia"),
	("Endocrinologia Pediátrica"),
	("Endoscopia"),
	("Endoscopia Digestiva"),
	("Foniatria"),
	("Gastroenterologia"),
	("Genética Médica"),
	("Geriatria"),
	("Ginecologia e Obstetrícia"),
	("Hematologia e Hemoterapia"),
	("Hepatologia"),
	("Homeopatia"),
	("Infectologia"),
	("Mastologia"),
	("Medicina de Família e Comunidade"),
	("Medicina de Tráfego"),
	("Medicina do Trabalho"),
	("Medicina Física e Reabilitação"),
	("Medicina Intensiva"),
	("Medicina Nuclear"),
	("Nefrologia"),
	("Neurocirurgia"),
	("Neurofisiologia Clínica"),
	("Neurologia"),
	("Neurologia Pediátrica"),
	("Neurorradiologia"),
	("Neurorradiologia Terapêutica"),
	("Nutrição Parenteral e Enteral"),
	("Nutrologia"),
	("Oftalmologia"),
	("Ortopedia e Traumatologia"),
	("Otorrinolaringologia"),
	("Patologia"),
	("Patologia Clínica/Medicina Laboratorial"),
	("Pediatria"),
	("Pneumologia"),
	("Psicogeriatria"),
	("Psicoterapia"),
	("Psiquiatria"),
	("Radiologia e Diagnóstico Por Imagem"),
	("Radioterapia"),
	("Reumatologia"),
	("Ultrassonografia"),
	("Urologia")
]

class FormSearch(FlaskForm):
	city = StringField("city", validators=[InputRequired(),
		Length(max=20)])
	occupation = SelectField("occupation", choices=OCCUPATIONS,
		validators=[InputRequired()])


@app.route("/", methods=["GET", "POST"])
def home():
	form = FormSearch()
	if request.method == "POST":
		if form.validate():
			response = get_doctors_by_local(
				query = form.occupation.data,
				location = form.city.data)
			if response:
				return render_template("result.html", doctors=response)
			flash("Naõ foi possível buscar os dados")
	return render_template("home.html", form=form)
	

if __name__ == "__main__":
	app.run(debug=True)