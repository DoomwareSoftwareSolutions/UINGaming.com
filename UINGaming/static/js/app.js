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
    'ProfileCtrl',
    'EventDetailCtrl',
    'EventEditCtrl',
    'NavCtrl',
    'EventAddCtrl',
    'NewsCtrl',
    'NewsAddCtrl',
    'NewsViewerCtrl',
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
            when('/profile', {
                templateUrl: 'partials/Profile',
                controller: 'ProfileCtrl'
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
            	templateUrl: 'partials/EventDetailView',
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
	    when('/news/add',{
                templateUrl: 'partials/NewsEditView',
                controller: 'NewsAddCtrl'
            }).
            when('/news/:pk',{
                templateUrl: 'partials/NewsViewerView',
                controller: 'NewsViewerCtrl'
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
