'use strict';

var name = 'EventService';

// $http: http://docs.angularjs.org/api/ng.$http
angular.module(name, []).factory(name, ['$http', function ($http) {

    var EventService = {};

    var eventList = [];

    EventService.getEvents = function ($q, $scope) {
        // Promise: http://docs.angularjs.org/api/ng.$q
        return $q.all([$http.get('http://localhost:8000/api/events')])
            .then(function (results) {
                eventList = results[0].data;
                $scope.$emit("HideSpinner");
                return eventList;
            }, errorOnREST);
    }

    EventService.getEventList = function () {
        return eventList;
    }

    EventService.setEventList = function (newList) {
        eventList = newList;
    }

    return EventService;

}]);