Feature: CRUD Project

  Scenario: Create project
    Given que quiero crear un proyecto

    When completo alta de proyecto, con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto", presupuesto "1000" dolares, con duracion tentativa de 7 dias y tenologias "python, react"

    And confirmo la creacion

    Then se me informa que se creo exitosamente

  Scenario: Update project

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    When edito el nombre del proyecto a "Find my team - platform", idiomas "ingles", descripcion "Plataforma de matcheo de equipos y proyecto" y tecnologias "python, react, aws"

    Then se me informa que se actualizo correctamente

    And veo que tiene nombre "Find my team - platform", idiomas "ingles", descripcion "Plataforma de matcheo de equipos y proyecto" y tecnologias "python, react, aws"


  Scenario: Update project state to cancelled

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    When edito el estado a "cancelado"

    Then se me informa que se actualizo correctamente

    And veo que tiene el estado "cancelado"


  Scenario: Update project state to finished

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    When edito el estado a "finalizado"

    Then se me informa que se actualizo correctamente

    And veo que tiene el estado "finalizado"


  Scenario: Update project state to WIP

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    When edito el estado a "en proceso"

    Then se me informa que se actualizo correctamente

    And veo que tiene el estado "en proceso"


  Scenario: List pending projects

    Given que existe el proyecto con nombre "Find my team", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    And que existe el proyecto con nombre "Find my team 2", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto" y tecnologias "python, react"

    When cuando pido todos los proyectos con estado "pendiente"

    Then me retorna 2 proyectos


  Scenario: Apply filters with empty results

    Given que existe el proyecto con nombre "Find my team" y tipo "Web", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto", tecnologias "javascript", framework "React" y presupuesto de 800 DOLAR

    And que existe el proyecto con nombre "SplitSmart" y tipo "Mobile", idiomas "ingles", descripcion "App mobile para dividir gastos", tecnologias "javascript", framework "React Native" y presupuesto de 1600 DOLAR

    When filtro por proyectos con tecnologia "python"

    Then me retorna 0 proyectos


  Scenario: Apply filters with  results

    Given que existe el proyecto con nombre "Find my team" y tipo "Web", idiomas "ingles, español", descripcion "Plataforma para matcheo de equipos y proyecto", tecnologias "javascript", framework "React" y presupuesto de 800 DOLAR

    And que existe el proyecto con nombre "SplitSmart" y tipo "Mobile", idiomas "ingles", descripcion "App mobile para dividir gastos", tecnologias "javascript", framework "React Native" y presupuesto de 1600 DOLAR

    When filtro por proyectos con tecnologia "javascript", presupuesto entre 500 y 1000 DOLAR.

    Then me retorna 1 proyectos
