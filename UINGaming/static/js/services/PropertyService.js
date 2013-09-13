'use strict';

var name = 'PropertyService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var PropertyService = {};

    PropertyService.properties = {};

    PropertyService.properties.signIn = {
        es: {
            formTitle: 'Inicie sesión',
            emailPlaceholder: 'Dirección de email',
            passwordPlaceholder: 'Contraseña',
            rememberLabel: 'Recordarme',
            submitLabel: 'Iniciar sesión'
        },
        en: {
            formTitle: 'Please sign in',
            emailPlaceholder: 'Email address',
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

    return PropertyService;

}]);