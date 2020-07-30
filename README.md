# Djang-GraphQL-Graphene-Relay-API
Ejecutar los requeriments.txt para arrancar la API
Para probar la api se debe ser superusuario o crear una cuenta desde /admin, en las urls del project esta la documentacion basica de la API
Datos de Prueba

mutation{
  createCharacter(name:"Skywalker",height:"160",mass:"160",gender:"Male",homeworld:"Tierra"){
    name{
      id
      name
      height
      mass
      gender
      homeworld
    }
  }
}
mutation{
  createFilm(openingCrawl:"star wars theme",director:"J. J. Abrams",characterId:1){
    name{
      id
      openingCrawl
      director
    }
  }
}
#creo un planeta para el film con id 1, creado en la mutation anterior
mutation{
  createPlanet(name:"Marte",poblation:"890000",filmId:1){
    name{
      id
      name
      poblation
    }
  }
}
}
#creo otro planeta para el film con id 1, creado en la mutation anterior
mutation{
  createPlanet(name:"Venus",poblation:"10020",filmId:1){
    name{
      id
      name
      poblation
    }
  }
}
#creo productor para el film con id 1
mutation{
  createProducer(name:"George", lastName:"Lucas", filmeId:1){
    name{
      id
      name
      lastName
    }
  }
}
#creo otro productor para el film con id 1
mutation{
  createProducer(name:"George", lastName:"Lucas", filmeId:1){
    name{
      id
      name
      lastName
    }
  }
}

query de datos anteriores
query{
  allFilms(character_Name:"Skywalker"){
    edges{
      node{
        id
        openingCrawl
        director,
        character{
          id
          name
          homeworld
          mass
        },
        planets{
          edges{
            node{
              id
              name
            }
          }
        },
        producers{
          edges{
            node{
              id
              name
              lastName
            }
          }
        }
      }
    }
  }
}





