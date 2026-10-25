SELECT
    id,
    UPPER(nome) AS nome,
    LOWER(email) AS email,
    idade,
    UPPER(cidade) AS cidade,
    NOW() AS created_at,
    NOW() AS updated_at
FROM {{ source('public', 'users_info') }}