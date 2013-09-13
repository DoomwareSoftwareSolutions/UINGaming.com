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
        pathEventRegister: '/eventregister'
    }
    PropertyService.properties.navBar = {
        es: {
            pageTitle: 'UIN Gaming',
            signIn: 'Iniciar Sesión',
            register: 'Registrarse',
            home: 'Home',
            events: 'Eventos',
            eventRegister: 'Registrarse a Evento'
        },
        en: {
            pageTitle: 'UIN Gaming',
            signIn: 'Sign In',
            register: 'Register',
            home: 'Home',
            events: 'Events',
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