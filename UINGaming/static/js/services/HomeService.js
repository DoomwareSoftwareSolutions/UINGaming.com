'use strict';

var name = 'HomeService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var HomeService = {};

    HomeService.getSlides = function ($q, $scope) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        return $q.all([$http.get('http://localhost:8000/api/slides')])
            .then(function (results) {
                var slideList = results[0].data;
                $scope.$emit("HideSpinner");
                return slideList;
            }, errorOnREST);
    }

    HomeService.getFeatures = function ($q, $scope) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        return $q.all([$http.get('http://localhost:8000/api/features')])
            .then(function (results) {
                var featureList = results[0].data;
                return featureList;
            }, errorOnREST);
    }

    return HomeService;

}]);