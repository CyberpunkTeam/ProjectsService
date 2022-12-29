Feature: CRUD Project Postulations


  Scenario: Create project postulations
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And que quiero postular a mi equipo "Alfa" al projecto "Find my team"
    When completo el formulario de postulacion con presupuesto estimado 100 dolares
    And descripcion de propuesta "Somos un equipo con mucha experiencia en desarrollo"
    And envio postulacion
    Then se confirma que se envio la propuesta

  Scenario: Find project postulations by project
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And que el equipo "Alfa" se postulo mi projecto "Find my team"
    And que el equipo "Omega" se postulo mi projecto "Find my team"
    When pido los postulados a mi proyecto "Find my team"
    Then recibo que el equipo "Alfa" se postulo
    And recibo que el equipo "Omega" se postulo

  Scenario: Find project postulations by team
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And que el equipo "Alfa" se postulo mi projecto "Find my team"
    When pido los postulados de mi equipo "Alfa"
    Then recibo el proyecto "Find my team"

  Scenario: Accept postulation
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And que el equipo "Alfa" se postulo mi projecto "Find my team"
    When acepto la postulacion
    Then la postulacion figura como aceptada

  Scenario: Reject postulation
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And que el equipo "Alfa" se postulo mi projecto "Find my team"
    When cancelo la postulacion
    Then la postulacion figura como cancelada
