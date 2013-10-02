'use strict';

var name = 'EventService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var EventService = {};

    var eventList = [];

    var currentEventPk;

    var serverUrl = "http://localhost:8000";

    EventService.deleteEvent = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/eventDelete?pk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }

    EventService.getEvents = function ($q, $scope) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get(serverUrl+"/"+'api/events')
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
    
    EventService.getEventsByUser = function ($q, $scope, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.get(serverUrl+"/"+'api/eventsByUser?pk='+pk)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }
    
    EventService.getEvent = function ($q, $scope, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/events?pk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }
    
    EventService.addEvent = function ($q, EventData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        EventData.pk = -1;
        var deferred = $q.defer();
        $http.post(serverUrl+"/"+'api/events', [EventData])
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    EventService.editEvent = function ($q, EventData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post(serverUrl+"/"+'api/events', [EventData])
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }


	EventService.registerToEvent = function ($q, EventData) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        $http.post(serverUrl+"/"+'api/eventMembership', EventData)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
        return deferred.promise;
    }

    EventService.getEventMemberships = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/eventMembership?eventPk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }
    
    EventService.getUserMemberships = function ($q, pk) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/eventMembership?userPk='+pk;
        $http.get(url)
            .success(function (jsonData) {
                deferred.resolve(jsonData);
            });
            
        return deferred.promise;
    }

    EventService.getMembershipByUserAndEvent = function ($q, pkEvent, username) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        var deferred = $q.defer();
        var url = serverUrl+"/"+'api/eventMembership?userPk='+pk+'&eventPk='+pkEvent;
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
