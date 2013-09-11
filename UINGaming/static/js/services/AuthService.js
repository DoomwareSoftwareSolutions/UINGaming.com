'use strict';

var name = 'AuthService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var AuthService = {};

    var eventList = [];

    AuthService.registerUser = function ($q, $scope, userData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        return $q.all([$http.post('http://localhost:8000/api/signup', userData)])
            .then(function (results) {
                eventList = results[0].data;
                return eventList;
            }, errorOnREST);
    }

    return AuthService;

}]);