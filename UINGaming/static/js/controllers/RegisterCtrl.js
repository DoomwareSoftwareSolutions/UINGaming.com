'use strict';

/* Controllers */

var controllerName = 'RegisterCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService', 'PropertyService', function ($scope, $http, $q, AuthService, PropertyService) {

        $scope.$emit("BackgroundChange", "signin-background");

        var loadFields = function () {
            PropertyService.loadFields('register', 'en', $scope);
            $scope.user = {
                username: '',
                email: '',
                password: '',
                vpassword: '',
                name: '',
                lastname: ''
            }
        }

        $scope.register = function () {
            AuthService.registerUser($q, $scope.user)
                .then(function (results) {
                    // Prueba funcionamiento mostrando el response
                    alert(JSON.stringify(results));
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
        }

        loadFields();

    }]);
