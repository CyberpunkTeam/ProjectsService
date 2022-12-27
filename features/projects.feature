Feature: CRUD Project


  Scenario: Create project
    Given que quiero crear un proyecto

    When completo alta de proyecto, con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"

    And confirmo la creacion

    Then se me informa que se creo exitosamente

  Scenario: Update project

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"

    When edito el nombre del proyecto a "Find my team - platform", idiomas "ingles", descripcion "Plataforma de matcheo de equipos y proyecto" y tenologias "python, react, aws"

    Then se me informa que se actualizo correctamente

    And veo que tiene nombre "Find my team - platform", idiomas "ingles", descripcion "Plataforma de matcheo de equipos y proyecto" y tenologias "python, react, aws"
