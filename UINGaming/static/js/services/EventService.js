'use strict';

var name = 'EventService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var EventService = {};

    var eventList = [];

    var currentEventPk;

    EventService.getEvents = function ($q, $scope) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get('http://localhost:8000/api/events')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
    
    EventService.getEvent = function ($q, $scope, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = 'http://localhost:8000/api/events?pk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }

	EventService.registerToEvent = function ($q, EventData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post('http://localhost:8000/api/eventMembership', EventData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    EventService.getEventMemberships = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = 'http://localhost:8000/api/eventMembership?pk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }
	
    EventService.getEventList = function () {
        return eventList;
    }

    EventService.setEventList = function (newList) {
        eventList = newList;
    }

    EventService.getEventPk = function(){
        return currentEventPk;
    }

    EventService.setEventPk = function(pk){
        currentEventPk = pk;
    }
    return EventService;

}]);
