Feature: CRUD Project


  Scenario: Create project
    Given que quiero crear un proyecto

    When completo alta de proyecto, con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tenologias "python, react"

    And confirmo la creacion

    Then se me informa que se creo exitosamente
