'use strict';

// Declare app level module which depends on filters, and services

var depList = [
    'myApp.filters',
    'myApp.services',
    'myApp.directives',
    'PropertyService',
    'EventService',
    'NewsService',
    'AuthService',
    'HomeService',
    'EventRegisterCtrl',
    'BackgroundCtrl',
    'SignInCtrl',
    'RegisterCtrl',
    'HomeCtrl',
    'EventsCtrl',
    'NewsCtrl',
    'EventsEnrolledCtrl',
    'EventDetailCtrl',
    'EventEditCtrl',
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
            when('/eventsEnrolled', {
                templateUrl: 'partials/EventsView',
                controller: 'EventsEnrolledCtrl'
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
            when('/eventDelete',{
                controller: 'EventDetailCtrl'
            }).
            when('/eventAdd',{
            	templateUrl: 'partials/EventAddView',
            	controller: 'EventAddCtrl'
            }).
            when('/eventEdit',{
                templateUrl: 'partials/EventEditView',
                controller: 'EventEditCtrl'
            }).
            when('/news',{
                templateUrl: 'partials/NewsView',
                controller: 'NewsCtrl'
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
