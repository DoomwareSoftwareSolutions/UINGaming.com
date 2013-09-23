'use strict';

/* Controllers */

var controllerName = 'EventRegisterCtrl';
var minTeamSize = 5;
angular.module(controllerName, []).
    controller(controllerName, ['$scope','PropertyService', 'EventService','$q', function ($scope, PropertyService,EventService,$q) {

        $scope.$emit("BackgroundChange", "event-register-background");

        $scope.teamMembers = [];

        $scope.newMember = '';

		
        var triggerDigest = function () {
            if (!$scope.$$phase) {
                $scope.$digest();
            }

        }

        $scope.addMember = function () {
            if ($scope.teamMembers.length < minTeamSize) {
                $scope.teamMembers.push($scope.newMember);
                $scope.newMember = '';
                triggerDigest();
            }
        }
        
        
        $scope.removeMember = function (index) {
            $scope.teamMembers.splice(index, 1);
            triggerDigest();
        }
        
        //Respeto el formato json que pide la api
        var loadFields = function () {
            PropertyService.loadFields('eventRegister', 'en', $scope);
            $scope.registerData = 
				{
					"pk": -1,
					"model": "events.eventmembership",
					"fields": {
						"paid": false,
						"teamMembers": "asd",
						"teamTag": "",
						"event": -1,
						"teamName": "",
						"user": -1
					}
				}
        }
        
        //TODO get user and event ID!
        $scope.register = function () {
    		//Paso el array a string separado por comas. TODO: escapar las comas / prohibir las comas del member name.
        	$scope.registerData.fields['teamMembers']=$scope.teamMembers.join(",");
        	
        	//API expects a json enclosed between brackets
        	var auxJsonContainer=[$scope.registerData];
            EventService.registerToEvent($q, auxJsonContainer)
                .then(function (results) {
                    // Prueba funcionamiento mostrando el response
                    alert(JSON.stringify(results));
                    $scope.$emit("HideSpinner");
                }, errorOnREST);
        }
        
		loadFields();
    }]);
