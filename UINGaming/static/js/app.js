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
    'ProfileEditCtrl',
    'EventDetailCtrl',
    'EventEditCtrl',
    'NavCtrl',
    'EventAddCtrl',
    'NewsCtrl',
    'NewsAddCtrl',
	//'NewsEditCtrl',
    'NewsViewerCtrl',
    'UserSearchCtrl',
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
            when('/profile/:pk', {
                templateUrl: 'partials/Profile',
                controller: 'ProfileCtrl'
            }).
            when('/profileEdit/:pk', {
                templateUrl: 'partials/ProfileEdit',
                controller: 'ProfileEditCtrl'
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
			when('/news/edit/:pk',{
                templateUrl: 'partials/NewsEditView',
                controller: 'NewsEditCtrl'
            }).
            when('/news/:pk',{
                templateUrl: 'partials/NewsViewerView',
                controller: 'NewsViewerCtrl'
            }).
            when('/search/:pk',{
                templateUrl: 'partials/UserSearchView',
                controller: 'UserSearchCtrl'
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
