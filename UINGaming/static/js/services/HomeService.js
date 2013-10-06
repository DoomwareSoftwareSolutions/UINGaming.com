'use strict';

var name = 'HomeService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var HomeService = {};

    HomeService.getNews = function ($q) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get('http://localhost:8000/api/news?begin=0&end=2')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    HomeService.getEvents = function ($q) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get('http://localhost:8000/api/eventSearch?n=2')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    return HomeService;

}]);