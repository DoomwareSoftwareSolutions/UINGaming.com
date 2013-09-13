'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$http', '$q', 'AuthService', 'PropertyService', function ($scope, $http, $q, AuthService, PropertyService) {

        $scope.$emit("BackgroundChange", "signin-background");

        var loadFields = function () {
            PropertyService.loadFields('signIn', 'en', $scope);
            $scope.user = {
                username: '',
                password: ''
            }
            $scope.rememberUser = true;
        }

        loadFields();

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
