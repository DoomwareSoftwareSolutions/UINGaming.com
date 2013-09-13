'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService', function ($scope, $http, $q, AuthService) {

        $scope.$emit("BackgroundChange", "signin-background");

        $scope.user = {
            email: '',
            password: ''
        }

        $scope.rememberUser = true;

        $scope.signIn = function () {
            $scope.$emit("ShowSpinner");
            AuthService.loginUser($q, $scope.user)
                .then(function (results) {
                    // Prueba funcionamiento mostrando el response
                    alert(JSON.stringify(results));
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
        }

    }]);
