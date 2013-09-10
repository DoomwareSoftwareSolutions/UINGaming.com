'use strict';

// Declare app level module which depends on filters, and services

var depList = [
    'myApp.filters',
    'myApp.services',
    'myApp.directives',
    'EventService',
    'HomeService',
    'EventRegisterCtrl',
    'BackgroundCtrl',
    'SignInCtrl',
    'HomeCtrl',
    'EventsCtrl',
    'NavCtrl'
]

angular.module('myApp', depList).
    config(function ($routeProvider, $locationProvider) {
        $routeProvider.
            when('/home', {
                templateUrl: 'partials/HomeView',
                controller: 'HomeCtrl'
            }).
            when('/events', {
                templateUrl: 'partials/EventsView',
                controller: 'EventsCtrl'
            }).
            when('/signin', {
                templateUrl: 'partials/SignInView',
                controller: 'SignInCtrl'
            }).
            when('/eventregister', {
                templateUrl: 'partials/EventRegisterView',
                controller: 'EventRegisterCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });

        $locationProvider.html5Mode(true);
    });

var errorOnREST = function (error) {
    alert(error.config.method + ': ' + error.config.url + ' [status: ' + error.status + ']');
    return false;
}