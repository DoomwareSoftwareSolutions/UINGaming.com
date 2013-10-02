'use strict';

/* Controllers */

var controllerName = 'RegisterCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope','$location', '$http', '$q', 'AuthService', 'PropertyService', function ($scope, $location, $http, $q, AuthService, PropertyService) {

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
					$scope.error = false;
					if (results['error-code'] == 0) {
						$scope.$emit("UserChange");
						$scope.$emit("HideSpinner");
						$location.path($scope.pathHome);
					} else {
						$scope.$emit("HideSpinner");
						$scope.error = true;
                        $scope.errorDescription = "Error: "+results['error-description'];
					}
                }, errorOnREST);
        }

        loadFields();

    }]);
