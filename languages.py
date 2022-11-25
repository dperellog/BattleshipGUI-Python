#Fitxer per afegir suport pels idiomes.

#Funció que retorna o printa una string segons idioma, nom i paràmetres.
def text(text, idioma, *p, mostrar=False):
        strPrint = "Text not found"
        text = text.split("/")
        if idioma in ('ca', 'es', 'en'):
                if len(text) == 1:
                        strPrint = lang[idioma][text[0]]
                elif len(text) == 2:
                        strPrint = lang[idioma][text[0]][text[1]]
        if len(p) == 1:
                strPrint = strPrint.format(p[0])
        elif len(p) == 2:
                strPrint = strPrint.format(p[0],p[1])
        if mostrar:
                print(strPrint)
        else:
                return(strPrint)

lang = {
        
        #IDIOMA CATALÀ:
        'ca' : {
        'menu': {
                'newGame' : 'Crear Nova Partida',
                'resumeGame' : 'Recuperar partida',
                'createNewGame' : 'Crear nou tauler',        
                'activePlaygrounds' : 'Partides actives:',
                'changeLng' : 'Canviar idioma',
                'exitGame' : 'Sortir del joc'
        },



        'playground': {
                'info' : 'Info del tauler:',
                'name' : 'Nom del tauler: {0}',
                'playWLives' : 'Vols jugar amb vides? ',
                'enterName' : 'Introdueix un nom pel identificar el tauler: ',
                'delete': 'Eliminar tauler',
                'remaining' : "Vides restants:",
                'touched' : 'TOCAT!',
                'water' : 'AIGUA!',
                'sink' : 'HAS ENFONSAT {0}!',
                'winMessage' : 'FELICITATS! HAS GUANYAT!',
                'deathMessage' : 'Quina pena! El jugador ha mort!',

        },


        'fleet': {
                'four': 'un portaavions',
                'three': 'un cuirassat',
                'two' : 'una fragata',
                'one' : 'una patrullera'
        },

        'errors' : {
                'noActiveGames' : 'No s\'han trobat partides actives!'
        }
        
        #IDIOMA CASTELLÀ:
        },'es' : {
        'menu': {
                'newGame' : 'Empezar una nueva partida',
                'resumeGame' : 'Recuperar una partida anterior',   
                'createNewGame' : 'Crear nuevo tablero',       
                'activePlaygrounds' : 'Partidas activas:',
                'changeLng' : 'Cambiar el idioma',
                'exitGame' : 'Salir del juego'
        },



        'playground': {
                'info' : 'Info del tablero:',
                'name' : 'Nombre del tablero: {0}',
                'playWLives' : '¿Deseas jugar con vidas? ',
                'enterName' : 'Introduce un nombre para identificar el tablero: ',
                'delete': 'Eliminar tablero',
                'remaining' : "Vidas restantes:",
                'touched' : '¡TOCADO!',
                'water' : '¡AGUA!',
                'sink' : '¡HAS HUNDIDO {0}!',
                'winMessage' : '¡FELICIDADES! ¡HAS GANADO!',
                'deathMessage' : '¡Qué pena! El jugador ha muerto!',

        },


        'fleet': {
                'four': 'un portaviones',
                'three': 'un acorazado',
                'two' : 'una fragata',
                'one' : 'una patrullera'
        },

        'errors' : {
                'noActiveGames' : '¡No se han encontrado partidas activas!'
        }
        #IDIOMA INGLES
        },'en' : {
        'menu': {
                'newGame' : 'Start a new game',
                'resumeGame' : 'Recover an old game',
                'createNewGame' : 'Create new game',          
                'activePlaygrounds' : 'Active Playgrounds:',
                'changeLng' : 'Change the language',
                'exitGame' : 'Exit'
        },



        'playground': {
                'info' : 'Playground Info:',
                'name' : 'Playground name: {0}',
                'playWLives' : 'Do you want to play with lives? ',
                'enterName' : 'Enter a name for the playground: ',
                'delete': 'Delete Playground',
                'remaining' : "Remaining lives:",
                'touched' : 'REACHED!',
                'water' : 'WATER!',
                'sink' : 'YOU\'VE SUNKEN {0}!',
                'winMessage' : 'CONGRATULATIONS! YOU HAVE WIN!',
                'deathMessage' : 'What a pitty! The player has died!',

        },


        'fleet': {
                'four': 'an aircraft carrier',
                'three': 'a battleship',
                'two' : 'a frigate',
                'one' : 'a patrol boat'
        },

        'errors' : {
                'noActiveGames' : 'ERROR: ¡No active games found!'
        }
        
        }
}