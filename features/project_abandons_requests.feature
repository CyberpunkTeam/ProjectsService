Feature: CRUD project abandons requests

  Scenario: Create project abandons requests
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"
    When el owner a cargo de proyecto crea la solicitud de abandono del proyecto
    Then puedo verificar que se creo que con exito la solicitud de abandono

  Scenario: Get project abandons requests
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"
    And el owner a cargo de proyecto crea la solicitud de abandono del proyecto
    When pido la solicitud de abandono creada
    Then puedo ver las razones por las cual se abandono
    And el proyecto tiene estado de solicitud de abandono enviado

  Scenario: Update project abandons requests state
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"
    And el owner a cargo de proyecto crea la solicitud de abandono del proyecto
    When actualizo la solicitud de abandonado a aceptado
    Then puedo ver que la solicitud se actualizo correctamente
