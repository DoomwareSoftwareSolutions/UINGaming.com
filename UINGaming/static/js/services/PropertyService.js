'use strict';

var name = 'PropertyService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var PropertyService = {};

    PropertyService.properties = {};

    PropertyService.properties.paths = {
        pathSignIn: '/signin',
        pathRegister: '/register',
        pathHome: '/home',
        pathEvents: '/events',
        pathProfile: '/profile',
        pathProfileEdit: '/profileEdit',
        pathEventRegister: '/eventregister',
        pathEventAdd: '/eventAdd',
        pathEventEdit: '/eventEdit',
        pathNews: '/news',
        pathNewsViewer: '/news',
        pathNewsAdd: '/news/add',
        pathNewsEdit: '/news/edit',
    }
    PropertyService.properties.navBar = {
        es: {
            pageTitle: 'UIN Gaming',
            signIn: 'Iniciar Sesión',
            logOut: 'Cerrar Sesión',
            register: 'Registrarse',
            home: 'Home',
            news: 'Noticias',
            events: 'Eventos',
            eventRegister: 'Registrarse a Evento'
        },
        en: {
            pageTitle: 'UIN Gaming',
            signIn: 'Sign In',
            logOut: 'LogOut',
            register: 'Register',
            home: 'Home',
            news: 'News',
            events: 'Events',
            eventsEnrolled: 'Eventos Inscripto',
            eventRegister: 'Event Register'
        }
    };
    PropertyService.properties.signIn = {
        es: {
            formTitle: 'Inicie sesión',
            usernamePlaceholder: 'Nombre de usuario',
            passwordPlaceholder: 'Contraseña',
            rememberLabel: 'Recordarme',
            submitLabel: 'Iniciar sesión'
        },
        en: {
            formTitle: 'Please sign in',
            usernamePlaceholder: 'Username',
            passwordPlaceholder: 'Password',
            rememberLabel: 'Remember me',
            submitLabel: 'Sign in'
        }
    };
    PropertyService.properties.register = {
        es: {
            formTitle: 'Registrar usuario',
            usernamePlaceholder: 'Nombre de usuario',
            emailPlaceholder: 'Dirección de email',
            passwordPlaceholder: 'Contraseña',
            passwordRepeatPlaceholder: 'Repita la contraseña',
            namePlaceholder: 'Nombre',
            surnamePlaceholder: 'Apellido',
            submitLabel: 'Registrarse'
        },
        en: {
            formTitle: 'Register',
            usernamePlaceholder: 'Username',
            emailPlaceholder: 'Email address',
            passwordPlaceholder: 'Password',
            passwordRepeatPlaceholder: 'Repeat password',
            namePlaceholder: 'First name',
            surnamePlaceholder: 'Last name',
            submitLabel: 'Register'
        }
    };
   
     PropertyService.properties.eventRegister = {
        es: {
            formTitle: 'Subscribirse a evento',
            teamNamePlaceholder: 'Nombre del team',
            teamTagPlaceholder: 'Tag del team',
            teamMembersPlaceholder: 'Miembros del team',
			gotoEventPlaceholeder: 'Ir al evento',
        },
        en: {
            formTitle: 'Subscribirse a evento',
            teamNamePlaceholder: 'Nombre del team',
            teamTagPlaceholder: 'Tag del team',
            teamMembersPlaceholder: 'Miembros del team',
			gotoEventPlaceholeder: 'Go to event',
        }
    };
    
     PropertyService.properties.eventsView = {
        es: {
			noEvents: 'No hay eventos a los que estes inscripto.'
        },
        en: {
			noEvents: 'No hay eventos a los que estes inscripto.'
        }
    };
    
     PropertyService.properties.profile = {
        es: {
			noEvents: 'No hay eventos a los que estes inscripto.'
        },
        en: {
			noEvents: 'No hay eventos a los que estes inscripto.'
        }
    };
    
    PropertyService.properties.eventsdetail = {
        es: {
            registerToEvent: "Unirse al evento",
            editEvent: "Editar evento",
            deleteEvent: "Eliminar evento",
            eventManagement: "Configuracion del evento"
        },
        en: {
            registerToEvent: "Register to event",
            editEvent: "Edit event",
            deleteEvent: "Delete event",
            eventManagement: "Event Management"
        }
        
    };
    
    PropertyService.properties.news = {
        es: {
            continueReadingPlaceholder: 'Continuar leyendo',
			noNews: 'No hay noticias.',
			readPlaceholder: 'Leer',
            newHeaderPlaceholder: "Título",
            newSubheaderPlaceholder: "Subtítulo",
            newBodyPlaceholder: "Cuerpo de la noticia",
            newImagePlaceholder: "Imagen para el slider",
            editNewPlaceholder:'Editar noticia',
            addNewPlaceholder:'Crear noticia',
			saveNewPlaceholder:'Guardar noticia',
            deleteNewPlaceholder:'Eliminar noticia',
        },
        en: {
            continueReadingPlaceholder: 'Continue reading',
			noNews: 'There is no news.',
			readPlaceholder: 'Read',
            newHeaderPlaceholder: "Title",
            newSubheaderPlaceholder: "Subtitle",
            newBodyPlaceholder: "New's Body",
            newImagePlaceholder: "Image for slider",
            editNewPlaceholder:'Edit new',
            addNewPlaceholder:'Add new',
			saveNewPlaceholder:'Save',
			deleteNewPlaceholder:'Delete new',
        }
    };
    
    PropertyService.getProperties = function () {
        return PropertyService.properties;
    }

    PropertyService.loadFields = function (pageName, language, $scope) {
        var messageBundle = PropertyService.getProperties()[pageName][language];
        for (var property in messageBundle) {
            $scope[property] = messageBundle[property];
        }
    }

    PropertyService.loadPaths = function ($scope) {
        var messageBundle = PropertyService.getProperties().paths;
        for (var property in messageBundle) {
            $scope[property] = messageBundle[property];
        }
    }

    return PropertyService;

}]);
