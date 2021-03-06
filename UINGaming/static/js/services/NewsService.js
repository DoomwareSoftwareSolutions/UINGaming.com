'use strict';

var name = 'NewsService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var NewsService = {};

    var eventList = [];

    var currentEventPk;

    var serverUrl = "http://localhost:8000";

    NewsService.getNews = function ($q, $scope, begin, end) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
		var url = serverUrl+"/"+'api/news?begin='+begin+'&end='+end
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
    
    
    NewsService.getNew = function ($q, $scope, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/news-viewer?pk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }
    
    NewsService.addNew = function ($q, nnew) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post(serverUrl+'/api/news', nnew)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
	
	NewsService.editNew = function ($q, pk, nnew) {
        // Promise: http://docs.angularjs.org/api/ng.$q
		nnew.pk = pk
        var deferred = $q.defer();
        $http.post(serverUrl+'/api/news', nnew)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
    
	NewsService.deleteNew = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
		var data = new Object();
        var url = serverUrl+'/api/news-delete';
		data.pk = pk;
        $http.post(url,data)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }
	
    return NewsService;

}]);
