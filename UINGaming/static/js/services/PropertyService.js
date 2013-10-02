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
        pathEventsEnrolled: '/eventsEnrolled',
        pathEventRegister: '/eventregister',
        pathEventAdd: '/eventAdd',
        pathEventEdit: '/eventEdit',
        pathNews: '/news',
        pathNewsViewer: '/news-viewer',
        pathNewsAdd: '/news-add',
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
            eventsEnrolled: 'Eventos Inscripto',
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
        },
        en: {
            formTitle: 'Subscribirse a evento',
            teamNamePlaceholder: 'Nombre del team',
            teamTagPlaceholder: 'Tag del team',
            teamMembersPlaceholder: 'Miembros del team',
        }
    };
    
    PropertyService.properties.news = {
        es: {
            continueReadingPlaceholder: 'Continuar leyendo',
        },
        en: {
            continueReadingPlaceholder: 'Continue reading',
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
