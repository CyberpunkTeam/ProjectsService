Feature: CRUD project abandonment

  Scenario: Create project abandonment
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    When el equipo a cargo de proyecto crea el abandono del proyecto
    Then puedo verificar que se creo que con exito el abandono

  Scenario: Get project abandonment
    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"
    And el equipo a cargo de proyecto crea el abandono del proyecto
    When pido el abandono creado
    Then puedo ver las razones por las cual se abandono
