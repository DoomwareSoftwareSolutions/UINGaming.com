'use strict';

// Declare app level module which depends on filters, and services

var depList = [
    'myApp.filters',
    'myApp.services',
    'myApp.directives',
    'PropertyService',
    'EventService',
    'AuthService',
    'HomeService',
    'EventRegisterCtrl',
    'BackgroundCtrl',
    'SignInCtrl',
    'RegisterCtrl',
    'HomeCtrl',
    'EventsCtrl',
    'EventDetailCtrl',
    'NavCtrl',
    'EventAddCtrl',
    'ngCookies',
]

angular.module('myApp', depList).
    config(function ($routeProvider, $locationProvider, $httpProvider) {
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
            when('/register', {
                templateUrl: 'partials/RegisterView',
                controller: 'RegisterCtrl'
            }).
            when('/eventregister', {
                templateUrl: 'partials/EventRegisterView',
                controller: 'EventRegisterCtrl'
            }).
            when('/events/:pk',{
            	templateUrl: 'partials/EventDetail',
            	controller: 'EventDetailCtrl'
            }).
            when('/eventAdd',{
            	templateUrl: 'partials/EventAddView',
            	controller: 'EventAddCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
            
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        $locationProvider.html5Mode(true);
    });

var errorOnREST = function (error) {
    alert(error.config.method + ': ' + error.config.url + ' [status: ' + error.status + ']');
    return false;
}
