# Autenticação e leitura em runtime via API do Odoo
import os
import xmlrpc.client

def get_odoo_connection():
    url = os.getenv("ODOO_URL")
    db = os.getenv("ODOO_DB")
    user = os.getenv("ODOO_USER")
    password = os.getenv("ODOO_PASSWORD")

    if not all([url, db, user, password]):
        raise Exception("Variáveis de ambiente do Odoo não configuradas")

    common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
    uid = common.authenticate(db, user, password, {})

    if not uid:
        raise Exception("Falha na autenticação com o Odoo")

    models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

    return models, db, uid, password


def fetch_partners():
    models, db, uid, password = get_odoo_connection()

    fields = [
        "name",
        "is_company",
        "country_id",
        "state_id",
        "create_date",
        "x_studio_boolean_field_7ls_1jeug4mgc",
    ]

    partners = models.execute_kw(
        db,
        uid,
        password,
        "res.partner",
        "search_read",
        [[]],
        {"fields": fields}
    )

    return partners
