# XPTOZ — Pipeline de Engenharia de Dados

Este repositório contém a solução completa para o case técnico de Engenharia de Dados da **XPTOZ — Saúde em Tecnologia**, estruturado para automatizar a análise de cadastros de pessoas e identificar os domínios de e-mail mais utilizados.

---

## 🏗️ 1. Arquitetura e Fluxo de Processamento
O pipeline foi construído utilizando uma arquitetura em camadas moderna (*Medallion Architecture* simplificada), garantindo a separação entre dados brutos e analíticos[cite: 1]:

1. **Camada Raw (Dados Brutos):** Tabela `users_info` populada via script Python utilizando a biblioteca `Faker`[cite: 1].
2. **Camada Staging (Padronização):** Normalização de textos (maiúsculas/minúsculas) e adição de metadados de controlo (`created_at`, `updated_at`) gerados via DBT[cite: 1].
3. **Camada Intermediate (Enriquecimento):** Divisão do nome completo em primeiro e último nome, e extração limpa do domínio do e-mail[cite: 1].
4. **Camada Marts (Consolidação):** Tabela analítica agregada por domínio de e-mail com a respetiva contagem total de registos[cite: 1].

---

## 🛠️ 2. Tecnologias Utilizadas
* **PostgreSQL:** Armazenamento relacional dos dados[cite: 1].
* **Python (Faker & Psycopg2):** Ingestão e carga inicial de dados simulados[cite: 1].
* **DBT (Data Build Tool):** Transformação modular dos dados em camadas[cite: 1].
* **Apache Airflow:** Orquestração e agendamento diário do pipeline[cite: 1].
* **Docker:** Gestão e execução local do ambiente de base de dados[cite: 1].

---

## 📂 3. Organização do Repositório
```text
xptoz-data-pipeline/
├── dags/
│   └── xptoz_pipeline_dag.py     # DAG do Apache Airflow para orquestração diária
├── dbt_xptoz/
│   ├── models/
│   │   ├── staging/              # stg_users_info.sql e schema.yml
│   │   ├── intermediate/         # int_users_transformed.sql
│   │   └── marts/                # marts_email_domains.sql
│   └── dbt_project.yml
├── scripts/
│   └── generate_data.py          # Script Python de geração e carga Raw
├── docker-compose.yml            # Configuração do PostgreSQL local
└── README.md                     # Documentação técnica do projeto
