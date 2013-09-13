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
                passwordRepeat: '',
                firstName: '',
                lastName: ''
            }
        }

        loadFields();

    }]);
