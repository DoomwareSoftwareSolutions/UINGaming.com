'use strict';

/* Controllers */

var controllerName = 'SignInCtrl';

angular.module(controllerName, []).
    controller(controllerName, ['$scope', '$location', '$http', '$q', 'AuthService', 'PropertyService', function ($scope, $location, $http, $q, AuthService, PropertyService) {

        $scope.$emit("BackgroundChange", "signin-background");
        $scope.error =false;
        $scope.errorDescription = "";
        var loadFields = function () {
            PropertyService.loadFields('signIn', 'en', $scope);
            PropertyService.loadPaths($scope);
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

    }]);
