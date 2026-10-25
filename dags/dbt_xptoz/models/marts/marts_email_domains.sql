SELECT
    dominio_email,
    COUNT(id) AS total_registros,
    MIN(created_at) AS created_at,
    NOW() AS updated_at
FROM {{ ref('int_users_transformed') }}
GROUP BY dominio_email
ORDER BY total_registros DESC