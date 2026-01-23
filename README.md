# 📊 Dashboard de Contatos — Odoo + Flask

Dashboard web desenvolvido em **Flask**, que consome dados do **Odoo via API (XML-RPC)** em tempo real e apresenta **KPIs e gráficos interativos** para análise de contatos.

O objetivo do projeto é demonstrar:
- Integração com Odoo
- Tratamento e agregação de dados com Pandas
- Visualização clara e interativa com Plotly
- Organização de código e boas práticas de backend + frontend

---

## 🚀 Funcionalidades

### 🔐 Integração com Odoo
- Autenticação via API do Odoo
- Leitura do modelo **res.partner**
- Consumo direto da API (sem exportação manual)

### 📌 KPIs principais
- Total de contatos  
- Clientes ativos  
- Percentual de clientes ativos  
- Países distintos  

### 📈 Gráficos interativos
- **Pizza**: clientes ativos vs inativos  
- **Barras**: distribuição geográfica dos contatos  
- **Linha**: evolução diária de novos clientes  

### 🎨 Interface
- Layout moderno, limpo e responsivo  
- Cards de KPI  
- Barra de pesquisa (UI)  
- Gráficos com títulos, eixos e legendas claras  

### ⚠️ Tratamento básico de erros
- Sem dados retornados
- Falha de autenticação na API
- Exceções controladas no backend

---

## 🧱 Estrutura do projeto

```text
dashboard-odoo/
├── app.py                 # Aplicação Flask
├── odoo_client.py         # Integração com a API do Odoo
├── templates/
│   └── dashboard.html     # Template HTML (Jinja + Plotly)
├── static/
│   └── style.css          # Estilos da aplicação
├── requirements.txt       # Dependências do projeto
├── .env.example           # Variáveis de ambiente (exemplo)
├── .gitignore
└── README.md
