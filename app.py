from flask import Flask, render_template
from dotenv import load_dotenv
import pandas as pd

from odoo_client import fetch_partners

load_dotenv()

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        data = fetch_partners()

        if not data:
            return "Sem dados disponíveis no Odoo"

        df = pd.DataFrame(data)

        # ===== Normalização =====
        df["cliente_ativo"] = df["x_studio_boolean_field_7ls_1jeug4mgc"].fillna(False)

        df["pais"] = df["country_id"].apply(
            lambda x: x[1] if isinstance(x, list) else "Não informado"
        )

        df["create_date"] = pd.to_datetime(df["create_date"])

        # ===== KPIs =====
        total_contatos = len(df)
        total_ativos = int(df["cliente_ativo"].sum())
        perc_ativos = round((total_ativos / total_contatos) * 100, 1)
        total_paises = df["pais"].nunique()

        # ===== Gráfico 1 — Pizza =====
        pizza_clientes = (
            df["cliente_ativo"]
            .value_counts()
            .rename(index={True: "Ativo", False: "Inativo"})
        )

        # ===== Gráfico 2 — País =====
        contatos_por_pais = df["pais"].value_counts()

        # ===== Gráfico 4 — Linha temporal =====
        criacao_dia = (
            df
            .set_index("create_date")
            .resample("D")
            .size()
            .loc[pd.Timestamp.today().strftime("%Y-%m")]
        )
        criacao_dia.index = criacao_dia.index.day

        # ===== Render =====
        return render_template(
            "dashboard.html",
            total_contatos=total_contatos,
            total_ativos=total_ativos,
            perc_ativos=perc_ativos,
            total_paises=total_paises,
            pizza_clientes=pizza_clientes,
            contatos_por_pais=contatos_por_pais,
            criacao_dia=criacao_dia,
        )

    except Exception as e:
        return f"Erro ao carregar dashboard: {e}"


if __name__ == "__main__":
    app.run(debug=True)
