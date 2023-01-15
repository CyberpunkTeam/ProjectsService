Feature: CRUD Projects Reviews

  Scenario: Create review
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    When el proyecto finaliza el equipo escribe la review del proyecto
    Then veo que la review se cargo correctamente

  Scenario: Get review by project
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And el equipo ya escribio la review
    When pido la review del proyecto
    Then me trae la review
