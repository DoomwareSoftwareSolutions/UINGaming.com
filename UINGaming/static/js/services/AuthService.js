'use strict';

var name = 'AuthService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var AuthService = {};

    AuthService.registerUser = function ($q, userData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post('http://localhost:8000/api/signup', userData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    AuthService.loginUser = function ($q, userData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post('http://localhost:8000/api/signin', userData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    return AuthService;

}]);