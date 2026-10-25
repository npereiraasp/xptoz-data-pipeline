SELECT
    id,
    nome,
    SPLIT_PART(nome, ' ', 1) AS primeiro_nome,
    TRIM(SUBSTR(nome, LENGTH(SPLIT_PART(nome, ' ', 1)) + 1)) AS ultimo_nome,
    email,
    SPLIT_PART(email, '@', 2) AS dominio_email,
    idade,
    cidade,
    created_at,
    NOW() AS updated_at
FROM {{ ref('stg_users_info') }}