Feature: CRUD project finished requests

  Scenario: Create project finished requests
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    When el owner a cargo de proyecto crea la solicitud de finalizar el proyecto
    Then puedo verificar que se creo que con exito la solicitud de finalizacion

  Scenario: Get project finished requests
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And el owner a cargo de proyecto crea la solicitud de finalizar el proyecto
    When pido la solicitud de finalizacion creada
    Then puedo ver las solicitud de finalizacion esta pendiente
    And el proyecto tiene estado de solicitud de finalizacion enviado

  Scenario: Update project finished requests state
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And el owner a cargo de proyecto crea la solicitud de finalizar el proyecto
    When actualizo la solicitud de finalizado a aceptado
    Then puedo ver que la solicitud se actualizo correctamente
